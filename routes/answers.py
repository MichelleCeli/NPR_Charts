from typing import Any
from models import Sounds, Netflilx, Haveyouever
from fastapi import APIRouter

from sheet import update_sounds, update_netflix, update_hye

router = APIRouter()

def read_item_haveyouever(item: Haveyouever):
    update_hye(item)

def read_item_sounds(item: Sounds):
    update_sounds(item)

def read_item_netflix(item: Netflilx):
    update_netflix(item)

def unrecognised_answer(type):
    print("unrecognised_answer")
    raise HTTPException(status_code=400, detail="answer type not found")
    return {}

@router.post("/answer/sounds")
def handle_generic_answer(item: Sounds):
    print('answer/sounds')
    read_item_sounds(item)
    return {"type": "sounds", "result": "success"}

@router.post("/answer/netflix")
def handle_generic_answer(item: Netflilx):
    print('answer/netflix')
    read_item_netflix(item)
    return {"type": "netflix", "result": "success"}

@router.post("/answer/haveyouever")
def handle_generic_answer(item: Haveyouever):
    print('answer/haveyouever')
    read_item_haveyouever(item)
    return {"type": "read_item_haveyouever", "result": "success"}



# @router.post("/answer/{type}")
# def handle_generic_answer(type: str, item: Any[Sounds, Netflilx, Haveyouever]):
#     switcher = {
#         'netflix': read_item_netflix,
#         'sounds': read_item_sounds,
#         'haveyouever': read_item_haveyouever,
#         'nothing': unrecognised_answer
#     }

#     func = switcher.get(type, unrecognised_answer)
#     print('answer/' + type)
#     func(item)
#     return {"type": type, "result": "success"}