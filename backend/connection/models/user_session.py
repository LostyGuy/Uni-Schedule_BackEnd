from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, func, JSON

from backend.connection.connection import Base


class UserSession(Base):
    __tablename__ = 'user_session'
    user_session_id: int = Column(
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
    ip_address: str = Column(
        String,
        nullable= False,
    )
    device_info: JSON = Column(
        JSON,
        nullable= True,
    )
    logged_in_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
    )
    logged_out_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= True,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
