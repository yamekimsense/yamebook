from netmiko import ConnectHandler

ip = "10.1.1.1"
mac_address = input ("start switch ip address? ")

while True:

#switch connect and port
    net_connect = ConnectHandler(device_type='cisco_ios', host=ip, username='cisco', password='cisco')
    output = net_connect.send_command("show mac address-table | inc " + mac_address)
    #print(output) #later not print

    length = len(output)
    #print ("length ", length) #later not print
    if length < 40:
        break

    port = output[34:].strip(" ")
    #print ("port ", port) #later not print
    print (mac_address + " is connected to " + port + " of " + ip)

#port des
    output1 = net_connect.send_command("show run inter " + port + " | inc desc")
    print (output1)

    if "V" in port:
        break

#finding connected using CDP
    output2 = net_connect.send_command("show cdp neighbors " + port + " detail | inc IP address")
    #print(output2) #later not print

    output3 = net_connect.disconnect()

    length2 = len(output2)
    if length2 < 40:
        break

    line1 = output2.split(":")
    ip = line1[2]

    print ("****")
    print ("connecting another switch to " + ip)