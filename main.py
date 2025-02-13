from fastapi import FastAPI
from pymongo import MongoClient
from routers import auth, posts, comments, search
import os

# App setup
app = FastAPI()
MONGO_URI = os.getenv("MONGO_URI")

# MongoDB Connection
client = MongoClient(MONGO_URI)
db = client.writers_platform

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(comments.router, prefix="/comments", tags=["Comments"])
app.include_router(search.router, prefix="/search", tags=["Search"])

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




