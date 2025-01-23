from http import HTTPStatus
from typing import List

from fastapi import FastAPI

from src.schemas.users import UserInDBSchema, UserPublicSchema, UserSchema

app = FastAPI()

# HTTP_TO_CRUD_MAPPING = {
#    'POST': 'create',
#    'GET': 'read',
#    'PUT': 'update',
#    'DELETE': 'delete',
# }
db: List[UserSchema] = []


@app.get('/', status_code=HTTPStatus.OK)
def health_check():
    return {'status': 'ok'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    if user.email in [u.email for u in db]:
        raise ValueError('email already registered')
    db.append(UserInDBSchema(**user.model_dump(), id=len(db) + 1))
    print(db)
    return user


@app.get('/users/', status_code=HTTPStatus.OK)
def read_users():
    return db


@app.put('/users/', status_code=HTTPStatus.OK)
def update_users():
    return {'status': 'updated'}


@app.delete('/users/', status_code=HTTPStatus.OK)
def delete_users():
    return {'status': 'deleted'}
