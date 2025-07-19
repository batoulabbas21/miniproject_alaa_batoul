# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements file first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and configure pip to use fast mirror
RUN pip install --upgrade pip && \
    pip config set global.index-url https://pypi.org/simple

# Install all packages except spacy without dependencies
RUN pip install --prefer-binary --no-cache-dir --progress-bar off --timeout 300 --retries 20 --no-deps --break-system-packages -r requirements.txt

# Install spacy separately with full dependencies
RUN pip install --prefer-binary --no-cache-dir --progress-bar off --timeout 300 --retries 20 --break-system-packages spacy==3.8.7

# Copy the rest of the application code
COPY . .

# Run your app using uvicorn (adjust the module path if needed)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8100"]
