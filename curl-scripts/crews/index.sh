#!/bin/bash
# TOKEN="56b38ba7f276fcf1aec8034b66dd6c7a0d196756" ID=2 sh curl-scripts/crews/show.sh
curl "http://localhost:8000/crews/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
