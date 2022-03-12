#!/bin/bash
# TOKEN="b4c0cff8f8c5e0f2528187c3de375409f3f94098" NAME=BeastPirates90 sh curl-scripts/crews/create.sh
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
