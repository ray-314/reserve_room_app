from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データの格納先：同じディレクトリにデータベースファイルを作成する
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# DBエンジンを作成する（CRAD操作をするための設定）※connect_args：SQLiteのみ必要な引数
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# セッションを作成する
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルクラスを作る(テーブル定義を書く)
Base = declarative_base()