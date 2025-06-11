import bcrypt
from sqlalchemy.orm import sessionmaker
from database.model import engine , User

Session = sessionmaker(bind=engine)
session = Session()

def register_user(username,password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, password_hash=password_hash.decode('utf-8'))
    session.add(new_user)
    session.commit()
    print("Registration successful!")

def login_user(username, password ):
    user = session.query(User).filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        print(f"Welcome back, {username}!")
        return True  
    print("Invalid username or password!")
    return False 