from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import StreamingResponse, JSONResponse
from datetime import datetime
import os, json
from minivaultapi.api.prompt_handler import router as prompt_router

app = FastAPI()

LOG_FILE = "logs/log.jsonl"

app.include_router(prompt_router, tags=["prompt"])