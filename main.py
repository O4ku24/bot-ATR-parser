import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from routers_users import router_users
from routers_object import router_object

from database import engine
from models import UserModel, OrderModel, ObjectModel, QueryModel


app = FastAPI(
    title="Order List IT-ROOM",
    version="0.0.1"
)

app.include_router(router_users)
app.include_router(router_object)
app.mount("/static", StaticFiles(directory='static'), name='static')






if __name__ == '__main__':
    UserModel.metadata.create_all(engine)
    OrderModel.metadata.create_all(engine)
    ObjectModel.metadata.create_all(engine)
    QueryModel.metadata.create_all(engine)
    print('Start Server')
    uvicorn.run('main:app', port = 8000, host='127.0.0.1', reload=True)
    print('Server Stop')