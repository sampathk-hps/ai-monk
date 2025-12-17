from core.vector_search import get_results
from constants.constants import PROMPT_DIR
from core.llm import get_llm

from typing_extensions import List, TypedDict

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

class AssistantState(TypedDict):
    question: str
    context: List[Document]
    answer: str
    files: List[str]

def _retrieve_context(query: str):
    retrieved_docs = get_results(query=query)
    return retrieved_docs

def _get_prompt_message(content: str, query: str) -> str:
    prompt_template = ChatPromptTemplate.from_template(open(PROMPT_DIR).read())
    messages = prompt_template.format(context=content, question=query)
    return messages
    
def _generate_answer(state: AssistantState):
    docs_content = ""
    file_names = []
    for doc in state["context"]:
        docs_content += doc.page_content + "\n\n"
        file_names.append(doc.metadata.get("file_name"))

    messages = _get_prompt_message(docs_content, state["question"])

    response = get_llm().invoke(messages)
    file_names = list(set(file_names))
    return {"answer": response.content, "files": file_names}


if __name__ == "__main__":
    while True:
        query = input("User> ").strip()
        if not query or query.lower() in {"exit", "quit", "bye"}:
            break
        state = AssistantState(
            question=query,
            context=_retrieve_context(query)
            )
        result = _generate_answer(state)
        
        print("\nAnswer:")
        print(result["answer"])
        print("\nSource Files:")
        for file in result["files"]:
            print(file)
        print("=====================================")

