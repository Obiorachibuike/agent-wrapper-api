Sure! Here's your content formatted as a clean and professional `README.md` file:

```markdown
# Agent Wrapper API

A simple API built with FastAPI that allows you to create AI agents using two providers: [VAPI](https://vapi.ai/) and [Retell AI](https://www.retellai.com/). This API accepts agent configuration data and routes requests to the selected provider.

---

## 🚀 Requirements

- Python 3.8+
- `pip` for installing dependencies

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd agent-wrapper-api
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following keys:

```env
VAPI_API_TOKEN=your_vapi_token_here
RETELL_API_KEY=your_retell_api_key_here
```

---

## 🚦 Running the Server

After setting up the environment, run the FastAPI server using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The server will be live at `http://127.0.0.1:8000`.

---

## 📬 API Usage

### `POST /create-agent`

Create an AI agent using either VAPI or Retell.

#### Request Body

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

#### Sample Response

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
│   ├── __init__.py
│   └── main.py               # FastAPI app entry point
├── models/
│   ├── __init__.py
│   └── agent.py              # Pydantic model for agent request
├── services/
│   ├── __init__.py
│   ├── vapi_service.py       # Logic for VAPI integration
│   └── retell_service.py     # Logic for Retell AI integration
├── .env                      # Environment config file (not versioned)
├── requirements.txt          # Python dependencies
└── venv/                     # Virtual environment (not versioned)
```

---

## 🧪 Testing

Use any of the following tools to test the API:

- [Postman](https://www.postman.com/)
- [cURL](https://curl.se/)
- [Insomnia](https://insomnia.rest/)
- Browser (for GET endpoints)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [VAPI](https://vapi.ai/)
- [Retell AI](https://www.retellai.com/)
```

Let me know if you'd like a badge section or deployment instructions added!