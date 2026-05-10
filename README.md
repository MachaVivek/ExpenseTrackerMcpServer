uv init .

setup folder structure

create requirements.txt file and write all are the required pacakges

uv pip install -r requirements.txt

create a neon account

create a project with the postgresql database and copy the db connection url and paste it in env

create prisma folder and inside folder create a schema.prisma file

write all the table schemas needed

uv run prisma generate -> generate prisma client

uv run prisma db push -> push schema to neon

Terminal 1: run npx @modelcontextprotocol/inspector -> you can able to see the tools in the inspector

Terminal 2: uv run uvicorn app.main:app --reload --reload-dir app --reload-exclude .venv  -> you can able to see the routes in the docs


Commit :1
