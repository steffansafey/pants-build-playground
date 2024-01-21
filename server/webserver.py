import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """A simple endpoint to test out the webserver."""
    return {"message": "Hello World"}


def run_server():
    """Run the webserver."""
    uvicorn.run(app, host="0.0.0.0", port=8000)
