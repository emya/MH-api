from flask_restful import Resource
from flask import request
from sqlalchemy import and_, or_

from flask_sqlalchemy import SQLAlchemy

from schemas import CommunityPostSchema
from models import CommunityPost, CommunityMember

from uuid import uuid4
import datetime
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__).setLevel('INFO')


class CommunityPostList(Resource):
    def get(self, uid):
        try:
            private_flag = request.args.get('private', default="False")
            private = private_flag == "True"
            logging.info('private: %s' % private)
            schema = CommunityPostSchema()

            db = SQLAlchemy()

            if private:
                logging.info('Querying Private CommunityPost with uid: %s' % uid)
                friend_ls = db.Session.query(CommunityMember).filter(
                    and_(
                        or_(
                            CommunityMember.uid1 == uid,
                            CommunityMember.uid2 == uid,
                        )
                    ),
                    CommunityMember.status == 2
                ).all()

                results_set = db.session.query(CommunityPost).filter(
                    or_(
                        CommunityPost.public_flag == True,
                        and_(
                            CommunityPost.public_flag == False,
                            CommunityPost.uid.in_(friend_ls)
                        )
                    )
                ).all()

            else:
                logging.info('Querying CommunityPost with uid: %s' % uid)
                results_set = db.session.query(CommunityPost).all()

            results = schema.dump(results_set, many=True)
            db.session.close()
            return results
        except Exception as e:
            logging.info("Exception:", e)

    def post(self, uid):
        try:
            content = request.json.get('content', "")
            public = request.json.get('public', True)
            image = request.json.get('image', False)
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_post = CommunityPost(id=uuid4(), uid=uid, content=content, image=image,
                                     likes=0, shares=0, hatsoffs=0, public_flag=public,
                                     created_at=created_at, updated_at=None)

            db = SQLAlchemy()
            db.session.add(new_post)
            db.session.commit()
            db.session.close()
        except Exception as e:
            logging.info("Exception:", e)
