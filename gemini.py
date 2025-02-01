#!/usr/bin/python

# This API tool for query to gemini AI from Google.

# How to use.
# 1. API_KEY setup in .bashrc 'export API_KEY='xxxxxxxx' && source .bashrc
# 2. Run script with string query with quotes.


import google.generativeai as genai
import os
import argparse
from rich import print
from rich.markdown import Markdown

prompt = """You are an assistant administrator and user of the
Linux system. Next comes the query: \n"""

parser = argparse.ArgumentParser(description='User query')
parser.add_argument('query', type=str, help='Query')
args = parser.parse_args()
genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(prompt + args.query)
response_formated = Markdown(str(response.parts[0].text))

print(response_formated)

