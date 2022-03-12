#!/bin/bash
# TOKEN="b4c0cff8f8c5e0f2528187c3de375409f3f94098" ID=8 sh curl-scripts/crews/show.sh
curl "http://localhost:8000/crews/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
