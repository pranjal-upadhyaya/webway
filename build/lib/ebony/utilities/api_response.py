from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any


class Response(BaseModel):
    data: Any
    message: str


class APIResponse(JSONResponse):
    data: Any
    message: str
    status_code: int

    def __init__(
        self, 
        data: Any, 
        message: str, 
        status_code: int
    ):
        self.data = data
        self.message = message
        self.status_code = status_code
        super().__init__(
            content=Response(data=data, message=message).model_dump(),
            status_code=self.status_code,
        )
