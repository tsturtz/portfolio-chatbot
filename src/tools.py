from langchain_core.tools import tool

def make_retriever_tool(retriever):
    @tool
    def retrieve_documents(query: str) -> list[str]:
        """Retrieves documents about Taylor from the vector database based on a query."""
        return retriever.invoke(query)
    return retrieve_documents
