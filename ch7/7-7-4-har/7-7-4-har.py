'''
input the web URL to connect
make the HAR
extract connect - wait -download
make the waterfall chart

download chrome driver

pip3 install selenium-wire
'''


#100 start
from seleniumwire import webdriver
import json, time, datetime, webbrowser, os, sys

#200 input URL
web_add = input("input URL with http or https ? ")
print ("Wait a moment. It takes 5~10 seconds.")

#300 GET HAR of URL
options = {
    'enable_har': True,
    'disable_encoding': True
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('ignore-certificate-errors')
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")

driver = webdriver.Chrome(seleniumwire_options=options, options = chrome_options)
driver.get(web_add)

json_val = driver.har

#310 local time
now = time.localtime()
now = "%04d%02d%02d-%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
print ("now is", now, type(now))

os.makedirs('./temp', exist_ok=True) #320 temp directory make if not

#330 HAR file export to temp folder
direc = os.path.dirname(os.path.realpath(__file__)) + "/"
tempfile = direc + "temp/" + now + ".har"

f = open(tempfile,'w')
f.write(json_val)
f.close()




#380 human time to unix time converter
def unixtime(date_str):
    date_str = date_str[0:23].replace("T", " ")
    str_to_dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    unixtime2 = int(str_to_dt.timestamp() * 1000)

    return unixtime2


#400 HAR file reading
f = open(tempfile, 'r')
data = f.read()
f.close()

dicttt = json.loads(data)
xxx = json.dumps(dicttt, indent=4)

dicttt = json.loads(data)["log"]["entries"]

print ("startDateTime ", dicttt[0]["startedDateTime"])
ini_time = unixtime(dicttt[0]["startedDateTime"])

#430 HTML file making - 3 files
result_frame = direc + "temp/" +  now + "_frame.html"
result_left = direc +  "temp/" + now + "_left.html"
result_right = direc +  "temp/" + now + "_right.html"


#440 frame html
ff = open(result_frame, 'w')
ff.write("<html><title> YAME TE - Waterfall </title><frameset cols=\"705,*\" frameborder=\"1\">")
ff.write("<frame src=\"" + result_left + "\" name=\"left\">")
ff.write("<frame src=\"" + result_right + "\" name=\"right\">")
ff.write("</frameset></html>")
ff.close()

#450 left and right HTML
fl = open(result_left, 'w') ### fl for left side HTML
fr = open(result_right, 'w') ### fr for right side HTML

#460 left side
fl.write("<html>")
fl.write("<title> YAME TE - Waterfall </title>\n")
fl.write("<body>\n")
fl.write("<span style=\"font-size: 10pt; font-family: arial;\">\n")

fl.write("<table border=\"0\" width=\"700\"> \n")
fl.write("<tr>")
fl.write("<td width=\"200\">file</td> \n")
fl.write("<td width=\"100\">status</td>  \n")
fl.write("<td width=\"200\">domain</td> \n")

fl.write("<td width=\"50\">time</td>  \n")
fl.write("<td width=\"50\">connect</td>  \n")
fl.write("<td width=\"50\">wait</td>  \n")
fl.write("<td width=\"50\">download</td>  \n")

fl.write("</tr> \n")
fl.write("</table> \n")


#470 right side
fr.write("<html>")
fr.write("<title> YAME TE - Waterfall </title>\n")
fr.write("<body>\n")
fr.write("<span style=\"font-size: 10pt; font-family: arial;\">\n")
fr.write("<table border=\"0\" width=\"10000\"> \n")
fr.write("<tr>")

fr.write("<td align=right width=\"200\" bgcolor=\"#A0A0A0\">Queue(200ms)</td> \n")
fr.write("<td align=right width=\"200\" bgcolor=\"#00c548\">Wait(400ms)</td> \n")
fr.write("<td align=right width=\"200\" bgcolor=\"#009ef2\">Down(600ms)</td> \n")

#480 right side column
for i in range (800,10200,200):
    fr.write("<td align=right width=\"200\" bgcolor=\"white\">" + str(i) + "</td> \n")

fr.write("</tr> \n")
fr.write("</table> \n")

#500 each component output

for i in range (0, len (dicttt) ) :
    each_time = unixtime(dicttt[i]["startedDateTime"])
    delta = each_time - ini_time

    URL_ini = dicttt[i]["request"]["url"]
    URL_spit = URL_ini.split("/")
    URL_length = len(URL_spit)-1
    URL = URL_spit[0] + URL_spit[1] + "//" + URL_spit[2]

    file_name = URL_spit[URL_length]
    file_name_len = len(file_name) - 15
    if len(file_name) > 15:
        file_name = "~" + file_name[file_name_len:]

    connect = dicttt[i]["timings"]["connect"]
    wait = dicttt[i]["timings"]["wait"]
    receive = dicttt[i]["timings"]["receive"]
    status = str(dicttt[i]["response"]["status"])
    last = 10000 -delta - connect - wait - receive -100

#510 left side add
    fl.write("\n\n\n")
    fl.write("<table border=\"0\" width=\"700\"> \n")
    fl.write("<tr>")
    fl.write("<td width=\"200\">" + file_name + "</td> \n")
    fl.write("<td width=\"100\">" + status + "</td>  \n")
    fl.write("<td width=\"200\">" + URL + "</td> \n")

    fl.write("<td width=\"50\">" + str(dicttt[i]["time"]) + "</td> \n")
    fl.write("<td width=\"50\">" + str(connect) + "</td> \n")
    fl.write("<td width=\"50\">" + str(wait) + "</td> \n")
    fl.write("<td width=\"50\">" + str(receive) + "</td> \n")
    fl.write("</tr> \n")
    fl.write("</table> \n")
    fl.write("\n")

#520 right side add
    fr.write("\n\n\n")
    fr.write("<table border=\"0\" width=\"10000\"> \n")
    fr.write("<tr>")
    fr.write("<td width=\"" + str(delta) + "\" bgcolor=\"white\"></td> \n")
    fr.write("<td width=\"" + str(connect) + "\" bgcolor=\"#A0A0A0\"></td> \n")
    fr.write("<td width=\"" + str(wait) + "\" bgcolor=\"#00c548\"></td> \n")
    fr.write("<td width=\"" + str(receive) + "\" bgcolor=\"#009ef2\"></td> \n")
    fr.write("<td width=\"" + str(last) + "\" bgcolor=\"white\"></td> \n")
    fr.write("<td width=\"100\" bgcolor=\"white\">100</td> \n")
    fr.write("</tr> \n")
    fr.write("</table> \n")
    fr.write("\n")

#530 left and rifht side HTML end
fl.write("</span>")
fl.write("</body>")
fl.write("</html>")

fr.write("</span>")
fr.write("</body>")
fr.write("</html>")

fl.close()
fr.close()

#600 call the web browser
web_URL = "file://" + result_frame
print ("web_URL", web_URL)
webbrowser.open_new(web_URL)
print ("END")
