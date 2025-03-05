from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def get_data():
    return {
        "name1": "Juan",
        "name2": "Maria",
        "name3": "Pedro",
        "name4": "Luisa",
        "name5": "Carlos"
    }