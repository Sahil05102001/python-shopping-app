import uuid
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

users = [
    {
        "user_id": 2,
        "username": "sahil",
        "password": hash_password("sahil123"),
        "role": "user"
    },
    {
        "user_id": 1,
        "username": "admin",
        "password": hash_password("admin786"),
        "role": "admin"
    }]
    
user_sessions = {}
    
def login(username, password):
    for user in users:
        if user["username"]==username and bcrypt.checkpw(password.encode(), user["password"]):
            session_id = str(uuid.uuid4())
            user_sessions[session_id]={
                "username": username,
                "role": user["role"]
            }
            return session_id
    return None
    
    
def is_authenticated(session_id):
    return session_id in user_sessions

def logout(session_id):
    if session_id in user_sessions:
        del user_sessions[session_id]