from .base import Base
from sqlalchemy import Column, BIGINT, String, BOOLEAN, TIMESTAMP, func, Index, text

class User(Base):
    __tablename__ = "user"

    id = Column(BIGINT, autoincrement=True, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    is_active = Column(BOOLEAN, server_default="0", nullable=False)
    status = Column(String(30), server_default="Offline", nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    __table_args__ = (
        Index("id_is_active", "id", "is_active"),
        Index("username_is_active", "username", "is_active")
    )
