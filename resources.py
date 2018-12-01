from flask_restful import Resource
from flask import request
from sqlalchemy import and_, or_

from flask_sqlalchemy import SQLAlchemy

from schemas import CommunityPostSchema, ActivitySchema
from models import CommunityPost, CommunityMember, Activity

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
            schema = CommunityPostSchema()

            db = SQLAlchemy()

            if private:
                logging.info('Querying Private CommunityPost with uid: %s' % uid)
                friend_ls = db.session.query(CommunityMember).filter(
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
            private_flag = request.json.get('private', "True")
            image_flag = request.json.get('image', "False")
            id = request.json.get('id', uuid4())
            public = private_flag == "False"
            image = image_flag == "True"
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_post = CommunityPost(id=id, uid=uid, content=content, image=image,
                                     likes=0, shares=0, hatsoffs=0, public_flag=public,
                                     created_at=created_at, updated_at=None)

            db = SQLAlchemy()
            db.session.add(new_post)
            db.session.commit()
            db.session.close()
        except Exception as e:
            logging.info("Exception:", e)

class ActivityList(Resource):
    def get(self, uid):
        try:
            """
            Use following parameters in future
            """
            # 1: like, 2: share
            activity_type = int(request.args.get('activity', default="1"))
            # 1: community post
            content_type = int(request.args.get('content', default="1"))
            schema = ActivitySchema()

            db = SQLAlchemy()

            results_set = db.session.query(Activity).filter(
                Activity.uid == uid
            ).all()

            results = schema.dump(results_set, many=True)
            db.session.close()
            return results
        except Exception as e:
            logging.info("Exception:", e)

    def post(self, uid):
        try:
            activity_type = int(request.args.get('activity', default="1"))
            content_type = int(request.args.get('content', default="1"))
            content_id = request.args.get('content_id')
            disable_flag = request.args.get('disable')

            if disable_flag:
                Activity.query.filter_by(uid=uid, activity_type=activity_type,
                                         content_type=content_type, content_id=content_id,).delete()


            else:
                created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_post = Activity(id=uuid4(), uid=uid, activity_type=activity_type, content_type=content_type,
                                    content_id=content_id, created_at=created_at, updated_at=None)

                db = SQLAlchemy()
                db.session.add(new_post)
                db.session.commit()
                db.session.close()
        except Exception as e:
            logging.info("Exception:", e)

class FriendList(Resource):
    def get(self, uid):
        try:
            """
            Use following parameters in future
            """
            db = SQLAlchemy()

            friend_ls = db.session.query(CommunityMember).filter(
                and_(
                    or_(
                        CommunityMember.uid1 == uid,
                        CommunityMember.uid2 == uid,
                    )
                ),
                CommunityMember.status == 2
            ).all()

            if uid in friend_ls:
                friend_ls.remove(uid)

            db.session.close()
            return {"friends": friend_ls}
        except Exception as e:
            logging.info("Exception:", e)

