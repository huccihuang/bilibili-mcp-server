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

目前仅支持搜索视频，未来预计添加更多操作。

## 如何为本项目做贡献

1. Fork 本项目
2. 新建分支，并在新的分支上做改动
3. 提交 PR

## License

MIT
