import datetime
import time

from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from prometheus_fastapi_instrumentator import Instrumentator, metrics
from prometheusrock import PrometheusMiddleware, metrics_route
from config import config_document

from routes import answers, questions
from typing import Union
from models import Sounds, Netflilx, Haveyouever

app = FastAPI()

origins = [
    "https://gspreadsheets-charts-logiclocks.netlify.app",
    "http://gspreadsheets-charts-logiclocks.netlify.app",
    "https://game-forms-demo.netlify.app/",
    "http://game-forms-demo.netlify.app/",
    "http://localhost",
    "http://localhost:8080",
    "http://0.0.0.0:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prometheus mw
app.add_middleware(PrometheusMiddleware)

# prometheus Instrumentator
instrumentator = Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_respect_env_var=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=[".*admin.*", "/metrics"],
    env_var_name="ENABLE_METRICS",
    inprogress_name="inprogress",
    inprogress_labels=True,
)

instrumentator.add(
    metrics.request_size(
        should_include_handler=True,
        should_include_method=False,
        should_include_status=True,
        metric_namespace="a",
        metric_subsystem="b",
    )
).add(
    metrics.response_size(
        should_include_handler=True,
        should_include_method=False,
        should_include_status=True,
        metric_namespace="namespace",
        metric_subsystem="subsystem",
    )
)

instrumentator.instrument(app).expose(app)

@app.on_event("startup")
async def startup():
    print('\n app startup')
    FastAPICache.init(InMemoryBackend())

app.add_route("/metrics", metrics_route)

@app.get("/")
def read_root():
    print(datetime.datetime.now())
    return {"Hello": "World"}

@app.get("/configs")
def read_root():
    return {"document": config_document()}

@app.get("/configs/clear-cache")
async def clear():
    return await FastAPICache.clear(namespace="gspreadsheets")

app.include_router(answers.router)
app.include_router(questions.router)