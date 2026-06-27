from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey, text, func

from backend.connection.connection import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    username = Column(
        String,
        nullable= False,
    )
    name = Column(
        String,
        nullable= False,
    )
    surname  = Column(
        String,
        nullable= False,
    )
    email = Column(
        String,
        nullable= False,
        unique= True,
    )
    hashed_password  = Column(
        String,
        nullable= False,
    )
    role_id  = Column(
        BigInteger,
        ForeignKey("roles.role_id"),
        nullable= False,
        server_default= text("2"),
    )
    is_active  = Column(
        Boolean,
        nullable= True,
        server_default= text("false"),
    )
    last_active = Column(
        DateTime(timezone= True),
        nullable= True,
    )
    created_at  = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
    policy_agreement  = Column(
        Boolean,
        nullable= False,
    )