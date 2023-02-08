import datetime
from pydantic import BaseModel, Field

# テーブルでは小文字の複数形だが、classはパスカルケース（アッパーキャメルケース）
class BookingCreate(BaseModel):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

    class Config: # ORMのデータも許可する
        orm_mode = True

class Booking(BookingCreate):
    booking_id: int

    class Config: # ORMのデータも許可する
        orm_mode = True

class UserCreate(BaseModel):
    user_name: str = Field(max_length=12)

class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

class RoomCreate(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int

    class Config:
        orm_mode = True

class Room(RoomCreate):
    room_id: int

    class Config:
        orm_mode = True