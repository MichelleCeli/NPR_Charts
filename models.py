from pydantic import BaseModel, Field
from typing import Optional

class Sounds(BaseModel):
    team: str
    sound1: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    sound2: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    sound3: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    sound4: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    sound5: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    sound6: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )

class Netflilx(BaseModel):
    team: str
    order: list = []

class Haveyouever(BaseModel):
    answers: list = []