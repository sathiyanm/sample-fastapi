from fastapi import  Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import  List, Optional
from .. import models, schemas, oauth2
from ..database import  get_db

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=List[schemas.PostOut])
# @router.get("/")
def get_posts(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), limit:int=10, skip:int=0, search:Optional[str]=""):
    # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all() // collect posts for specific user
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(1).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    print(results)
    return results

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    create_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(create_post)
    db.commit()
    db.refresh(create_post)
    # create_post = models.Post(title=post.title, content: post.content, published=post.published)

    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (posts.title, posts.content, posts.published))
    # new_data = cursor.fetchone()
    # conn.commit()
    
    
    # post_dict = posts.model_dump()
    # post_dict['id'] = random.randrange(1, 1000000)
    # my_posts.append(post_dict)
# def create_posts(payload: dict = Body(...)):
    # print(posts)
    # return {"newpost sathya": f"title {payload['title']} content: {payload['content']}"}
    return create_post

@router.get("/{id}", response_model=schemas.PostOut)
def get_posts(id: int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)) : 
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(1).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).first()
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=404, detail="Item not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)): 
    post_query = db.query(models.Post).filter(models.Post.id == id)  
    post = post_query.first()
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    if post == None:
        raise HTTPException(status_code=404, detail="Item not found")  
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not Authorized to delete")
    post_query.delete(synchronize_session=False)
    db.commit()
    return { "data": Response(status_code=status.HTTP_204_NO_CONTENT)}

@router.put("/{id}", response_model=schemas.Post)
def update_posts(id: int, p: schemas.PostCreate, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)  
    # cursor.execute("""UPDATE posts SET title=(%s),content=(%s), published=(%s) WHERE id = (%s) RETURNING * """, (post.title, post.content, post.published, id))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=404, detail="Item not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this content")
    post_query.update(p.model_dump(), synchronize_session=False)  
    db.commit()
    return  post_query.first()
