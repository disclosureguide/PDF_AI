# ---- Build Stage ----
FROM python:3.9-slim AS build
# FROM ubuntu/python:3.10-slim
# Set work directory
# WORKDIR /

# Install build dependencies
COPY . .

# Check this out for how to build gpt4all in docker
# https://www.runpod.io/articles/guides/deploying-gpt4all-cloud-docker-minimal-api


# Upgrade pip and install all requirements, including gpt4all, into /install
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "api.endpoints:app", "--host", "0.0.0.0", "--port", "8000"] 

# ---- Runtime Stage ----
# FROM python:3.9-slim AS runtime

# # Copy application code
# COPY . .

# # Expose port
# EXPOSE 8000

# # Command to run the app
# CMD ["uvicorn", "api.endpoints:app", "--host", "0.0.0.0", "--port", "8000"] 