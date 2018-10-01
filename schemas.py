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
