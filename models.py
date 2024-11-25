from database import Model
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, func
import datetime

class ObjectModel(Model):
    __tablename__ = 'object_table'

    object_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    city: Mapped[str] = mapped_column(String)
    name_object: Mapped[str] = mapped_column(String, unique=True)
    users_id: Mapped[list["UserModel"]] = relationship(back_populates="user_id", primaryjoin='UserModel.user_id')
    
class UserModel(Model):
    __tablename__ = 'users_table'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, back_populates='users_id')
    user_tg_id: Mapped[int] = mapped_column(Integer)
    user_phone: Mapped[int] = mapped_column(Integer)
    user_name: Mapped[str] = mapped_column(String)
    user_password: Mapped[str] = mapped_column(String)
    user_post: Mapped[str] = mapped_column(String)

""" "detail": "Не удалось определить условие соединения 
между родительскими / дочерними таблицами в отношении ObjectModel.users_id - 
нет внешних ключей, связывающих эти таблицы.  Убедитесь, что ссылающиеся столбцы 
связаны с ForeignKey или ForeignKeyConstraint, или укажите выражение 'primaryjoin' ". """

class QueryModel(Model):
    __tablename__ = 'query_table'

    query_id: Mapped[int] = mapped_column(Integer, primary_key=True )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users_table.user_id"), index=True)
    object_id: Mapped[int] = mapped_column(Integer, ForeignKey("object_table.object_id"), index=True)
    query_product: Mapped[str] = mapped_column(String) #запрос продукта
    quantity: Mapped[int] = mapped_column(Integer) #кол-во
    description: Mapped[str] = mapped_column(String) #комментарий
    create_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    
class OrderModel(Model):
    __tablename__ = 'order_table'

    order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    query_id: Mapped[int] = mapped_column(Integer, ForeignKey("query_table.query_id"), index=True)
    article: Mapped[str] 
    product: Mapped[str]
    price: Mapped[int]
    sale: Mapped[int]
    remains: Mapped[int] #остаток на складе
