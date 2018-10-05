from marshmallow_jsonapi import Schema, fields

# TODO: Add other fields 
class CommunityPostSchema(Schema):
    class Meta:
        type_ = 'community_post'
        self_url = '/community_post/{id}'
        self_url_kwargs = {'id': '<id>'}
        strict = True

    id = fields.UUID()
    uid = fields.String(required=True)
    content = fields.String()
    image = fields.Boolean()
    likes = fields.Integer()
    shares = fields.Integer()
    hatsoffs = fields.Integer()
    public_flag = fields.Boolean()
    shared_upcoming = fields.String() # id of shared upcoming
    shared_portfolio = fields.String() # id of shared portfolio 
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
