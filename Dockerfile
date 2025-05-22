# ---- Build Stage ----
FROM python:3.9-slim AS build

# Set work directory
WORKDIR /app

# Install build dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

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