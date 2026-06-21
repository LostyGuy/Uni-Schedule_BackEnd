from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey, text, func

from backend.connection.connection import Base

class User(Base):
    __tablename__ = 'users'
    user_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    username: str = Column(
        String,
        nullable= False,
    )
    name: str = Column(
        String,
        nullable= False,
    )
    surname: str = Column(
        String,
        nullable= False,
    )
    email: str = Column(
        String,
        nullable= False,
        unique= True,
    )
    hashed_password: str = Column(
        String,
        nullable= False,
    )
    role_id: int = Column(
        BigInteger,
        ForeignKey("roles.role_id"),
        nullable= False,
        server_default= text("2"),
    )
    is_active: bool = Column(
        Boolean,
        nullable= True,
        server_default= text("false"),
    )
    last_active: DateTime = Column(
        DateTime(timezone= True),
        nullable= True,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
    policy_agreement: bool = Column(
        Boolean,
        nullable= False,
    )