# Minecraft Server Ops Generator
Minecraft Server Ops Generator is a Python-based tool designed to simplify the process of managing operator permissions for your Minecraft server. With this app, you can easily generate and manage the `ops.json` file, ensuring your server operators have the correct permissions.

## Features

- **User-Friendly Interface**: Easily add operators.
- **Permission Levels**: Assign specific permission levels to operators.
- **JSON Export**: Generate a valid `ops.json` file for your server.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Rapter001/minecraft-server-ops.json-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd minecraft-server-ops-generator
    ```
3. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```
2. Follow the on-screen instructions to manage your server operators.
3. Export the `ops.json` file and place it in your Minecraft server directory.

## Deploy via Docker

You can either build the Docker image locally or pull it directly from Docker Hub.

### Option 1: Build Locally
1. Build the Docker image:
    ```bash
    docker build -t minecraft-server-ops-generator .
    ```
2. Run the Docker container:
    ```bash
    docker run -d -p 5000:5000 --name minecraft-server-ops-generator --restart=on-failure rapter001/minecraft-server-ops-generator:latest
    ```

3. Follow the on-screen instructions inside the container to manage your server operators.

### Option 2: Pull from Docker Hub

1. Pull the pre-built Docker image:
    ```bash
    docker pull rapter001/minecraft-server-ops-generator:latest
    ```
2. Run the Docker container:
    ```bash
    docker run -d -p 5000:5000 --name minecraft-server-ops-generator --restart=on-failure rapter001/minecraft-server-ops-generator:latest
    ```

3. Follow the on-screen instructions inside the container to manage your server operators.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## Contact

For questions or feedback, feel free to open an issue or contact the project maintainer.

[rapter.pages.dev/links](https://rapter.pages.dev/links)
