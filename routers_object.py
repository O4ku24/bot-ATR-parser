from fastapi import APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, delete
from database import engine

import os

from forms import CreateObject
from models import ObjectModel

router_object = APIRouter(prefix='/api/objects')

@router_object.get('/')
def get_all_objects(request: Request):
    session = Session(engine)
    
    stmt = select(ObjectModel)
    db = session.execute(stmt)
    objects:list = db.scalars().all()
    session.close()

    return objects

@router_object.get('/{obj_id}/')
def get_object(request: Request, obj_id:int):
    session = Session(engine)
    try:
        stmt = select(ObjectModel).filter(ObjectModel.object_id == obj_id)
        result = session.execute(stmt)
        obj = result.scalar_one_or_none()

        if obj in None:
            raise HTTPException(status_code=404, detail='not found')
        return obj
    except Exception as e:
        raise HTTPException(status_code=500, detail= str(e))
    finally:
        session.close()

@router_object.post('/')
def add_object(request: Request, obj:CreateObject):
    session = Session(engine)
    stmt = insert(ObjectModel).values(
        city = obj.city,
        name_object = obj.name_object,
        user_id = obj.user_id
    )
    session.execute(stmt)
    session.commit()
    session.close()

    os.mkdir(f'Обьекты/{obj.name_object}')

    return f'add - {obj}'

@router_object.delete('/{obj_id}/')
def delete_obj(request:Request, obj_id:int):
    session = Session(engine)
    stmt = delete(ObjectModel).where(ObjectModel.object_id == obj_id)
    session.execute(stmt)
    session.commit()
    session.close()

    return f'delete - {obj_id}'


