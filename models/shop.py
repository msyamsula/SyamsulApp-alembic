from .base import Base
from sqlalchemy import Column, BIGINT, String, BOOLEAN, TIMESTAMP, func, Index, text, INTEGER, ForeignKey
from .user import User

class Shop(Base):
    __tablename__ = "shop"

    id = Column(BIGINT, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    owner_id = Column(BIGINT, ForeignKey("user.id", ondelete="CASCADE", name="shop_owner_fk"), nullable=False) 
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    __table_args__ = ()
