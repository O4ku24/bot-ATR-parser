from database import Model
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Integer, func
import datetime


class CityObject(Model):

    __tablename__ = 'city_object_table'

    id_object: Mapped[int] = mapped_column(Integer, primary_key=True)
    city: Mapped[str] = mapped_column(String)
    name_object: Mapped[str] = mapped_column(String)

class UserModel(Model):
    
    __tablename__ = 'users_table'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String)
    user_password: Mapped[str] = mapped_column(String)
    post_user: Mapped[str] = mapped_column(String)

class OrderModel(Model):

    __tablename__ = 'order_table'

    order_id: Mapped[int] = mapped_column(Integer,primary_key=True )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users_table.user_id", ondelete="CASCADE"), index=True)
    construction_object_id: Mapped[int] = mapped_column(Integer)
    search_product: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    