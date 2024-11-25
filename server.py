from datetime import datetime

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import uvicorn

app = FastAPI()

# app.mount("/static", StaticFiles(directory = "static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple FastAPI Site</title>
    </head>
    <body>
        <h1>This is my test website please please please work!</h1>
    </body>
    </html>
"""



# @app.get("/")
# async def hello_world():
#     print("new web request")
#     message = f"hello from disco with fastAPI!!! the datetime is {datetime.now()}"
#     return {"message": message}


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
