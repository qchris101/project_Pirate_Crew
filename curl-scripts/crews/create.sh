#!/bin/bash
# TOKEN="00551ae6fab2a0fb92c4c74a15a868b8469c7c9d" NAME=BeastPirates sh curl-scripts/crews/create.sh
curl "http://localhost:8000/crews/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "crew": {
      "name": "'"${NAME}"'"
    }
  }'

echo
