from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from reviewer import analyze_code

app = FastAPI(
    title="Code Review Assistant",
    description="AI-powered Python code review using Claude",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

class ReviewResponse(BaseModel):
    bugs: list
    security: list
    quality: list
    suggestions: list

@app.get("/")
def root():
    return {"message": "Code Review Assistant API is running"}

@app.post("/review", response_model=ReviewResponse)
def review_code(request: CodeRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="No code provided")
    
    if len(request.code) > 10000:
        raise HTTPException(status_code=400, detail="Code too long. Maximum 10000 characters.")
    
    result = analyze_code(request.code)
    return result