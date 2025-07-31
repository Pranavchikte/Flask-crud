import uuid
import datetime
from mongoengine import Document, StringField, EmailField, DateTimeField


class User(Document):
    id = StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'collection': 'users',
        'ordering': ['-created_at']
    }

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # Don't return password hash
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
