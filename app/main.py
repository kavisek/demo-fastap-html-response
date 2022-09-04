import logging
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)

log = logging.getLogger(__name__)


app = FastAPI(title="NBA API")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"API": "Hello NBA"}

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )