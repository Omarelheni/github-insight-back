from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str

class ProjectInfoRequest(BaseModel):
    readme: str
    name: str
    description: str
    stars: int
    forks: int
    watching: int
