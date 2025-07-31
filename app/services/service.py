from app.models.user import User
from werkzeug.security import generate_password_hash
import datetime

def create_user(data):
    user = User(
        name=data['name'],
        email=data['email'],
        password=generate_password_hash(data['password']),
    )
    user.save()
    return {"message": "User created", "user": user.to_json()}, 201

def get_all_users():
    users = User.objects()
    return [user.to_json() for user in users], 200

def get_user_by_id(user_id):
    user = User.objects.get(id=user_id)
    return user.to_json(), 200

def update_user(user_id, data):
    user = User.objects.get(id=user_id)

    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password = generate_password_hash(data['password'])

    user.updated_at = datetime.datetime.utcnow()
    user.save()

    return {"message": "User updated", "user": user.to_json()}, 200

def delete_user(user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return {"message": "User deleted"}, 200
