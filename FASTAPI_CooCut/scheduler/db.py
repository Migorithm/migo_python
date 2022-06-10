from typing import Any, Union,Generator

from sqlalchemy import create_engine, inspect, Table,Integer,String
from sqlalchemy.orm import as_declarative, scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import MetaData

database_url = "sqlite:///./any.db"
engine = create_engine(database_url, pool_pre_ping=True,echo=True)
conn = engine.connect()

SessionLocal: Union[scoped_session, sessionmaker]
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
meta = MetaData()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print("shii~t",e)
    finally:
        db.close()

@as_declarative()
class Base:
    id: Any
    __name__: str

    def _to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
from sqlalchemy import Column,String,Integer


user = Table(
    'users',                                        
    meta,                                    
    Column('id', Integer, primary_key=True) ,
    Column('name',String)
    )
           

  
class User(Base):
    __tablename__ = "users"
    name:str = Column(String(64))
    id: int = Column(Integer,primary_key=True)
    
    

meta.create_all(engine)