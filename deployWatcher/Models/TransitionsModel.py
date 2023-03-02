from datetime import datetime
from deployWatcher.database import db

class TransitionModel(db.Model):
    __tablename__ = 'Transitions'

    id = db.Column(db.Integer, primary_key=True)
    component = db.Column(db.String(140))
    version = db.Column(db.String(50))
    author = db.Column(db.String(80))
    status = db.Column(db.String(50))
<<<<<<< HEAD
    sent_timestamp = db.Column(db.DateTime)
    received_timestamp = db.Column(db.DateTime)

    def __init__(self, component: str, version: str, author: str, status: str,
                 sent_timestamp: str):
=======
    sentTimestamp = db.Column(db.DateTime)
    receivedTimestamp = db.Column(db.DateTime)

    def __init__(self, component: str, version: str, author: str, status: str,
                 sent_timestamp: str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')):
>>>>>>> efaef465f656354e52b9b2aa50fecd59db5c42ac
        self.component = component
        self.version = version
        self.author = author
        self.status = status
<<<<<<< HEAD
        self.sent_timestamp = datetime.strptime(sent_timestamp, '%Y-%m-%d %H:%M:%S.%f')
        self.received_timestamp = datetime.utcnow()
=======
        self.sentTimestamp = datetime.strptime(sent_timestamp, '%Y-%m-%d %H:%M:%S.%f')
        self.receivedTimestamp = datetime.utcnow()
>>>>>>> efaef465f656354e52b9b2aa50fecd59db5c42ac

    def save(self):
        db.session.add(self)
        db.session.commit()
