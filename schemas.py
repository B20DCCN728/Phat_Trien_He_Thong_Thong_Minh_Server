import datetime
from typing import Union
from datetime import datetime

from pydantic import BaseModel


class LabelBase(BaseModel):
    name: str
    validDate: datetime
    status: Union[str, None] = None



class SampleBase(BaseModel):
    name: str
    validDate: datetime
    link_img: str
    link_map: str



class SampleCreate(SampleBase):
    pass


class Sample(SampleBase):
    id: int
    # label_id: int
    label: LabelBase

    class Config:
        orm_mode = True

class Label(LabelBase):
    id: int
    samples: list[Sample] = []

    class Config:
        orm_mode = True

#
# class ItemBase(BaseModel):
#     title: str
#     description: Union[str, None] = None
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
#
#
# class UserBase(BaseModel):
#     email: str
#
#
# class UserCreate(UserBase):
#     password: str
#
#
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []
#
#     class Config:
#         orm_mode = True
