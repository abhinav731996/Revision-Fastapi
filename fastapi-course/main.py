# def decorator(func):
#     def wrapper():
#         func()
#     return wrapper


# @decorator
# def greet():
#     print("Hello")


# greet()


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to FastAPI"}

@app.get("/about")
def about():
    return{
        "name": "FastAPI Course",
        "level": "Beginner to Advance"
    }



