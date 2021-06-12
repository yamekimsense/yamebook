from flask import Flask, render_template, redirect, request, url_for
import requests, json, datetime, time

app = Flask(__name__, template_folder='/root')

@app.route('/')
def main_get(num=None):
    return render_template('7-5-index.html', num=num)


@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):

    #Get the MAC from HTML input as client_id
    client_id = request.args.get('char1')
    print ("client_id = ", client_id)

    url = "https://api.meraki.com/api/v1/networks/{network}/clients/" + client_id

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "1234567890123456789012345678901234567890"
    }

    response = requests.request('GET', url, headers=headers, data=payload)
    dicttt = json.loads(response.text.encode('utf8'))

    apMAC = dicttt['recentDeviceMac']
    lastTime = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(dicttt['lastSeen']))

    print ("apMAC", apMAC)
    print ("lastTime Seen", lastTime)

    #based upon APMAC, find the AP location from ap text file
    f = open("7-5-aplist.txt", 'r')
    lines = f.readlines()
    for line in lines:
        # print (line)
        separate = line.split(' ')
        if apMAC == separate[0]:
            # print (line)
            last_ap_name = separate[1]
            last_lat = separate[2]
            last_lng = separate[3]
    f.close()

    print (apMAC, last_ap_name, last_lat, last_lng, lastTime)

    return render_template('7-5-map.html', last_ap_mac=apMAC, last_ap_name=last_ap_name, last_lat=last_lat,
                           last_lng=last_lng, last_time=lastTime, client_id=client_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80", debug=True, threaded=True)