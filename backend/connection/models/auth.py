from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey, func

from backend.connection.connection import Base

class Role(Base):
    __tablename__ = "roles"

    role_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    name: str = Column(
        String,
        nullable= False,
    )
    description: str = Column(
        String,
        nullable= True,
    )
    can_manage_events: bool = Column(
        Boolean,
        nullable= True,
    )
    can_invite_members: bool = Column(
        Boolean,
        nullable= True,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )

class Jwt(Base):
    __tablename__ = "jwt"

    jwt_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    user_id: int = Column(
        BigInteger,
        nullable= False,
    )
    access_token: str = Column(
        String,
        nullable= False,
    )
    issued_at: DateTime = Column(
        DateTime,
        nullable= False,
    )
    valid_till: DateTime = Column(
        DateTime,
        nullable= False,
    )
    issued_from_endpoint: str = Column(
        String,
        nullable= False,
    )
    valid_for_endpoint: str = Column(
        String,
        nullable= False,
    )
    status: str = Column(
        String,
        nullable= False,
    )
    jwt_id: int = Column(
        BigInteger,
        nullable= False,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )

