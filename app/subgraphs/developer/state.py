from typing import TypedDict

class DeveloperState(TypedDict):
    architecture: str

    folder_structure: str

    model: str

    schemas: str
    
    services: str

    readme: str

    generated_files: dict[str, str]

    history: list[str]