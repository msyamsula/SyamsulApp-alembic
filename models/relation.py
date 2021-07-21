from .base import Base
from .user import User
from .activity import Activity
from .private_message import PrivateMessage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, BIGINT, Table


User.activities = relationship("Activity", back_populates="user")
Activity.user = relationship("User", back_populates="activities")

User.sent_message = relationship("PrivateMessage", back_populates="sender", uselist=True, primaryjoin="User.id == PrivateMessage.sender_id")
PrivateMessage.sender = relationship("User", back_populates="sent_message", uselist=False, primaryjoin="User.id == PrivateMessage.sender_id")

User.received_message = relationship("PrivateMessage", back_populates="receiver", uselist=True, primaryjoin="User.id == PrivateMessage.receiver_id")
PrivateMessage.receiver = relationship("User", back_populates="received_message", uselist=False, primaryjoin="User.id == PrivateMessage.receiver_id")


follower_following = Table('follower_following', Base.metadata,
    Column('following_id', ForeignKey('user.id'), primary_key=True),
    Column('follower_id', ForeignKey('user.id'), primary_key=True)
)

User.followers = relationship(
    "User", 
    back_populates="followings", 
    secondary=follower_following, 
    primaryjoin="User.id == follower_following.c.following_id",
    secondaryjoin="User.id == follower_following.c.follower_id"
)
User.followings = relationship(
    "User",
    back_populates="followers",
    secondary=follower_following, 
    primaryjoin="User.id == follower_following.c.follower_id",
    secondaryjoin="User.id == follower_following.c.following_id"
)