from fastapi import FastAPI
app = FastAPI()
# 1. Addition API

@app.get("/hello")
def home():
    return "Home page ";

@app.get("/add/{number1}/{number2}/{n3}")
def add_numbers(number1: int, number2: int,n3:int):
    result = number1 + number2 + n3 ;

    return {
        "operation": "Addition",
        "number1": number1,
        "number2": number2,
        "n3" : n3,
        "result": result
    }
# 2. Subtraction API
@app.get("/subtract/{number1}/{number2}")
def subtract_numbers(number1: int, number2: int):
    result = number1 - number2

    return {
        "operation": "Subtraction",
        "number1": number1,
        "number2": number2,
        "result": result
    }
# 3. Multiplication API
@app.get("/multiply/{number1}/{number2}")
def multiply_numbers(number1: int, number2: int):
    result = number1 * number2

    return {
        "operation": "Multiplication",
        "number1": number1,
        "number2": number2,
        "result": result
    }