from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("access!!")
    return {"message": "Hello, FastAPI"}

@app.get("/health")
def return_status():
    return {"message": "It works!"}

