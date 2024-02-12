from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)



# my_posts =[{"id": 1, "title":"Title 1", "content": "My content 1"}, {"id": 2, "title": "title 2", "content": "My content 2"}]

# def find_index(id):
#   for i, j in enumerate(my_posts):
#       if j["id"] == id:
#          return i
      
# def find_posts(id):
#     for p in my_posts:
#       if p["id"] == id:
#          return p