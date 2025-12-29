from models import AskRequest, ProjectInfoRequest
def build_prompt(request: AskRequest) -> str:
    return request.question

def build_prompt_info(request: ProjectInfoRequest) -> str:
    prompt = f"""You are provided with the following GitHub project details:
            Name: {request.name}
            Description: {request.description}
            README Content: {request.readme}
            Stars: {request.stars}
            Forks: {request.forks}
            Watching: {request.watching} 
            Analyze the project and provide a concise summary focusing on its purpose, key features, and potential use cases.
            """
    return prompt

