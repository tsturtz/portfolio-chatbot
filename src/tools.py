from langchain_core.tools import tool


def make_tools(retriever):
    """Creates a LangChain tools for the agent."""

    @tool
    def retrieve_documents(query: str) -> list[str]:
        """Retrieves documents about Taylor from the vector database based on a query."""
        return retriever.invoke(query)
    
    # TODO: add more tools to get more specific answers

    return [retrieve_documents]
