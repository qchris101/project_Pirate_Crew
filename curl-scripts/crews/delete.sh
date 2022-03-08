#!/bin/bash

curl "http://localhost:8000/crews/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
