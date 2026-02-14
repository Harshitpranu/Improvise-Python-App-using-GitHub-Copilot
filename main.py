from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model to accept JSON body
class TextRequest(BaseModel):
    text: str

@app.get("/")
def welcome():
    """
    Welcome API with participant name
    """
    return {
        "message": "Welcome to Token Generator API!",
        "participant": "Harshit Srivastava",
        "organization": "Accenture"
    }

@app.post("/generate-checksum")
def generate_checksum(payload: TextRequest):
    """
    This API accepts text in JSON body and returns checksum of the text
    """
    text = payload.text
    checksum = hashlib.sha256(text.encode()).hexdigest()

    return {
        "input_text": text,
        "checksum": checksum
    }

