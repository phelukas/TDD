#!/bin/bash
echo "Atalizando o git"

REPO_URL="https://github.com/phelukas/TDD"
DIR="../.git"

if [ -d "$DIR" ]; then
    echo "Se tiver to aqui"
    pwd
    cd ../
    pwd
    git fetch
else
    echo "não tem em "
fi
