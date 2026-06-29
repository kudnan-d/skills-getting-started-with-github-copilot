# AGENTS instructions for this repository

Purpose
-------
Provide concise guidance for AI coding agents to be immediately productive in this repository.

Quick facts
-----------
- **Language:** Python
- **Framework:** FastAPI (app object in `src/app.py`)
- **Static files:** `src/static` mounted at `/static`
- **Tests:** standard `pytest` (see `pytest.ini`)

How to run (dev)
-----------------
1. Install dependencies:

   pip install -r requirements.txt

2. Run the dev server (recommended):

   python -m uvicorn src.app:app --reload --host 127.0.0.1 --port 8000

3. Open API docs:

   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

How to test
-----------

Run unit tests with:

```
pytest
```

Notes for agents
----------------
- The app uses an in-memory data store; state resets on restart.
- Preserve existing documentation: link to `README.md` and `src/README.md` for feature details.
- For quick local work, use the `uvicorn` command above rather than relying on `python app.py`.
- There is no database or migrations; do not attempt DB setup scaffolding.

Helpful links
-------------
- Project README: ./README.md
- API README: ./src/README.md
- Dependencies: ./requirements.txt

Suggested next customizations
----------------------------
- Create a small `skill` that runs tests and starts the dev server for quick verification.
- Add a short CI snippet (GitHub Actions) that runs `pip install -r requirements.txt` and `pytest` on push.
