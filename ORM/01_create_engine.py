from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:",echo=True)  #In memory -only SQLite database
""" The echo flag is a shortcut to setting up SQLAlchemy logging, 
which is accomplished via Python’s standard logging module.
With echo enabled, we'll see verbosity of SQL. If you want less output, set it to False.

When you create engine, it doesn't connect to anything. 
It just verifies if your url makes sense - Lazy Connecting. 
"""


#Define and Create Tables
from sqlalchemy import Table, Column, Integer, String, MetaData,ForeignKey
metadata_obj = MetaData()
users= Table("users",metadata_obj,
             Column("id",Integer,primary_key=True),
             Column("name",String),
             Column("fullname",String)
             )

addresses = Table("addresses",metadata_obj,
        Column("id",Integer,primary_key=True),
        Column("user_id",None,ForeignKey("users.id")),
        Column("email_address",String,nullable=False)
        )

metadata_obj.create_all(engine)




#https://docs.sqlalchemy.org/en/14/core/tutorial.html#version-check