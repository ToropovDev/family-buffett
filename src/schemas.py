from typing import Literal

from pydantic import BaseModel


class OK(BaseModel):
    success: Literal[True] = True
