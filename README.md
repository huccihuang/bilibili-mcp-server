# Bilibili API MCP Server

用于哔哩哔哩 API 的 MCP（模型上下文协议）服务器，支持多种操作。

## 环境要求

- [uv](https://docs.astral.sh/uv/) - 一个项目管理工具，可以很方便管理依赖。

## 使用方法

1. clone 本项目

2. 使用 uv 安装依赖

```bash
uv sync
```

3. 在任意 mcp client 中配置本 Server

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "uv",
      "args": [
        "--directory",
        "/your-project-path/bilibili-mcp-server",
        "run",
        "bilibili.py"
      ]
    }
  }
}
```

4. 在 client 中使用

## 支持的操作

支持以下操作：

1. `general_search`: 基础搜索功能，使用关键词在哔哩哔哩进行搜索。
2. `search_user`: 专门用于搜索哔哩哔哩用户的功能，可以按照粉丝数排序。
3. `get_precise_results`: 精确搜索功能，可以过滤掉不必要的信息，支持多种搜索类型：
   - 用户搜索 (`user`)：精确匹配用户名，只返回完全匹配的结果。例如搜索"双雷"只会返回用户名为"双雷"的账号信息，不会返回其他相关用户
   - 视频搜索 (`video`)
   - 直播搜索 (`live`)
   - 专栏搜索 (`article`)
返回结果包含 `exact_match` 字段，标识是否找到精确匹配的结果。
4. `get_video_danmaku·`: 获取视频弹幕信息。

## 如何为本项目做贡献

1. Fork 本项目
2. 新建分支，并在新的分支上做改动
3. 提交 PR

## License

MIT
