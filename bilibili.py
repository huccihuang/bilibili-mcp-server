import os
from typing import Any, Optional, Dict, List

from bilibili_api import search, sync
from bilibili_api.search import SearchObjectType, OrderUser
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

@mcp.tool()
def search_user(keyword: str, page: int = 1) -> dict[Any, Any]:
    """
    搜索哔哩哔哩用户信息。
    
    Args:
        keyword: 用户名关键词
        page: 页码，默认为1
        
    Returns:
        包含用户搜索结果的字典数据
    """
    return sync(search.search_by_type(
        keyword=keyword,
        search_type=SearchObjectType.USER,
        order_type=OrderUser.FANS,
        page=page
    ))

@mcp.tool()
def get_precise_results(keyword: str, search_type: str = "user") -> Dict[str, Any]:
    """
    获取精确的搜索结果，过滤掉不必要的信息。
    
    Args:
        keyword: 搜索关键词
        search_type: 搜索类型，默认为"user"(用户)，可选："video", "user", "live", "article"
        
    Returns:
        精简后的搜索结果，只返回完全匹配的结果
    """
    type_map = {
        "user": SearchObjectType.USER,
        "video": SearchObjectType.VIDEO,
        "live": SearchObjectType.LIVE,
        "article": SearchObjectType.ARTICLE
    }
    
    search_obj_type = type_map.get(search_type.lower(), SearchObjectType.USER)
    
    # 增加页面大小以提高匹配几率
    result = sync(search.search_by_type(
        keyword=keyword,
        search_type=search_obj_type,
        page=1,
        page_size=50
    ))
    
    # 提取关键信息，过滤掉不必要的字段
    if search_type.lower() == "user" and "result" in result:
        filtered_result = []
        exact_match_result = []
        
        for user in result.get("result", []):
            # 只保留关键信息
            filtered_user = {
                "uname": user.get("uname", ""),
                "mid": user.get("mid", 0),
                "face": user.get("upic", ""),
                "fans": user.get("fans", 0),
                "videos": user.get("videos", 0),
                "level": user.get("level", 0),
                "sign": user.get("usign", ""),
                "official": user.get("official_verify", {}).get("desc", "")
            }
            
            # 检查是否完全匹配
            if user.get("uname", "").lower() == keyword.lower():
                exact_match_result.append(filtered_user)
            else:
                filtered_result.append(filtered_user)
        
        # 如果有精确匹配结果，只返回精确匹配
        if exact_match_result:
            return {"users": exact_match_result, "exact_match": True}
        
        # 否则返回所有结果，但标记为非精确匹配
        return {"users": filtered_result, "exact_match": False}
    
    return result

if __name__ == "__main__":
    mcp.run(transport='stdio')
