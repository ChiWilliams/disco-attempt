from datetime import datetime

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import uvicorn

app = FastAPI()

# app.mount("/static", StaticFiles(directory = "static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return html_content



# @app.get("/")
# async def hello_world():
#     print("new web request")
#     message = f"hello from disco with fastAPI!!! the datetime is {datetime.now()}"
#     return {"message": message}


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)
