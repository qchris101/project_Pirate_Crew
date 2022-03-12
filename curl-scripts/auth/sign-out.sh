# "2b1fd9259c7db45ebd08824a462704c7ecf040a5" sh curl-scripts/auth/sign-out.sh
curl "http://localhost:8000/sign-out/" \
  --include \
  --request DELETE \
  --header "X-CSRFToken: ${CSRF}" \
  --header "Authorization: Token ${TOKEN}" \

echo
