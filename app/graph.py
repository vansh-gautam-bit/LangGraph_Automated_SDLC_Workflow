from langgraph.graph import StateGraph, START, END

from app.state import SDLCState
from app.nodes.product_owner import product_owner_node

from app.nodes.architect import architect_node
from app.nodes.developer import developer_node
from app.nodes.reviewer import reviewer_node
from app.nodes.security import security_node
from app.nodes.testing import testing_node
from app.nodes.qa import qa_node
from app.nodes.deployment import deployment_node

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

builder.add_node(
    "reviewer",
    reviewer_node
)

builder.add_node(
    "security",
    security_node
)

builder.add_node(
    "testing",
    testing_node
)

builder.add_node(
    "qa",
    qa_node,
)

builder.add_node(
    "deployment",
    deployment_node
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
    "reviewer"
)

builder.add_edge(
    "reviewer",
    "security"
)

builder.add_edge(
    "security",
    "testing"
)

builder.add_edge(
    "testing",
    "qa"
)

builder.add_edge(
    "qa",
    "deployment"
)

builder.add_edge(
    "deployment",
    END
)

graph = builder.compile()