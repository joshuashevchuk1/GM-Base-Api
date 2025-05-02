from mongoengine import Document, StringField, FileField

class MeetDocument(Document):
    # the google meet key for the space
    meet_key = StringField(required=True, unique=True)

    # name of the google meet space
    space_name = StringField(required=False)
    # url of the google meet space
    space_uri = StringField(required=False)

    # name of the topic subscribed to this google meet
    topic_name = StringField(required=False) # name of the topic subscribed to this google meet

    # the transcript file post google meet
    transcript = FileField()
    # the audio recording file post google meet
    recording = FileField()

    # all history dealt with ai chat for the post meeting session
    convo_history = StringField(required=False)

    meta = {
        'collection': 'meet_spaces',
        'indexes': ['meet_key']
    }