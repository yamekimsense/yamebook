# -*- coding: utf-8 -*-

import time, datetime
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
from flask import Flask
from flask import request
import requests
import json


botEmail = "yame-papago@webex.bot"
accessToken = "NTc4ZDAyMDAtMDE1Ny00OTNmLTlhMzAtODJkMTJkZjg4YzJlMjRkY2RkZmUtNTkw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"  # Bot's access token
host = "https://api.ciscospark.com/v1/"
headers = {"Authorization": "Bearer %s" % accessToken, "Content-Type": "application/json"}

app = Flask(__name__)


@app.route('/', methods=['POST'])

def get_tasks():
        print ("============================================================================")
        print (datetime.datetime.now())

        email = request.json.get('data').get('personEmail')
        print ("email =", email)

        if email == botEmail :
            return("")

        messageId = request.json.get('data').get('id')
        print ("all == ", request.json.get('data'))
        room = request.json.get('data').get('roomId')
        print ("room_id == ", room)

        response = requests.get(host + "messages/" + messageId, headers=headers)
        key = response.json().get('text')
        print ("keyword length ==", len(key))
        print ("keyword is == ", key)


#papao line
#language detection

        headers1 = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Naver-Client-Id': 'hldfCVPrhBjZ75dJw5CO',
            'X-Naver-Client-Secret': 'XosxgTnXqX',
        }


        data1 = {
            'query': key
        }

        response = requests.post('https://openapi.naver.com/v1/papago/detectLangs', headers=headers1, data=data1)

        language = json.loads(response.text)['langCode']

#translate
        print ("language is ====", language)

        if language == "ko":
            source = "ko"
            target = "en"
        else:
            source = "en"
            target = "ko"

        data2 = {
            'source': source,
            'target': target,
            'text': key
        }

        response = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers1, data=data2)
        result = json.loads(response.text)
        context = result['message']['result']['translatedText']
        print ("tlanslated result is ", context)

#return to webex teams

        payload = {"roomId": room, "text": context }
        response = requests.request("POST", "https://api.ciscospark.com/v1/messages/", data=json.dumps(payload),
                                                    headers=headers)
        return ("")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)
