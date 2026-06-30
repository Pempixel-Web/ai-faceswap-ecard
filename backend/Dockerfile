FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --no-cache-dir -r facefusion/requirements.txt

WORKDIR /app/facefusion
RUN python install.py
WORKDIR /app

CMD ["python", "runpod_handler.py"]

# FROM python:3.11-slim

# # Prevent Python from buffering output
# ENV PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     git \
#     ffmpeg \
#     libgl1 \
#     libglib2.0-0 \
#     wget \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first for better Docker caching
# COPY requirements.txt .

# # Upgrade pip
# RUN pip install --upgrade pip

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application
# COPY . .

# # Install FaceFusion requirements
# RUN pip install -r facefusion/requirements.txt

# # Install FaceFusion
# RUN cd facefusion && python install.py

# # Default command
# CMD ["python", "runpod_handler.py"]

