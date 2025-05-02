from mongoengine import Document, StringField, FileField

class MeetDocument(Document):
    meet_key = StringField(required=True, unique=True)

    space_name = StringField(required=False)
    topic_name = StringField(required=False)
    space_uri = StringField(required=False)

    transcript = FileField()
    recording = FileField()

    meta = {
        'collection': 'meet_spaces',
        'indexes': ['meet_key']
    }