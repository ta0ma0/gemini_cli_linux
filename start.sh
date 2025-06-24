#!/bin/bash
WORK_DIR="~/opt/gemini_cli_linux"
cd $WORK_DIR
source venv/bin/activate
python gemini.py "$1"