from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str

class ProjectInfoRequest(BaseModel):
    readme: str
    name: str
    description: str
    stars: str
    forks: str
    watching: str

class FileExplinationRequest(BaseModel):
    filename: str
    content: str