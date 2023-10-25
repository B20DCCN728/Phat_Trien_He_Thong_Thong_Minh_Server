from sqlalchemy.orm import Session
import models, schemas


def get_samples(db: Session):
    return db.query(models.Sample).all()

def create_sample(db: Session, sample: schemas.SampleCreate):
    db_sample = models.Sample(**sample.dict())
    db.add(db_sample)
    db.commit()
    db.refresh(db_sample)
    return db_sample

def update_sample(db: Session, sample: schemas.Sample):
    db_sample = db.query(models.Sample).filter(models.Sample.id == sample.id).first()
    db_sample.name = sample.name
    db_sample.link_img = sample.link_img
    db_sample.link_map = sample.link_map
    db_sample.validDate = sample.validDate
    db.commit()
    db.refresh(db_sample)
    return db_sample

def get_sample(db: Session, sample_id: int):
    return db.query(models.Sample).filter(models.Sample.id == sample_id).first()


def delete_sample(db: Session, sample: models.Sample) -> bool:
    try:
        db.delete(sample)
        db.commit()
        return True
    except:
        return False

#
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
# def get_item(db: Session, item_id: int):
#     return db.query(models.Item).filter(models.Item.id == item_id).first()
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
# def get_all_items(db: Session):
#     return db.query(models.Item).all()
#
# def delete_item(db: Session, item: models.Item) -> bool:
#     try:
#         db.delete(item)
#         db.commit()
#         return True
#     except: return False
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
#
#
#
#
