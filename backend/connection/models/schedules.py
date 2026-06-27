from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, Text, func, Boolean

from backend.connection.connection import Base


class Schedule(Base):
    __tablename__ = 'schedules'
    schedule_id: int = Column(
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
    status: str = Column(
        String,
        nullable= False,
    )
    group_id: int = Column(
        BigInteger,
        ForeignKey("groups.group_id"),
        nullable= True,
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
    updated_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= True,
    )


class Event(Base):
    __tablename__ = 'events'
    event_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    schedule_id: int = Column(
        BigInteger,
        ForeignKey("schedules.schedule_id"),
        nullable= False,
    )
    title: str = Column(
        String,
        nullable= False,
    )
    description: str = Column(
        Text,
        nullable= True,
    )
    start_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
    )
    end_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
    )
    color_id: int = Column(
        BigInteger,
        ForeignKey("colors.color_id"),
        nullable= False,
    )
    is_repeating: bool = Column(
        Boolean,
        nullable= False,
        default= False,
    )
    repeat_pattern: str = Column(
        String,
        nullable= True,
    )
    status: str = Column(
        String,
        nullable= False,
        default= 'active',
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
    updated_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= True,
    )