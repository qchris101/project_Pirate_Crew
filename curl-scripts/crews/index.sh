#!/bin/bash

curl "http://localhost:8000/crews/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
