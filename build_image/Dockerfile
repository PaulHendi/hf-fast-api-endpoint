# Use an NVIDIA base image with CUDA support
FROM nvidia/cuda:12.1.0-base-ubuntu22.04


# Install Python and pip
RUN apt-get update && apt-get install -y python3-pip


# Set the working directory in the container
WORKDIR /app


# Copy only the requirements file first (for caching optimization)
COPY requirements.txt /app

# Set the environment variable for Hugging Face cache
# Note : the dir is set so that weights are saved to a volume (check launch_training.sh)
# This is to ensure that the weights are not lost when the container is stopped
ENV HF_HOME=/volume/.cache/huggingface


# Install Hugging Face libraries
RUN pip3 install --no-cache-dir -r requirements.txt

# Install additional libraries for inference
RUN pip3 install --no-cache-dir pydantic fastapi "uvicorn[standard]"


# (Optional) Copy project files
COPY . /app

# Launch the FastAPI server
CMD ["uvicorn", "test_endpoint:app", "--host", "0.0.0.0", "--port", "80"]