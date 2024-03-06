#!/usr/bin/python3

# This API tool for query to gemini AI from Google.

# How to use.

# 1. Run script with string query with quotes.


import google.generativeai as genai
import os
import argparse

parser = argparse.ArgumentParser(description='User query')
parser.add_argument('query', type=str, help='Query')
args = parser.parse_args()

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(args.query)

print(response.parts)
#    print(part.content)  # Access the content of each part

#print(response)
