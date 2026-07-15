from langgraph.graph import StateGraph, START, END

from app.state import SDLCState
from app.nodes.product_owner import product_owner_node
from app.nodes.architect import architect_node
from app.nodes.developer import developer_node

builder = StateGraph(SDLCState)

builder.add_node(
    "product_owner",
    product_owner_node
)

builder.add_node(
    "architect",
    architect_node
)

builder.add_node(
    "developer",
    developer_node
)

builder.add_edge(
    START,
    "product_owner"
)

builder.add_edge(
    "product_owner",
    "architect"
)

builder.add_edge(
    "architect",
    "developer"
)

builder.add_edge(
    "developer",
    END
)

graph = builder.compile()