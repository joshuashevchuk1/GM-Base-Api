# models.py

from mongoengine import Document, StringField, FileField

class MeetSpace(Document):
    space_name = StringField(required=True, unique=True)
    topic_name = StringField(required=True)
    space_uri = StringField(required=True)

    transcript = FileField()
    recording = FileField()

    meta = {
        'collection': 'meet_spaces',
        'indexes': ['space_name']
    }