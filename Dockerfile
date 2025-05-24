# ---- Build Stage ----
FROM python:3.9-slim AS build

# Set work directory
WORKDIR /app

# Install build dependencies
COPY requirements.txt ./

# Check this out for how to build gpt4all in docker
# https://www.runpod.io/articles/guides/deploying-gpt4all-cloud-docker-minimal-api

# Upgrade pip and install all requirements, including gpt4all, into /install
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt && \
    pip install --prefix=/install gpt4all

# Install system build tools for native library
RUN apt-get update && apt-get install -y build-essential cmake

# Build the native library for gpt4all
RUN cd /usr/local/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY && make

# Copy the rest of the application code
COPY . .

# ---- Runtime Stage ----
FROM python:3.9-slim AS runtime

WORKDIR /app

# Copy installed dependencies from build stage
COPY --from=build /install /usr/local

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "api.endpoints:app", "--host", "0.0.0.0", "--port", "8000"] 