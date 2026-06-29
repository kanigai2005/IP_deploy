import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.api.auth import router as auth_router

app = FastAPI(title="AI-Assisted Product Development Support Tool")

# Get frontend URL from environment or fallback to localhost
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL,
        "http://localhost:3000",
        "http://16.16.242.152:3000",  # ADD YOUR EC2 FRONTEND HERE
    ],
    # This regex allows all Vercel preview/production domains
    allow_origin_regex="https://.*\\.vercel\\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Modular router registration
# Change prefix to "/auth" if your frontend strictly hits /auth/register
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(api_router, prefix="/api")
