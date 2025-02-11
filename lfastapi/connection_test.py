from datetime import datetime

import httpx
from fastapi import FastAPI, Body, Header, Response
from httpx import ConnectError
from pydantic import BaseModel

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


tags = []


@app.post('/', response_model=TagOut, status_code=201)
def create_tag(tag_in: TagIn) -> TagOut:
    tag: Tag = Tag(
        tag=tag_in.tag,
        created=datetime.now(),
        secret="shhhh",
    )

    tags.append(tag)

    return TagOut(
        tag=tag.tag,
        created=tag.created,
    )


@app.get('/{number}', response_model=TagOut, status_code=200)
def get_tag_by_id(number: int) -> TagOut | Response:
    try:
        tag = tags[number]
    except IndexError as error:
        return Response(status_code=404, content=str(error).encode())
    return TagOut(
        tag=tag.tag,
        created=tag.created
    )




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
    return datetime.datetime.now().strftime('%Y_%m_%d %H:%m:%s')[:19]


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





