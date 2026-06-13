from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, func

from backend.connection.connection import Base


class Group(Base):
    __tablename__ = 'groups'
    group_id: int = Column(
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


class GroupMember(Base):
    __tablename__ = 'group_members'
    group_member_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    user_id: int = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable= False,
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
    joined_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
    left_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= True,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )