from fastapi import  Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session
from typing import  List, Optional
from .. import models, schemas, oauth2
from ..database import  get_db

router = APIRouter(prefix="/vote", tags=["Votes"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_posts(vote: schemas.Vote, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"!!!! warning post id {vote.post_id} Item not found")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    print("found_vote", found_vote)
    if (vote.dir == 1):
        if found_vote:
             raise HTTPException(status_code=409, detail=f"Vote has been already added on this content")
        new_vote = models.Vote(user_id=current_user.id, post_id = vote.post_id, )
        db.add(new_vote)
        db.commit()
        return { "message": "Successfully added vote"}
    else:
        if not found_vote:
             raise HTTPException(status_code=404, detail="Item not found")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return { "data": "Successfully deleted vote"}



