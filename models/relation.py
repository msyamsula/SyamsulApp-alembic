from .base import Base
from .user import User
from .activity import Activity
from .private_message import PrivateMessage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, BIGINT


User.activities = relationship("Activity", back_populates="user")
Activity.user = relationship("User", back_populates="activities")

User.sent_message = relationship("PrivateMessage", back_populates="sender", primaryjoin="User.id == PrivateMessage.sender_id")
PrivateMessage.sender = relationship("User", back_populates="sent_message", primaryjoin="User.id == PrivateMessage.sender_id")

User.received_message = relationship("PrivateMessage", back_populates="receiver", primaryjoin="User.id == PrivateMessage.receiver_id")
PrivateMessage.receiver = relationship("User", back_populates="received_message", primaryjoin="User.id == PrivateMessage.receiver_id")


# class FollowerFollowing(Base):
#     __tablename__ = "follower_following"

#     follower_id = Column(BIGINT, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
#     following_id = Column(BIGINT, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)

# User.followers = relationship("User", back_populates="followings", secondary=FollowerFollowing)
# User.followings = relationship("User", back_populates="followers", secondary=FollowerFollowing)