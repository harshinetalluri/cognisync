# CogniSync

**The AI-Driven Peer Learning Mesh**

CogniSync is an adaptive assignment system that uses Generative AI to create dynamic questions and a Graph Database to foster peer-to-peer learning.

## Tech Stack
*   **Backend**: FastAPI, Python 3.11, PostgreSQL
*   **Frontend**: Next.js 14, Tailwind CSS, TypeScript
*   **AI**: Google Gemini Pro
*   **Database**: Neo4j (Graph), PostgreSQL (Relational)

## Directory Structure
*   `backend/`: FastAPI application
*   `frontend/`: Next.js web application
*   `database/`: Scripts for DB initialization (if any)

## Getting Started

### Prerequisites
*   Docker & Docker Compose
*   Node.js 18+ (for local frontend dev)
*   Python 3.11+ (for local backend dev)

### Run with Docker (Recommended)
1.  Create a `.env` file in `backend/` (see `backend/.env.example` - to be created).
2.  Run:
    ```bash
    docker-compose up --build
    ```
3.  Access:
    *   Frontend: http://localhost:3000
    *   Backend Docs: http://localhost:8000/docs
    *   Neo4j Browser: http://localhost:7474

## Project Phase
Currently in Phase 1: Core Foundation Setup.
