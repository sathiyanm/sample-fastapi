from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi import Body
from typing import   List
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, get_db
from  .routers import post, user, auth, vote
from .config import settings


models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    
    allow_headers=["*"],
)
  
@app.get("/")
def read_root():
    return {"Hello": "this is a API output"}

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)



