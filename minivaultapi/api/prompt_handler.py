import asyncio
import logging
import traceback
from fastapi import APIRouter, BackgroundTasks, status
from fastapi.responses import JSONResponse, StreamingResponse

from minivaultapi.model_loader import load_model
from minivaultapi.models.prompt_model import PromptModel__Out, PromptModel__In
from datetime import datetime
import json

LOG_FILE = "minivaultapi/logs/log.jsonl"

router = APIRouter(tags=["prompt"])
tokenizer, model = load_model()


@router.post(
    "/generate",
    response_model=PromptModel__Out,
    status_code=status.HTTP_200_OK,
)
async def generate_response(req: PromptModel__In) -> PromptModel__Out:
    prompt = req.prompt

    response_text = f"Stubbed sample response to: {prompt}\n\nThis is a placeholder response to the prompt."

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response_text
    }

    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    return PromptModel__Out(response=response_text)


@router.post("/generate/stream")
async def generate_response_stream(
    req: PromptModel__In,
    background_tasks: BackgroundTasks
) -> StreamingResponse:
    prompt = req.prompt
    response_text = ""

    try:
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, return_attention_mask=True)
        input_ids = inputs["input_ids"].to(model.device)
        attention_mask = inputs["attention_mask"].to(model.device)

        output_ids = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=100,
            temperature=0.7,
            top_k=50,
            repetition_penalty=1.2,
            eos_token_id=tokenizer.eos_token_id,
        )

        generated_ids = output_ids[0][input_ids.shape[-1]:]
    except Exception as e:
        logging.error(f"Error during token generation: {e}\n{traceback.format_exc()}")
        return JSONResponse(status_code=500, content={"error": "Failed to generate tokens"})

    async def token_stream():
        nonlocal response_text
        for token_id in generated_ids:
            token = tokenizer.decode(token_id, skip_special_tokens=True)
            if token.strip():
                response_text += token
                yield json.dumps({"response": token}) + "\n"
                await asyncio.sleep(0.05)

    def log_after_response():
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response_text
        }
        with open(LOG_FILE, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")

    background_tasks.add_task(log_after_response)

    return StreamingResponse(token_stream(), media_type="application/json")