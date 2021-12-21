from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter

from fastapi_cache.decorator import cache
from fastapi_cache.coder import JsonCoder

from sheet import get_questions

router = APIRouter()

@router.post("/questions/{type}")
@cache(namespace="gspreadsheets", expire=300, coder=JsonCoder)
async def read_item(type: str):
    print('questions/', type)
    questions = get_questions(type)
    json_compatible_item_data = jsonable_encoder({"items": questions, "result": "success"})
    return json_compatible_item_data
    #JSONResponse(content=json_compatible_item_data)
