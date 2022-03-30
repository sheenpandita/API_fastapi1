from .. import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from ..repository import user
from fastapi import APIRouter, Depends, status,HTTPException

router = APIRouter(
    prefix="/user",
    tags=['USER']
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session = Depends(database.get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session = Depends(database.get_db)):
    return user.show(id,db)