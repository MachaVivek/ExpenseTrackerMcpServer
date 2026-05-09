uv init .

uv add fastmcp

To run the server

* uv run main.py
* fastmcp run main.py --transport http --host 0.0.0.0 --port 8000

To run inspector

* uv run fastmcp dev inspector main.py
* select the "streamble http" as transport type
* use "http://127.0.0.1:8000/mcp" as url
* click on connect
