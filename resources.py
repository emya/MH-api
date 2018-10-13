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
            schema = CommunityPostSchema()
            logging.info('Querying CommunityPost with uid: %s' % uid)

            from flask_sqlalchemy import SQLAlchemy

            db = SQLAlchemy()
            friend_ls = db.Session.query(CommunityMember.uid1, CommunityMember.uid2).filter(
                and_(
                    or_(
                        CommunityMember.uid1 == uid,
                        CommunityMember.uid2 == uid,
                        )
                    ),
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

    def post(self, uid):
        try:
            content = request.args.get('content', default="")
            public = request.args.get('public', default="True")
            image = request.args.get('image', default="False")
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_post = CommunityPost(uuid4(), uid, content, image, 0, 0, 0, public, created_at, None)

            db = SQLAlchemy()
            db.session.add(new_post)
            db.session.commit()
        except Exception as e:
            logging.info("Exception:", e)
