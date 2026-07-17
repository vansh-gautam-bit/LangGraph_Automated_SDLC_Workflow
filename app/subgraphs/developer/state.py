from typing import TypedDict

class DeveloperState(TypedDict):
    project_name:str
    user_requirements: str

    product_owner_artifact: str
    architecture_artifact: str

    folder_structure: str

    models: str

    schemas: str

    routers: str
    
    services: str

    readme: str

    generated_files: dict[str, str]

    history: list[str]