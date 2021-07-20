from .base import Base
from sqlalchemy import Column, BIGINT, String, BOOLEAN, TIMESTAMP, func, Index, text, INTEGER, ForeignKey
from .user import User

class Activity(Base):
    __tablename__ = "activity"

    id = Column(BIGINT, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, server_default="0")
    priority = Column(INTEGER, nullable=False)
    is_crossed = Column(BOOLEAN, server_default="0", nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    user_id = Column(BIGINT, ForeignKey("user.id"))

    __table_args__ = (
        Index("name", "name"),
        Index("priority", "priority"),
        Index("user_id_name", "user_id", "name")
    )
