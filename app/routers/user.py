from fastapi import  Depends, HTTPException, status,  APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, util
from ..database import  get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = util.get_password_hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_specfic_user(id: int, db: Session = Depends(get_db)): 
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    return user