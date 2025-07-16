from pydantic import BaseModel, Field

class PromptModel__Out(BaseModel):
    response: str = Field()

class PromptModel__In(BaseModel):
    prompt: str = Field()