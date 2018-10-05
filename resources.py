from flask_restful import Resource
from sqlalchemy import and_, or_
from schemas import CommunityPostSchema
from models import CommunityPost

import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__).setLevel('INFO')


class CommunityPostList(Resource):
    def get(self, uid):
        try:
            schema = CommunityPostSchema()
            logging.info(f'Querying CommunityPost with uid: {uid}')
            results_set = CommunityPost.query.filter_by(uid=uid).all()
            results_set = CommunityPost.query.filter(
                    or_(
                        CommunityPost.public_flag == True,
                        and_(
                            CommunityPost.public_flag == False,
                            CommunityPost.uid <= p_value
                        )
                    )
                ).all()

            from flask_sqlalchemy import SQLAlchemy
            db = SQLAlchemy()
            friend_ls = db.Session.query(CommunityMember.uid1, CommunityMember.uid2).filter(
                and_(
                    or_(
                        CommunityMember.uid1 == uid,
                        CommunityMember.uid2 == uid,
                        )
                    )
                    CommunityMember.status == 2
                ).all()
                        
            results_set = db.session.query(CommunityPost, CommunityMember).filter(
                    or_(
                        CommunityPost.public_flag == True,
                        and_(
                            CommunityPost.public_flag == False,
                            CommunityPost.uid.in_(friend_ls)
                        )
                    )
                ).all()

            results = schema.dump(results_set, many=True)
            return results
        except Exception as e:
            logging.info("Exception:", e)
