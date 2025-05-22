# Basic Python Project

A simple Python project that prints "Hello World!".

## Setup

1. Create a virtual environment with Python 3.9.6:
```bash
python3.9 -m venv venv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
.\venv\Scripts\activate
```

3. Run the project:
```bash
python main.py
```

## Development: Running the FastAPI App

To start the FastAPI app in development mode, use the following command from the project root:

```
uvicorn api.endpoints:app --reload
```

- The `--reload` flag enables auto-reloading on code changes.
- By default, the app will be available at http://127.0.0.1:8000
- You can access the interactive API docs at http://127.0.0.1:8000/docs 