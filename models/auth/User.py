import hashlib
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, Date

from models.Base import Base


class User(Base):  # We extend the Base class
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    user_name = Column(String(25), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    registration_date = Column(Date(), default=datetime.now)

    def __repr__(self):
        return f"User: [{self.user_name}, {self.first_name} {self.last_name}, {self.registration_date}]"

    def __str__(self):
        return repr(self)

    def set_password(self, password: str):
        self.password = self.hash_password_text(password)

    @classmethod
    def hash_password_text(cls, password):
        return hashlib.sha224(password.encode()).hexdigest()
