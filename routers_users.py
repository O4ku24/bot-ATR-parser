from fastapi import APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, delete
from database import engine
from models import UserModel
from forms import CreateUser, DeleteUser, ReadUser

router_users = APIRouter(prefix='/api/users')


@router_users.get('/')
def get_all_users(request:Request):
    session = Session(engine)
    try:
        stmt = select(UserModel)
        object_db = session.execute(stmt)
        users:list = object_db.scalars().all()
        return {
            'Status Code': '200 OK',
            'User list': users
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()


@router_users.get('/user/{user_name}/')
def get_user(request:Request, user:ReadUser):
    session = Session(engine)
    try:
        stmt = select(UserModel).filter(UserModel.user_name == user.user_name)
        result = session.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {
        'Status Code': '200 OK',
        'User': user
    }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()


@router_users.post('/')
def add_user(request:Request, user:CreateUser):
    session = Session(engine)
    try:
        stmt = insert(UserModel).values(
                    user_tg_id = user.user_tg_id,
                    user_name = user.user_name,
                    user_phone = user.user_phone,
                    user_password = user.user_password,
                    user_post = user.user_post)
        
        session.execute(stmt)
        session.commit()

        return {
            'Status Code': '200 OK',
            'User Create': user
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()


@router_users.delete('/user/{user_name}/')
def delete_user(request:Request, user:DeleteUser):
    session = Session(engine)
    try:
        stmt = delete(UserModel).where(UserModel.user_name == user.user_name)
        session.execute(stmt)
        session.commit()

        return {
            'Status Code': '200 OK',
            'User delete': user
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
