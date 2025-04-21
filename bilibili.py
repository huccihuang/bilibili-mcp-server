import os
from typing import Any

from bilibili_api import search, sync
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Bilibili mcp server")

@mcp.tool()
def general_search(keyword: str) -> dict[Any, Any]:
    """
    Search Bilibili API with the given keyword.
    
    Args:
        keyword: Search term to look for on Bilibili
        
    Returns:
        Dictionary containing the search results from Bilibili
    """
    return sync(search.search(keyword))


if __name__ == "__main__":
    mcp.run(transport='stdio')
