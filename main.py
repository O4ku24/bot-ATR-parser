import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from routers import router
from database import engine
from models import UserModel, OrderModel, CityObject


app = FastAPI(
    title="Order List IT-ROOM",
    version="0.0.1"
)

app.include_router(router)
app.mount("/static", StaticFiles(directory='static'), name='static')






if __name__ == '__main__':
    UserModel.metadata.create_all(engine)
    OrderModel.metadata.create_all(engine)
    CityObject.metadata.create_all(engine)
    print('Start Server')
    uvicorn.run('main:app', port = 8000, host='127.0.0.1', reload=True)
    print('Server Stop')