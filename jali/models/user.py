from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, DateTime, String, func
from jali.db import Base


class User(Base):
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    username: str = Column(String, nullable=True)

    # Debug time
    created_at: datetime = Column(DateTime,
                                  server_default=func.now(),
                                  nullable=False)
    updated_at: datetime = Column(DateTime,
                                  server_default=func.now(),
                                  onupdate=func.now(),
                                  nullable=False)

    # Permanent settings
    admin: bool = Column(Boolean, nullable=False, default=False)

    # Data
    update_count = Column(Integer)

    def __init__(self, user_id: int, name: str, data=None, admin=False):
        self.id = user_id
        self.name = name
        self.admin = admin
        self.update_count = 0

    def __repr__(self):
        """Print as string."""
        return f"User with Id: {self.id}, name: {self.name}"

    def delete(self):
        """Delete the user."""
        self.started = False
        self.username = "GDPR removed user"
        self.name = "GDPR removed user"
        self.locale = "English"
        self.european_date_format = False
        self.notifications_enabled = False
