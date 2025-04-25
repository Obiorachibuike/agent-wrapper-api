---
# Agent Wrapper API

This is a simple API built with FastAPI that allows you to create AI agents using two different providers: [VAPI](https://vapi.ai/) and [Retell AI](https://www.retellai.com/). The API accepts agent configuration data and routes the requests to the respective provider.

## Requirements

Before running the application, make sure to install the necessary dependencies. The project uses Python 3.8+.

### Install Dependencies

1. Clone the repository:
    ```bash
    git clone <your-repository-url>
    cd agent-wrapper-api
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

Create a `.env` file in the root directory of the project and add the following keys:

- `VAPI_API_TOKEN`: Your API token for [VAPI](https://vapi.ai/).
- `RETELL_API_KEY`: Your API key for [Retell AI](https://www.retellai.com/).

Example `.env` file:

```plaintext
VAPI_API_TOKEN=your_vapi_token_here
RETELL_API_KEY=your_retell_api_key_here
```

## How to Run

1. After setting up the virtual environment and adding your `.env` file, you can start the FastAPI server using `uvicorn`:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Your FastAPI server should now be running at `http://127.0.0.1:8000`.

3. You can test the API by making POST requests to the `/create-agent` endpoint.

    Example Request Body:
    ```json
    {
        "name": "MyAgent",
        "description": "An AI agent for demonstration.",
        "voice": "echo",
        "provider": "vapi"
    }
    ```

    Example cURL request:
    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/create-agent' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "MyAgent",
        "description": "An AI agent for demonstration.",
        "voice": "echo",
        "provider": "vapi"
    }'
    ```

    Response Example (from VAPI):
    ```json
    {
        "id": "some-agent-id",
        "name": "MyAgent",
        "description": "An AI agent for demonstration.",
        "voice": "echo"
    }
    ```

## API Endpoints

### `POST /create-agent`

This endpoint allows you to create an AI agent using either the VAPI or Retell provider.

**Request Body:**

```json
{
  "name": "string",            # The name of the agent
  "description": "string",     # Optional: A short description of the agent
  "voice": "string",           # Optional: The voice for the agent (default: "echo")
  "provider": "string"         # Provider to use ("vapi" or "retell")
}
```

**Response:**

- Returns the created agent details, including an ID, name, description, and voice.

Example Response:
```json
{
  "id": "some-agent-id",
  "name": "MyAgent",
  "description": "An AI agent for demonstration.",
  "voice": "echo"
}
```

## Project Structure

```
agent-wrapper-api/          # Project Root Directory
├── app/                    # Contains your FastAPI app logic
│   ├── __init__.py
│   ├── main.py             # FastAPI application entry point
├── models/                 # Pydantic models for request validation
│   ├── __init__.py
│   └── agent.py            # Model for agent request data
├── services/               # Contains logic for interacting with external APIs
│   ├── __init__.py
│   ├── vapi_service.py     # VAPI API logic
│   └── retell_service.py   # Retell AI API logic
├── .env                    # Store environment variables (API keys, tokens, etc.)
├── requirements.txt        # List of dependencies
└── venv/                   # Virtual environment folder (automatically created)
```

## Testing

To test the API locally, you can use any HTTP client such as:

- Postman
- cURL (as shown above)
- Insomnia
- or simply the browser (for GET requests)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [VAPI](https://vapi.ai/)
- [Retell AI](https://www.retellai.com/)
---
