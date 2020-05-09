from fastapi import FastAPI
from timer import Timer

app = FastAPI()

def get_timer():
      timer = Timer()
      while True:
            yield timer

timer = get_timer()

@app.get("/timer")
def timer() -> dict:
      return {"Timer": next(timer) , "current_time": ""}