from mongoengine import Document, StringField, FileField

class MeetDocument(Document):
    meet_key = StringField(required=True, unique=True) # google meet key

    space_name = StringField(required=False) # name of the google meet space
    space_uri = StringField(required=False)  # url of the google meet space

    topic_name = StringField(required=False) # name of the topic subscribed to this google meet

    transcript = FileField() # the transcript file post google meet
    recording = FileField() # the audio recording file post google meet

    conversation_history = StringField(required=False)

    meta = {
        'collection': 'meet_spaces',
        'indexes': ['meet_key']
    }