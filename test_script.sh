#!/bin/bash

# Config
BASE_URL="http://localhost:8000"

# Prompt for input
read -p "Enter prompt: " PROMPT
read -p "Use streaming? (y/n): " STREAM

# Choose endpoint
if [[ "$STREAM" == "y" ]]; then
    echo -e "\n--- Streaming Response ---"
    curl -N -X POST "$BASE_URL/generate/stream" \
         -H "Content-Type: application/json" \
         -d "{\"prompt\": \"$PROMPT\"}"
else
    echo -e "\n--- Standard Response ---"
    curl -s -X POST "$BASE_URL/generate" \
         -H "Content-Type: application/json" \
         -d "{\"prompt\": \"$PROMPT\"}" | jq
fi
