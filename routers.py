from fastapi import APIRouter, Request


router = APIRouter(prefix='/api')



@router.get('/index/')
def index(request:Request):
   
    pass

