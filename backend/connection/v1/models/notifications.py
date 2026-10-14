from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, func, JSON, Boolean

from backend.connection.v1.connection import Base


class Notification(Base):
    __tablename__ = 'notifications'
    notification_id = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    event_id = Column(
        BigInteger,
        ForeignKey("events.event_id"),
        nullable= False,
    )
    message = Column(
        String,
        nullable= False,
    )
    destination = Column(
        JSON,
        nullable= False,
    )
    created_by = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable= False,
    )
    created_at = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )


class Invite(Base):
    __tablename__ = 'invites'
    invite_id = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    group_id = Column(
        BigInteger,
        ForeignKey("groups.group_id"),
        nullable= False,
    )
    role_id = Column(
        BigInteger,
        ForeignKey("roles.role_id"),
        nullable= False,
    )
    is_active = Column(
        Boolean,
        nullable= False,
        default= True,
    )
    invite_code = Column(
        String,
        nullable= False,
        unique= True,
    )
    max_uses = Column(
        BigInteger,
        nullable= True,
    )
    current_uses = Column(
        BigInteger,
        nullable= False,
        default= 0,
    )
    created_by = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable= False,
    )
    created_at = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
    expires_at = Column(
        DateTime(timezone= True),
        nullable= False,
    )