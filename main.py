from fastapi import FastAPI
from utils import build_prompt,build_prompt_info
from models import AskRequest, ProjectInfoRequest
from call import call_llm
from starlette.middleware.cors import CORSMiddleware
from models import FileExplinationRequest

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
    prompt = build_prompt_info(request)
    answer = await call_llm(prompt)
    print(" Answer:", answer)
    return answer

@app.post("/explain-file")
async def explain_file(request: FileExplinationRequest):
    prompt = f"Explain the following code file named {request.filename}:\n\n{request.content}"
    answer = await call_llm(prompt)
    return answer
