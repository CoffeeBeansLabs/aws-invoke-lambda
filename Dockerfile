# Set the base image to use for subsequent instructions
FROM alpine:3.12.3-slim

# Update software packages
RUN apt-get update
RUN pip install --upgrade pip

# Copy requirements.txt and install
COPY requirements.txt .
RUN pip install -r requirements.txt


# Set the working directory inside the container
WORKDIR /usr/src

# Copy any source file(s) required for the action
COPY ./src/ .

# Configure the container to be run as an executable
ENTRYPOINT ["python", "/usr/src/aws.py"]
