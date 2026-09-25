from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# =========================
# FRONTEND
# =========================

# 1. Addition API
@app.get("/")
def add_numbers():
    return {"message :","Welcome to Web Applciation "}
    
@app.get("/calulator", response_class=HTMLResponse)
def calculator_page():

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Calculator</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #eef2f7;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .calculator {
                background-color: white;
                width: 400px;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.20);
                text-align: center;
            }

            h1 {
                color: #333;
            }

            input {
                width: 90%;
                padding: 12px;
                margin: 8px;
                font-size: 16px;
                border: 1px solid #aaa;
                border-radius: 6px;
            }

            button {
                padding: 12px 18px;
                margin: 6px;
                font-size: 16px;
                border: none;
                border-radius: 6px;
                color: white;
                cursor: pointer;
            }

            .add {
                background-color: #28a745;
            }

            .sub {
                background-color: #dc3545;
            }

            .mul {
                background-color: #007bff;
            }

            .div {
                background-color: #ff9800;
            }

            button:hover {
                opacity: 0.8;
            }

            #resultBox {
                margin-top: 20px;
                padding: 15px;
                background-color: #f4f4f4;
                border-radius: 8px;
                font-size: 20px;
                font-weight: bold;
                color: #222;
            }

            #errorMessage {
                color: red;
                margin-top: 10px;
            }
        </style>
    </head>

    <body>

        <div class="calculator">

            <h1>FastAPI Calculator</h1>

            <input
                type="number"
                id="number1"
                placeholder="Enter first number"
                step="any"
            >

            <input
                type="number"
                id="number2"
                placeholder="Enter second number"
                step="any"
            >

            <div>
                <button class="add" onclick="calculate('add')">
                    Add
                </button>

                <button class="sub" onclick="calculate('sub')">
                    Subtract
                </button>

                <button class="mul" onclick="calculate('mul')">
                    Multiply
                </button>

                <button class="div" onclick="calculate('div')">
                    Divide
                </button>
            </div>

            <div id="resultBox">
                Result will appear here
            </div>

            <div id="errorMessage"></div>

        </div>


        <script>
            async function calculate(operation) {

                // Read the values entered by the user
                const number1 =
                    document.getElementById("number1").value;

                const number2 =
                    document.getElementById("number2").value;

                const resultBox =
                    document.getElementById("resultBox");

                const errorMessage =
                    document.getElementById("errorMessage");


                // Clear the previous error message
                errorMessage.innerHTML = "";


                // Validate input fields
                if (number1 === "" || number2 === "") {
                    errorMessage.innerHTML =
                        "Please enter both numbers";

                    return;
                }


                try {
                    // Call the selected FastAPI endpoint
                    const response = await fetch(
                        `/${operation}/${number1}/${number2}`
                    );

                    // Convert the JSON response into JavaScript object
                    const data = await response.json();


                    // Check for division-by-zero message
                    if (data.message) {
                        errorMessage.innerHTML = data.message;
                        resultBox.innerHTML = "Unable to calculate";
                    } else {
                        resultBox.innerHTML =
                            `${data.operation} Result: ${data.result}`;
                    }

                } catch (error) {
                    errorMessage.innerHTML =
                        "Unable to connect to the server";
                }
            }
        </script>

    </body>
    </html>
    """


# =========================
# BACKEND APIs
# =========================

# 1. Addition API
@app.get("/add/{number1}/{number2}")
def add_numbers(number1: float, number2: float):

    result = number1 + number2

    return {
        "operation": "Addition",
        "number1": number1,
        "number2": number2,
        "result": result
    }


# 2. Subtraction API
@app.get("/sub/{number1}/{number2}")
def subtract_numbers(number1: float, number2: float):

    result = number1 - number2

    return {
        "operation": "Subtraction",
        "number1": number1,
        "number2": number2,
        "result": result
    }


# 3. Multiplication API
@app.get("/mul/{number1}/{number2}")
def multiply_numbers(number1: float, number2: float):

    result = number1 * number2

    return {
        "operation": "Multiplication",
        "number1": number1,
        "number2": number2,
        "result": result
    }


# 4. Division API
@app.get("/div/{number1}/{number2}")
def divide_numbers(number1: float, number2: float):

    if number2 == 0:
        return {
            "message": "Cannot divide a number by zero"
        }

    result = number1 / number2

    return {
        "operation": "Division",
        "number1": number1,
        "number2": number2,
        "result": result
    }