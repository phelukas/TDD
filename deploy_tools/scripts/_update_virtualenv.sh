#!/bin/bash
echo "Atualizando a virtualenv"

DIR="../venv/bin/pip"

if [ ! -f "$DIR" ]; then
    echo "Se tiver to aqui"
    cd ../
    python3 -m venv venv
fi
${DIR} install -r ../requirements.txt
