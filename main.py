from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/test")
def read_test():
    return {"message": "Hello Raspberry Pi"}
