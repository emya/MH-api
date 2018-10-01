from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TODO: Add other columns
class CommunityPost(db.Model):
    id = db.Column(db.String, primary_key=True)
    uid = db.Column(db.String)

