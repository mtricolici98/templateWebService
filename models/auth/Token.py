from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.Base import Base


class Token(Base):
    __tablename__ = 'auth_token'

    token = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("User", backref="tokens")
