# Use a python base image
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set the working directory
WORKDIR /app

# Copy dependency files first to leverage Docker caching
COPY pyproject.toml uv.lock ./

# Install dependencies
# --system: Installs into the system python (avoids creating a venv inside Docker, which is simpler)
# --deploy: Enforces that uv.lock is up to date
RUN uv sync --frozen --no-cache

# Copy the rest of your application code
COPY . .

# Add src to Python path
ENV PYTHONPATH=/app/src:/app

# Hugging Face Spaces expects your app to run on port 7860
# This is a HARD requirement
ENV PORT=7860
EXPOSE 7860

# Command to run the application
# Ensure host is 0.0.0.0 so external traffic can reach it
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]