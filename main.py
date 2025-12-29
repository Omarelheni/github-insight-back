from fastapi import FastAPI
from utils import build_prompt,build_prompt_info
from models import AskRequest, ProjectInfoRequest
from call import call_llm
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^chrome-extension://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ask")
async def ask_question(request: AskRequest):
    prompt = build_prompt(request)
    answer = await call_llm(prompt)
    return {"answer": answer}


@app.post("/project-info")
async def project_info(request: ProjectInfoRequest):
    print(request)
    prompt = build_prompt_info(request)
    answer = await call_llm(prompt)
    return answer


