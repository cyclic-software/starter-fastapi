import uvicorn
from app import app

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8181)
    uvicorn.run(app, host="127.0.0.1", port=8000)


