from datetime import datetime

import httpx
from fastapi import FastAPI, Body, Header, Response, HTTPException
from httpx import ConnectError
from pydantic import BaseModel, ValidationError

app = FastAPI()


class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str


class TagIn(BaseModel):
    tag: str


class TagOut(BaseModel):
    tag: str
    created: datetime


class ErrorResponse(BaseModel):
    detail: str
    status_code: int


tags = []


@app.post('/', responses={
    403: {"model": ErrorResponse},
    201: {"model": TagOut}},
    )
def create_tag(tag_in: TagIn) -> TagOut:
    try:
        tag: Tag = Tag(
            tag=tag_in.tag,
            created=datetime.now(),
            secret="shhhh",
        )
    except ValidationError as error:
        raise HTTPException(
            status_code=403,
            detail=str(error),
        )

    tags.append(tag)

    return TagOut(
        tag=tag.tag,
        created=tag.created,
    )


@app.get('/{number}', responses={
    404: {"model": ErrorResponse},
    200: {"model": TagOut}},
    )
def get_tag_by_id(number: int) -> TagOut | ErrorResponse:
    try:
        tag: Tag = tags[number]
    except IndexError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )
    return tag



@app.post('/hi')
def show_test_description(person: str = Body(embed=True)):
    return f"Test string, {person}"


@app.get("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent


@app.get("/happy/{code}")
def happy(response: Response, code: str = 'status', status_code: int = 269):
    response.status_code = status_code
    response.headers[code] = str(status_code)
    print(response.headers)
    return datetime.now().strftime('%Y_%m_%d %H:%m:%s')[:19]


def start_server():
    import uvicorn
    uvicorn.run("connection_test:app", reload=True)
    return None


def start_client():
    with httpx.Client() as client:
        while True:
            stop = input('click enter')
            if stop:
                break
            try:
                result = client.get('http://127.0.0.1:8000/hi/man')
            except ConnectError as error:
                print("ERROR", error)
            else:
                print(result)
                print('STATUS_CODE', result.status_code)
                print("HEADERS", result.headers)
                print("CONTENT", result.content)
                print("JSON", result.json())



if __name__ == "__main__":
    start_client()





