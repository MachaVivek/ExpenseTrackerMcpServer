# Expense Tracker MCP Server

A Model Context Protocol (MCP) server that enables AI assistants to securely manage personal expenses through structured tools. Built with **FastAPI**, **Python**, **Prisma ORM**, and **SQLite**, the server provides authenticated expense tracking, category management, and financial data retrieval for MCP-compatible clients.

---

## 📋 Project Overview

Expense Tracker MCP Server exposes a set of MCP tools that allow AI clients to create, update, delete, and analyze expense records through a secure API. The project combines FastAPI for backend services, Prisma for database access, and JWT authentication to provide a scalable foundation for AI-powered personal finance assistants.

---

## ✨ Key Features

### 1. MCP Tool Integration

Implements Model Context Protocol tools for seamless interaction with AI assistants.

### 2. Expense Management

Create, update, delete, and retrieve expense records with categorized transactions.

### 3. Secure Authentication

JWT-based user authentication with protected API routes and role-aware access.

### 4. Category & Financial Tracking

Organize expenses into categories and maintain structured financial records.

### 5. Prisma ORM & SQLite

Type-safe database operations using Prisma with SQLite for lightweight local development.

---

## 🛠️ Tech Stack

| **Layer**              | **Technologies**             |
| ---------------------- | ---------------------------- |
| **Backend**            | FastAPI, Python              |
| **MCP**                | Model Context Protocol (MCP) |
| **Database**           | SQLite                       |
| **ORM**                | Prisma ORM                   |
| **Authentication**     | JWT, FastAPI Security        |
| **API**                | REST API                     |
| **Package Management** | uv, pip                      |

---

## 🚀 Setup & Run

### Clone the Repository

```bash
git clone https://github.com/MachaVivek/ExpenseTrackerMcpServer.git
cd ExpenseTrackerMcpServer
```

### Create Virtual Environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Prisma Client

```bash
prisma generate
```

### Start the Server

```bash
uvicorn main:app --reload
```

### API Endpoint

```text
http://localhost:8000
```

---

## 📁 Project Structure

```text
ExpenseTrackerMcpServer/
├── app/
│   ├── auth/              # Authentication & JWT
│   ├── database/          # Prisma database client
│   ├── expenses/          # Expense management
│   ├── categories/        # Category operations
│   ├── generated/         # Generated Prisma client
│   └── mcp/              # MCP tools & server logic
├── prisma/
│   ├── schema.prisma
│   └── dev.db
├── main.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🔄 MCP Workflow

1. Client authenticates using JWT credentials.
2. MCP client invokes an expense management tool.
3. FastAPI validates the request and user.
4. Prisma performs database operations.
5. Structured expense data is returned to the AI client.

---

## 🌐 Core Capabilities

| **Operation**  | **Purpose**                    |
| -------------- | ------------------------------ |
| Create Expense | Add new financial transactions |
| Update Expense | Modify existing records        |
| Delete Expense | Remove expense entries         |
| List Expenses  | Retrieve user expenses         |
| Categories     | Organize spending by category  |
| Authentication | Secure user access             |

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL="file:./prisma/dev.db"
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🚧 Future Enhancements

* Budget planning & spending limits
* Monthly financial analytics
* Recurring expense automation
* Multi-user workspace support
* PostgreSQL production deployment

---

## 📄 License

This project is developed for educational and portfolio purposes.

---

## 👨‍💻 Author

**Vivek Macha**

GitHub: https://github.com/MachaVivek
