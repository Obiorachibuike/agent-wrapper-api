Here’s your updated and visually enhanced `README.md` file for the **Agent Wrapper API**, now including emojis for better readability and engagement:

---

# 🤖 Agent Wrapper API

A simple and scalable API built with **FastAPI** to create AI agents using either [🔊 VAPI](https://vapi.ai/) or [🧠 Retell AI](https://www.retellai.com/). This API receives agent configuration data and routes it to the chosen provider.

---

## 📚 Table of Contents

- [🚀 Requirements](#-requirements)
- [🛠 Installation](#-installation)
- [🔐 Environment Variables](#-environment-variables)
- [🚦 Running the Server](#-running-the-server)
- [📬 API Usage](#-api-usage)
- [📁 Project Structure](#-project-structure)
- [🧪 Testing](#-testing)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🚀 Requirements

✅ Python 3.8+  
✅ `pip` for dependency management

---

## 🛠 Installation

### 1. 📥 Clone the Repository

```bash
git clone <your-repository-url>
cd agent-wrapper-api
```

### 2. 🧰 Set Up Virtual Environment

```bash
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add the following:

```env
VAPI_API_TOKEN=your_vapi_token_here
RETELL_API_KEY=your_retell_api_key_here
```

These are your secret API keys—keep them safe! 🛡️

---

## 🚦 Running the Server

Start the development server using:

```bash
uvicorn app.main:app --reload
```

🌐 Visit your API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

You can also explore the Swagger docs here: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📬 API Usage

### 📌 `POST /create-agent`

Create an AI agent with either VAPI or Retell.

#### 📝 Request Body

```json
{
  "name": "MyAgent",
  "description": "An AI agent for demonstration.",
  "voice": "echo",
  "provider": "vapi"
}
```

#### 🧪 Example cURL Request

```bash
curl -X POST 'http://127.0.0.1:8000/create-agent' \
-H 'Content-Type: application/json' \
-d '{
  "name": "MyAgent",
  "description": "An AI agent for demonstration.",
  "voice": "echo",
  "provider": "vapi"
}'
```

#### ✅ Sample Response

```json
{
  "id": "some-agent-id",
  "name": "MyAgent",
  "description": "An AI agent for demonstration.",
  "voice": "echo"
}
```

---

## 📁 Project Structure

```
agent-wrapper-api/
├── app/
│   └── main.py               # FastAPI app entry point
├── models/
│   └── agent.py              # Pydantic model for agent creation
├── services/
│   ├── vapi_service.py       # VAPI integration logic
│   └── retell_service.py     # Retell AI integration logic
├── .env                      # Environment variables
├── requirements.txt          # Project dependencies
└── venv/                     # Virtual environment (not committed)
```

---

## 🧪 Testing

You can test your API using:

- 🧪 [Postman](https://www.postman.com/)
- 🧵 [cURL](https://curl.se/)
- 🌙 [Insomnia](https://insomnia.rest/)
- 🌐 Swagger docs at `/docs`

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more information.

---

## 🙏 Acknowledgments

Special thanks to the amazing tools used:

- 🚀 [FastAPI](https://fastapi.tiangolo.com/)
- 🗣 [VAPI](https://vapi.ai/)
- 🤖 [Retell AI](https://www.retellai.com/)

---

Awesome! Here's your enhanced `README.md` with a **🔖 Badges** section and a **🚢 Deployment** section added for extra polish and professionalism:

---

# 🤖 Agent Wrapper API

A simple and scalable API built with **FastAPI** to create AI agents using either [🔊 VAPI](https://vapi.ai/) or [🧠 Retell AI](https://www.retellai.com/). This API receives agent configuration data and routes it to the chosen provider.

---

## 🔖 Badges

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green?logo=fastapi)
![MIT License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

---

## 📚 Table of Contents

- [🚀 Requirements](#-requirements)
- [🛠 Installation](#-installation)
- [🔐 Environment Variables](#-environment-variables)
- [🚦 Running the Server](#-running-the-server)
- [📬 API Usage](#-api-usage)
- [📁 Project Structure](#-project-structure)
- [🧪 Testing](#-testing)
- [🚢 Deployment](#-deployment)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🚀 Requirements

✅ Python 3.8+  
✅ `pip` for dependency management

---

## 🛠 Installation

### 1. 📥 Clone the Repository

```bash
git clone <your-repository-url>
cd agent-wrapper-api
```

### 2. 🧰 Set Up Virtual Environment

```bash
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

```env
VAPI_API_TOKEN=your_vapi_token_here
RETELL_API_KEY=your_retell_api_key_here
```

---

## 🚦 Running the Server

```bash
uvicorn app.main:app --reload
```

🌐 Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
📘 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📬 API Usage

### 📌 `POST /create-agent`

Create an AI agent.

#### Request

```json
{
  "name": "MyAgent",
  "description": "An AI agent for demonstration.",
  "voice": "echo",
  "provider": "vapi"
}
```

#### Example cURL

```bash
curl -X POST 'http://127.0.0.1:8000/create-agent' \
-H 'Content-Type: application/json' \
-d '{
  "name": "MyAgent",
  "description": "An AI agent for demonstration.",
  "voice": "echo",
  "provider": "vapi"
}'
```

---

## 📁 Project Structure

```
agent-wrapper-api/
├── app/
│   └── main.py
├── models/
│   └── agent.py
├── services/
│   ├── vapi_service.py
│   └── retell_service.py
├── .env
├── requirements.txt
└── venv/
```

---

## 🧪 Testing

Use your favorite tools:

- 🧪 [Postman](https://www.postman.com/)
- 🧵 [cURL](https://curl.se/)
- 🌙 [Insomnia](https://insomnia.rest/)
- 🧬 Swagger: `/docs`

---

## 🚢 Deployment

### 🐳 Docker (Optional)

Add the following files if you'd like to use Docker:

**`Dockerfile`**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**`docker-compose.yml`**
```yaml
version: '3'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
```

Then run:

```bash
docker-compose up --build
```

### 🌍 Render / Railway / Heroku

- Push to GitHub
- Connect your repo to your platform
- Set environment variables (`.env`)
- Deploy 🎉

Perfect! Here's the complete set of deployment files you'll need, along with explanations and emojis to keep things engaging! 🚀

---

### 🐋 `Dockerfile`

This file tells Docker how to build your container image:

```Dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### ⚓ `docker-compose.yml`

This file helps run your project locally with Docker Compose:

```yaml
version: '3.8'

services:
  agent-wrapper-api:
    build: .
    container_name: agent-wrapper-api
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - .:/app
    restart: always
```

---

### ⚙️ `.dockerignore`

Avoid sending unnecessary files to the Docker context:

```
__pycache__/
*.pyc
*.pyo
*.pyd
.env
venv/
*.sqlite3
*.log
```

---

### 🧪 Run Locally with Docker

From the root of your project:

```bash
docker-compose up --build
```

Then visit your API at: [http://localhost:8000](http://localhost:8000)  
Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

