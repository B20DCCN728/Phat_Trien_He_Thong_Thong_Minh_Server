from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Label(Base):
    __tablename__ = "Label"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    validDate = Column(DateTime, index=True)
    status = Column(String)

    samples = relationship("Sample", back_populates="label")

class Sample(Base):
    __tablename__ = "Sample"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    validDate = Column(DateTime, index=True)
    link_img = Column(String)
    link_map = Column(String)
    label_id = Column(Integer, ForeignKey("Label.id"))

    label = relationship("Label", back_populates="samples")

# class User(Base):
#     __tablename__ = "Admin"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")
#
#
# class Item(Base):
#     __tablename__ = "Item"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("Admin.id"))
#
#     owner = relationship("User", back_populates="items")