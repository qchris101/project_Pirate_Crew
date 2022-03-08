#!/bin/bash

curl "http://localhost:8000/crews/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
