from pydantic import BaseModel


class S04E04_AI_DEVS_INPUT(BaseModel):
    instruction: str

class S04E04_AI_DEVS_OUTPUT(BaseModel):
    description: str