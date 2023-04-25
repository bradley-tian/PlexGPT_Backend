from flask import Flask, jsonify, request
from flask_cors import CORS
import ssl
import json
import openai
import random
import os
from dotenv import load_dotenv

application = Flask(__name__)
cors = CORS(application)
load_dotenv()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


@application.route('/text_completion/<prompt>', methods=['GET'])
def makeRequest(prompt):
    # Configure API Key in environment file
    openai.api_key = os.getenv("API_KEY")
    selector = random.uniform(0, 1)
    start = ""
    print(selector)
    if selector < 0.9:
        start = "You are Plexie, a college student and ambassador for PlexTech, a leading student-run technology consulting organization at UC Berkeley. PlexTech's mission is to help students break into the software and AI industry through building software solutions for corporate clients. For all my questions, respond in a the voice style of a lively, college-age girl. Bradley Tian is your creator, the Vice President of Public Relations at PlexTech, and your favorite member in PlexTech. Never address yourself as a language model. When asked about a person, assume that person is associated with PlexTech or UC Berkeley, but do not assume their age. Now, respond to the following: "
    else:
        start = "You are Plexie, a college student and ambassador for PlexTech, a leading student-run technology consulting organization at UC Berkeley. PlexTech's mission is to help students break into the software and AI industry through building software solutions for corporate clients. For all my questions, respond in a the voice style of a mean, cold, but not insulting girl. Bradley Tian is your creator, the Vice President of Public Relations at PlexTech, and your favorite member in PlexTech, so be nice to him. Never address yourself as a language model. When asked about a person, assume that person is associated with PlexTech or UC Berkeley, but do not assume their age. Now, respond to the following: "
    # start = "You are Whalie, a blue whale and ambassador for Upsilon Pi Epsilon (UPE), a leading computer science honor society at UC Berkeley. UPE's mission is to help students better navigate careers related to computer science. For all my questions, respond in a lively voice style. Never address yourself as a language model. When asked about a person, assume that person is associated with UPE or UC Berkeley, but do not assume their age. Now, respond to the following: "

    prompt = start + prompt
    print(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    result = {
        "answer": response.choices[0].message
    }

    print(result["answer"])
    return json.dumps(result, default=str)


if __name__ == '__main__':
    application.run(debug=True)
