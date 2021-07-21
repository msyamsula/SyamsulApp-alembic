from .base import Base
from sqlalchemy import Column, BIGINT, String, BOOLEAN, TIMESTAMP, func, Index, text as sa_text, ForeignKey

class PrivateMessage(Base):
    __tablename__ = "private_message"

    id = Column(BIGINT, autoincrement=True, primary_key=True)
    sender_id = Column(BIGINT, ForeignKey("user.id", name="sender_fk"), nullable=False)
    receiver_id = Column(BIGINT, ForeignKey("user.id", name="receiver_fk"), nullable=False)
    text = Column(String(1000), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=sa_text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    __table_args__ = ()
