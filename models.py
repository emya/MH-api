from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from flask import Flask, current_app

from uuid import uuid4

from flask_migrate import Migrate

db = SQLAlchemy()

"""
app = Flask(__name__)

with app.app_context():
    migrate = Migrate(app, db)
    #migrate = Migrate(current_app, db)
"""

# TODO: Add other columns
class CommunityPost(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    uid = db.Column(db.String)
    content = db.Column(db.String(200))
    image = db.Column(db.Boolean)
    likes = db.Column(db.Integer)
    shares = db.Column(db.Integer)
    hatsoffs = db.Column(db.Integer)
    public_flag = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class CommunityComment(db.Model):
    id = db.Column(db.String, primary_key=True)
    uid = db.Column(db.String)
    content = db.Column(db.String(200))
    community_id = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class CommunityMember(db.Model):
    id = db.Column(db.String, primary_key=True)
    uid1 = db.Column(db.String)
    uid2 = db.Column(db.String)
    # 1 or 2 (uid1 or uid2)
    action_user = db.Column(db.Integer)
    # 1: sent request, 2:accepted, 3:blocked
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class Activity(db.Model):
    id = db.Column(db.String, primary_key=True)
    # 1:comment, 2:hatsoff, 3:share, 4:like, 5:collaborate, 6:follow
    activity_type = db.Column(db.Integer)
    # 1:community post 2:upcoming 3:portfolio
    content_type = db.Column(db.Integer)
    content_id = db.Column(db.Integer)
    uid = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

