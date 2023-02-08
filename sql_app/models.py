# データベースの構造を明記する用のpyファイル
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from .database import Base

# テーブル設計(Baseを継承しているからテーブルになる, 大文字単数形)
class User(Base):
    # テーブル名を設定
    __tablename__ = 'users'
    # カラムを設定
    user_id = Column(Integer, primary_key=True, index=True) # primary_key=True：主キー（一意に決まる）, index=True：検索を早くするためにindex=True
    user_name = Column(String, unique=True, index=True) # unique=True：被りは許さない

class Room(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, index=True)
    capacity = Column(Integer)

class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False) # ondelete:親のキーが消されたらどうするのか
    room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='SET NULL'), nullable=False) # nullable:親のキーがnullのものを許すか
    booked_num = Column(Integer)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)