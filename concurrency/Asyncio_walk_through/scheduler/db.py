from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import  Column,String,Integer
from typing import  Generator
import asyncio
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()




  
class User(Base):
    __tablename__ = "users"
    name:str = Column(String(64))
    id: int = Column(Integer,primary_key=True)
    

# Base.metadata.create_all(engine)



def get_db() -> Generator:
    try:
        db = async_session()
        yield db
    except Exception as e:
        print("shii~t",e)
    finally:
        db.close()
        
        
async def db_setup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(db_setup())