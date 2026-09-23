from sqlalchemy import Column, BigInteger, String, DateTime, func

from backend.connection.v1.connection import Base

class Color(Base):
    __tablename__ = 'colors'
    color_id: int = Column(
        BigInteger,
        primary_key= True,
        nullable= False,
        autoincrement= True,
    )
    color_name: str = Column(
        String,
        nullable= False,
    )
    hex_value: str = Column(
        String,
        nullable= True,
    )
    created_at: DateTime = Column(
        DateTime(timezone= True),
        nullable= False,
        server_default= func.now(),
    )
