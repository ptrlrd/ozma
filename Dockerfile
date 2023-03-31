# Use a minimal Linux distribution with Python 3.10 installed
FROM python:3.10-alpine

# Set environment variables for the GitHub credentials and private token
ARG GH_USERNAME
ARG GH_ACCESS_TOKEN
ARG GH_REPO
ARG token

# Update packages and install necessary tools
RUN apk update && \
    apk add --no-cache git

# Clone the private GitHub repository
RUN git clone https://${GH_USERNAME}:${GH_ACCESS_TOKEN}@github.com/${GH_USERNAME}/${GH_REPO}.git /app

# Set the working directory
WORKDIR /app

# Create the .env file with the private token
RUN echo "token=\"${token}\"" > .env

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "main.py"]
