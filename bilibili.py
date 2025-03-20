from mcp.server.fastmcp import FastMCP
import requests
from typing import Any

mcp = FastMCP("Bilibili mcp server")


@mcp.tool()
def bilibili_search(keyword: str, session_data: str|None = None) -> dict[Any, Any]:
    """
    Search Bilibili API with the given keyword.
    
    Args:
        keyword: Search term to look for on Bilibili
        session_data: Optional SESSDATA cookie value for authenticated requests
        
    Returns:
        Dictionary containing the search results from Bilibili
    """
    url = "https://api.bilibili.com/x/web-interface/search/all/v2"
    
    # Set up parameters
    params = {
        "keyword": keyword
    }
    
    # Set up cookies if session_data is provided
    cookies = {}
    if session_data:
        cookies["SESSDATA"] = session_data
    
    # Make the request
    response = requests.get(url, params=params, cookies=cookies)
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Return the JSON response
    return response.json()


if __name__ == "__main__":
    mcp.run()
