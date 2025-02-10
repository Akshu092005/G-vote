from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, FileResponse
import mysql.connector

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Database Connection Function
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Kshu0903",
        database="login_data"
    )

# Login Route
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    
    # Check if the user exists in the database
    cursor.execute("SELECT * FROM student_details WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user and password == user["password"]:  # Ideally, use bcrypt for security
        return RedirectResponse("/static/Dashboard-gvote.html", status_code=303)  # Serve the Dashboard page
    else:
       return {"error": "Invalid username or password"}

# Serve the Dashboard HTML Page
@app.get("/dashboard")
def dashboard():
    return RedirectResponse("/static/Dashboard-gvote.html")  # Return the Dashboard page
