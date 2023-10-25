import shutil

from fastapi import Depends, FastAPI, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import models, schemas
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",  # Add the origin of your frontend application
    # You can add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
# @app.delete("/users/{user_id}/items/{item_id}")
# def delete_item(
#     item_id: int, db: Session = Depends(get_db)
# ):
#     item = crud.get_item(db, item_id)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Product not found")
#     if crud.delete_item(db, item) == False:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return {"message", "Item deleted"}
#
#
#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
#
# @app.get("/items/all", response_model=list[schemas.Item])
# def read_items(db: Session = Depends(get_db)):
#     items = crud.get_all_items(db)
#     return items
#
# @app.get("/items/all", response_model=list[schemas.Item])
# def read_items(db: Session = Depends(get_db)):
#     items = crud.get_all_items(db)
#     return items

@app.get("/sample/all", response_model=list[schemas.Sample])
def read_samples(db: Session = Depends(get_db)):
    samples = crud.get_samples(db)
    print(samples)
    return samples



@app.delete("/sample/{sample_id}")
def delete_sample(
        sample_id: int, db: Session = Depends(get_db)
):
    sample = crud.get_sample(db, sample_id)
    if sample is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if crud.delete_sample(db, sample) == False:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message", "Sample deleted"}


@app.post("/upload")
# File đại diện cho tham số file trong form-data
async def upload_file(file: UploadFile = File(...)):
    with open(f'hand/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}


@app.put("/sample/{sample_id}", response_model=schemas.Sample)
async def update_sample(sample_id: int, sample: schemas.Sample, db: Session = Depends(get_db)):
    update = crud.update_sample(db, sample)
    return update