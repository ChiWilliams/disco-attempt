from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    print("new web request")
    message = f"hello from disco!!! the datetime is {datetime.now()}"
    return {"message": message}


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)
