from langgraph.graph import StateGraph, END, START
from state.agent_state import AgentState
from nodes.classifier import classifier_node
from nodes.analyzer import analyzer_node
from nodes.ticket_creator import ticket_creator_node
from nodes.validation import validation_node

def build_feedback_graph():
    workflow = StateGraph(AgentState)

    # Add Nodes
    workflow.add_node("classifier", classifier_node)
    workflow.add_node("analyzer", analyzer_node)
    workflow.add_node("validator", validation_node)
    workflow.add_node("ticket_creator", ticket_creator_node)

    # Define Edges
    workflow.add_edge(START, "classifier")
    workflow.add_edge("classifier", "analyzer")
    workflow.add_edge("analyzer", "validator")
    workflow.add_edge("validator", "ticket_creator")
    workflow.add_edge("ticket_creator", END)

    return workflow.compile()

if __name__ == "__main__":
    graph = build_feedback_graph()
    graph.get_graph().draw_mermaid_png(output_file_path="results/feedback_graph.png")
    print("Graph built successfully. Please check the file results/feedback_graph.png")
