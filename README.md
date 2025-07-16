# 🧠 MiniVault API

## ⚙️ Setup Instructions

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