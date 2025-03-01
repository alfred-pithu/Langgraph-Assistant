"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg
from typing_extensions import Annotated

from react_agent.supabase import search_dresses


async def search_tool(
    user_query: Annotated[str, "user_query"],
) -> Optional[list[dict[str, Any]]]:
    """This functions searches for dresses using rag-based search on the basis of the user query.
    """
    result = await search_dresses(user_query)
    print("RESULT", result)
    return f"Search results for '{user_query}': {result}"   

TOOLS: List[Callable[..., Any]] = [search_tool]
