from datetime import  timedelta
from fastapi import  Depends, HTTPException, status,  APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, util
from ..database import  get_db
from ..oauth2 import create_access_token

router = APIRouter(prefix="/login", tags=["Authenticaton"])
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/", response_model=schemas.Token)
def create_user(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credential")
    if not util.verify_password(user_credential.password, user.password):
        raise HTTPException(status_code=404, detail="Invalid Credential")
    access_token = create_access_token(
        data={"user_id": str(user.id)}
    )
    return {"access_token": access_token, "token_type": "bearer"}

