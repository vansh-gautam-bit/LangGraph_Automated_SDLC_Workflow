from langgraph.graph import START, END, StateGraph

from app.subgraphs.developer.state import DeveloperState

from app.subgraphs.developer.nodes.folder_generator import(
    folder_generator_node,
)

from app.subgraphs.developer.nodes.model_generator import(
    model_generator_node,
)

from app.subgraphs.developer.nodes.schema_generator import(
    schema_generator_node,
)

from app.subgraphs.developer.nodes.router_generator import(
    router_generator_node,
)

from app.subgraphs.developer.nodes.service_generator import(
    service_generator_node,
)

from app.subgraphs.developer.nodes.readme_generator import(
    readme_generator_node,
)

builder = StateGraph(DeveloperState)

builder.add_node(
    "folder_generator",
    folder_generator_node,
)

builder.add_node(
    "model_generator",
    model_generator_node,
)

builder.add_node(
    "schema_generator",
    schema_generator_node,
)

builder.add_node(
    "router_generator",
    router_generator_node,
)

builder.add_node(
    "service_generator",
    service_generator_node,
)

builder.add_node(
    "readme_generator",
    readme_generator_node,
)

builder.add_edge(START,"folder_generator")
builder.add_edge("folder_generator", "model_generator")
builder.add_edge("model_generator", "schema_generator")
builder.add_edge("schema_generator", "router_generator")
builder.add_edge("router_generator", "service_generator")
builder.add_edge("service_generator", "readme_generator")
builder.add_edge("readme_generator", END)

developer_graph = builder.compile()