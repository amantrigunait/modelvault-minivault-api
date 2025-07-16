# MiniVault API

## Setup Instructions

1. **Clone the Repository**

   ```
   git clone https://github.com/amantrigunait/modelvault-minivault-api
   cd modelvault-minivault-api
   ```

2. **Create a Virtual Environment**

   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```
   python3 -m pip install -r requirements.txt
   ```

4. **Run the Server**

   ```
   uvicorn main:app --reload
   ```


## 🧪 Endpoints

### `POST /generate`

- **Description:** Returns a stubbed response based on the provided prompt.
- **Request Body:**
  ```json
  {
    "prompt": "Your input prompt"
  }
  ```
- **Response:**
  ```json
  {
    "response": "Stubbed sample response to: Your input prompt"
  }
  ```

---

### `POST /generate/stream`

- **Description:** Returns a streamed token-by-token response
- **Request Body:**
  ```json
  {
    "prompt": "Your input prompt"
  }
  ```
- **Response:**
  ```
  {"response": "Token1"}
  {"response": "Token2"}
  ...
  ```

---

## 📜 CLI Script (`test_prompt.sh`)

This script allows quick terminal-based interaction.

- Run it with:
  ```bash
  ./test_prompt.sh
  ```

- You’ll be prompted to:
  - Enter a prompt.
  - Choose between regular or streaming mode.

---

## 📁 Logging

- Every request is logged in JSON Lines format to:
  ```
  minivaultapi/logs/log.jsonl
  ```
- Example log entry:
  ```json
  {
    "timestamp": "2025-07-16T01:23:45",
    "prompt": "Tell me a joke",
    "response": "Stubbed sample response to: Tell me a joke"
  }
  ```

## Design Choices

1. **Using GPT-2 with Local Cache**  
   Using Hugging Face to load and cache GPT-2 locally.

2. **Modularizing Model Loading into `model_loader.py`**  
   The model loading logic is separated into its own module to keep route handlers clean and maintainable. This improves testability and sets the foundation for future extensibility.

3. **Streaming Responses with `StreamingResponse`**  
   The `/generate/stream` endpoint streams generated tokens in real time, providing a more interactive, responsive experience for the user.

---

## 🔮 Future Improvements

- **Supporting Multiple Models**  
  Extend the `model_loader.py` to load different models dynamically based on configuration or request parameters. This enables experimentation and broader use cases (e.g., GPT-2, TinyLlama, Mistral).