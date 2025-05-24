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

## Production: Building and Running the FastAPI App

To run the FastAPI app in production mode, use the following command from the project root:

```
uvicorn api.endpoints:app --host 0.0.0.0 --port 8000
```

- This will start the app on all network interfaces at port 8000.
- The `--reload` flag is omitted for production for better performance and security.
- You can use a process manager like `systemd`, `supervisor`, or `pm2` to keep the server running in production.

### Example: Using gunicorn with uvicorn workers

For advanced production deployments, you can use Gunicorn with Uvicorn workers:

```
gunicorn -k uvicorn.workers.UvicornWorker api.endpoints:app --bind 0.0.0.0:8000
```

This is optional, but recommended for robust production environments.

## Docker

To build and run your container:
```sh
docker build -t my-fastapi-app .; 
docker run -p 8000:8000 my-fastapi-app;
``` 