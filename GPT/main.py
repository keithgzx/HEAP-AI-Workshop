"""
Documentation: 
1. https://platform.openai.com/docs/api-reference/chat
2. https://platform.openai.com/docs/api-reference/chat/object 
"""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import json
from pprint import pprint
import logging
from openai import OpenAI

load_dotenv()
logging.basicConfig(level=logging.INFO)

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPEN_API_KEY)
 
app = Flask(__name__)
CORS(app)

def jsonResponse(rescode, **kwargs):
    res_data = {key: value for key, value in kwargs.items()}
    return jsonify(res_data), rescode


@app.route("/v1/gpt/generate", methods=['POST'])
def generate_response():

    # 1. Initialize schema
    #TODO
    schema = { 
        "type": "object",
            "properties": {
                "dish": {
                    "type": "string",
                    "description": "Descriptive title of the dish"
                },
                "ingredients": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "instructions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "step": {
                                "type": "integer",
                                "description": "Step number, numbering from 1"
                            },
                            "description": {
                                "type": "string",
                                "description": "Steps to prepare the recipe."
                            }
                        }
                    }
                }
            }
        }

    # 2. Retrieve frontend request from body
    #TODO
    data = request.json
    dishName = data.get("dishName")
    # 3. Initialize openai chat completions instance with gpt-3.5-turbo model
    # 4. Show what happens if exceed token limit, unable to close json then give error
    #TODO
    chat_completions = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": f"provide output in valid json format. The data schema should be like this {json.dumps(schema)}"},
            {"role": "system", "content": "You are a helpful recipe assistant. Only use information you have been provided with"},
            {"role": "user", "content": f"Come up with a recipe for {dishName} in 3 steps"}
        ],
        temperature=0.1
    )
    data = chat_completions.choices[0].message.content
    
    return jsonResponse(200, response=json.loads(data))


if __name__ == "__main__":   
   app.run(host='127.0.0.1', port=8000, debug=True)