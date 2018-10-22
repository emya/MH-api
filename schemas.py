from marshmallow_jsonapi import Schema, fields

# TODO: Add other fields 
class CommunityPostSchema(Schema):
    class Meta:
        type_ = 'community_post'
        self_url = '/communitypost/{id}'
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
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class ActivitySchema(Schema):
    class Meta:
        type_ = 'activity'
        self_url = '/activity/{id}'
        self_url_kwargs = {'id': '<id>'}
        strict = True

    id = fields.UUID()
    uid = fields.String(required=True)
    activity_type = fields.Integer()
    content_type = fields.Integer()
    content_id = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
