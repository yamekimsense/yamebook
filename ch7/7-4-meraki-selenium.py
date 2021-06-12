
'''
python3 vevn venv
source venv/bin/activate

pip3 install selenium
pip3 install beautifulsoup4

also, pls install /usr/local/bin/chromedriver
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import requests, json, time

'''
#100
list up config of 
result is 
    x5 is list type, all blocked SSID
    no_block_ssid is the length if x5
'''

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get ('https://n189.meraki.com/login/dashboard_login?email=nonbeing%40gmail.com&password_login=true')
driver.implicitly_wait(1)

driver.find_element_by_name('password').send_keys('1234Qwer')
driver.find_element_by_xpath('//*[@id="login-btn"]').click()

driver.implicitly_wait(1)

driver.get ('https://n189.meraki.com/wankim-test2/n/eiqBTa9c/manage/dashboard/load_air_marshal_config')

ar_config = driver.page_source

length_ar_config = len(ar_config.split("[]"))

print ("ar_config", ar_config)
print ("length_ar_config", length_ar_config)

if length_ar_config == 3:
    no_block_ssid = 0
    x5 = []
else:
    x1 = ar_config.split("[]")[0]
    x2 = x1.split('[')[1]
    x3 = x2.split(']')[0]
    x4 = x3.replace("\"", "")

    x5 = x4.split(',')  # x5 list type, all blocked SSID/
    no_block_ssid = len(x5)  # no of blocked ssid



'''
#200 list up SSID over 30 and 30 min
result is
    ssid_tobe : list type

'''

now_time = round(time.time())

url = "https://api.meraki.com/api/v1/networks/L_669347494617964558/wireless/airMarshal"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "a084ad94cfc4bfd774e12a29d82d673fca6826ce"
}

response = requests.request('GET', url, headers=headers, data = payload)
result = response.text
result_json = json.loads(result) #used

print (type(result))
print (type(result_json)) #dict

# xxx, for beautiful printing not used
xxx = json.dumps(result_json, indent=4)

length_result = len (result_json)
print ("length_result ", length_result)

ssid_tobe = []

for i in range (0, length_result):
    sub = result_json[i]['bssids']
    length_J = len(sub[0]['detectedBy'])

    rssi_list = []
    for j in range (0, length_J):
        rssi = int (sub[0]['detectedBy'][j]['rssi'])
        rssi_list.append(rssi)

    a_ssid = result_json[i]['ssid']
    a_max = max(rssi_list)
    a_lastSeen = result_json[i]['lastSeen']
    a_timeGap = now_time - a_lastSeen
    #print (a_ssid, a_max, a_lastSeen, a_timeGap)

    '''
    #300 white list check
    '''
    white_list_check = 0
    if a_max > 29 and a_timeGap < 1800:
        white_list_check = 1
        if "douglas" in a_ssid:
            white_list_check = 0
            print ("douglas")
        if "KT" in a_ssid:
            white_list_check = 0
            print (KT)
        if "olleh" in a_ssid:
            white_list_check = 0
            #print ("olleh")
        if "U+" in a_ssid:
            white_list_check = 0
            #print ("U+")

    '''
    #400 block list check
    '''
    for ssid_check in x5:
        if ssid_check == a_ssid:
            white_list_check = 0

    if white_list_check == '':
        white_list_check = 0
        print ("there is empty SSID")

    if white_list_check == 1 and len(a_ssid) > 0:
        ssid_tobe.append(a_ssid)
        print (a_ssid, len(a_ssid))

length_ssid_tobe = len (ssid_tobe)
print ("total", length_ssid_tobe, ssid_tobe)

'''
#700 
'''

driver.get ('https://n189.meraki.com/wankim-test2/n/eiqBTa9c/manage/dashboard/air_marshal?timespan=7200')

driver.implicitly_wait(1)

step = 1

for ssid_add in ssid_tobe:

    driver.find_element_by_xpath('//*[@id="reactAirMarshalDiv"]/section/div[2]/div/div[1]/div/div/form/div[1]/div[3]/div[2]/div/div/div/div/div/div/button').click() #add a match

    driver.implicitly_wait(1)

    number = str (step + no_block_ssid)

    path = '/html/body/div/div[2]/div[1]/div[2]/div/div/section/div[2]/div/div[1]/div/div/form/div[1]/div[3]/div[2]/div/div/div/div/div/table/tbody/tr[' + number +']/td[3]/div/input'

    driver.find_element_by_xpath(path).send_keys(ssid_add) #SSID add

    step = step + 1

    driver.implicitly_wait(3)


driver.find_element_by_xpath('//*[@id="reactAirMarshalDiv"]/section/div[2]/div/div[1]/div/div/form/div[2]/button[2]').click() #click save

driver.implicitly_wait(3)

driver.quit()
