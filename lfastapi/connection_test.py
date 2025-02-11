import asyncio
from multiprocessing import Process
from threading import Thread

import httpx
from fastapi import FastAPI
from httpx import Response, ConnectError

app = FastAPI()


@app.get('/hi')
def show_test_description():
    return "Test string"


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
                result = client.get('http://127.0.0.1:8000/hi')
            except ConnectError as error:
                print("ERROR", error)
            else:
                print(result.status_code)
                print("CONTENT", result.content)
                print("JSON", result.json())



if __name__ == "__main__":
    start_client()





