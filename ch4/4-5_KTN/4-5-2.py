import os,sys, shutil

files = os.listdir('.')

for ffff in files:
    if ".txt" in ffff:
        f = open(ffff,'r')
        lines = f.readlines()

        for line in lines:

            if "uptime" in line:
                uptime = line.split('uptime')[1].replace(",", "").replace("is ", "")

                if "weeks" in uptime:
                    uptime = uptime.replace(" weeks", "w")

                if "day" in uptime:
                    uptime = uptime.replace(" day", "d")

                if "hours" in uptime:
                    uptime = uptime.replace(" hours", "h")

                if "minutes" in uptime:
                    uptime = uptime.replace(" minutes", "m")


            if "System serial number" in line:
                sn = line.split(':')[1]

            if "*" in line:
                while "  " in line:
                    line = line.replace("  "," ")
                line = line.split(" ")
                model = line[3]
                ios = line [4]

        print (ffff.replace(".txt", ""),  model.replace("WS-C",""), sn.replace("\n",""), ios, uptime.replace("\n",""))
