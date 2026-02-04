from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

def generate(text: str) -> str:
    """
    Generate a checksum (pseudo-random token) for the given text.
    """
    return hashlib.sha256(text.encode()).hexdigest()

class TextInput(BaseModel):
    text: str

@app.post("/generate/checksum")
def generate_checksum(payload: TextInput):
    """
    Accepts input text and returns a checksum generated using the generate() function.
    """
    checksum = generate(payload.text)
    return {"checksum": checksum}

@app.get("/")
def welcome():
    return {"message": "Welcome Harshit! This API generates pseudo-random tokens."}
