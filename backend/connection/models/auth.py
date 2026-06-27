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

class Refresh_tokens(Base):
    __tablename__ = "refresh_tokens"

    refresh_token_id = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    user_id = Column(
        BigInteger,
        nullable= False,
    )
    token_hash = Column(
        String,
        nullable= False,
    )
    expire_at = Column(
        DateTime,
        nullable= False,
    )
    is_revoked = Column(
        String,
        nullable= False,
    )
    device_name = Column(
        String,
        nullable= False,
    )
    ip_address = Column(
        String,
        nullable= False,
    )
    last_used_at = Column(
        DateTime,
        nullable= False,
    )
    created_at = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
