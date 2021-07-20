from .base import Base
from .user import User
from .activity import Activity
from sqlalchemy.orm import relationship


User.activities = relationship("Activity", back_populates="user")
Activity.user = relationship("User", back_populates="activities")