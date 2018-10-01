from flask_restful import Resource
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
            results = schema.dump(results_set, many=True)
            return results
        except Exception as e:
            logging.info("Exception:", e)
