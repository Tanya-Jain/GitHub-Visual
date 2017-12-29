#!/bin/sh
echo "Enter the OAuth token"
read token
curl -H "Authorization: bearer ${token}" -X POST -d " \
{ \
\"query\": \"query { viewer { login contributedRepositories (last:100) { edges { node { name commitComments (last:100) { edges { node { commit { id }}}}}}}}}\" \
} \
" https://api.github.com/graphql | python -mjson.tool > commitComments.json
python commitComments.py
