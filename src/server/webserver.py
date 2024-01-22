import uvicorn
from fastapi import FastAPI

from helper_library.math import add

app = FastAPI()


@app.get("/")
async def read_root():
    """A simple endpoint to test out the webserver."""

    number = add(1, 2)
    return {"message": "Hello there, World, 1 + 2 = " + str(number) + "!"}


def run_server():
    """Run the webserver."""
    uvicorn.run(app, host="0.0.0.0", port=8000)
