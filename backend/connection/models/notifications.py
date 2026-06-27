from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, func, JSON, Boolean

from backend.connection.connection import Base


class Notification(Base):
    __tablename__ = 'notifications'
    notification_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    event_id: int = Column(
        BigInteger,
        ForeignKey("events.event_id"),
        nullable= False,
    )
    message: str = Column(
        String,
        nullable= False,
    )
    destination: JSON = Column(
        JSON,
        nullable= False,
    )
    created_by: int = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable= False,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )


class Invite(Base):
    __tablename__ = 'invites'
    invite_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    group_id: int = Column(
        BigInteger,
        ForeignKey("groups.group_id"),
        nullable= False,
    )
    role_id: int = Column(
        BigInteger,
        ForeignKey("roles.role_id"),
        nullable= False,
    )
    is_active: bool = Column(
        Boolean,
        nullable= False,
        default= True,
    )
    invite_code: str = Column(
        String,
        nullable= False,
        unique= True,
    )
    max_uses: int = Column(
        BigInteger,
        nullable= True,
    )
    current_uses: int = Column(
        BigInteger,
        nullable= False,
        default= 0,
    )
    created_by: int = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable= False,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
    expires_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
    )