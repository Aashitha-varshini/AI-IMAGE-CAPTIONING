from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import caption, quiz, audio, dashboard

app = FastAPI(title="AI Captioning Backend API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers (removed auth router)
app.include_router(caption.router)
app.include_router(quiz.router)
app.include_router(audio.router)
app.include_router(dashboard.router)

@app.get("/")
def root():
    return {"message": "AI Captioning Backend is running - No authentication required!"}
