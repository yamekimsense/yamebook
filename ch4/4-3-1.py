from netmiko import ConnectHandler

iosv_l2_sw1 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.30.108',
    'username' : 'cisco',
    'password' : 'cisco',
    'secret' : 'cisco',
}

iosv_l2_sw2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.30.108',
    'username' : 'cisco',
    'password' : 'cisco',
    'secret' : 'cisco',
}


iosv_l2_sw3 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.30.108',
    'username' : 'cisco',
    'password' : 'cisco',
    'secret' : 'cisco',
}

i = 0

devices = [iosv_l2_sw1,iosv_l2_sw2,iosv_l2_sw3]
filenames = ['switch1.txt', 'switch2.txt', 'switch3.txt']


for device in devices:

    filename = filenames[i]
    print ("filename ", filename)

    with open(filename) as sw1f:
        lines_sw1 = sw1f.read().splitlines()

    print ("commands", lines_sw1)
    print ("type ", type(lines_sw1))

    net_connect = ConnectHandler(**device)
    output1 = net_connect.send_config_set(lines_sw1)
    print(output1)

    output = net_connect.send_command('show ip int brief')
    print(output)

    i = i + 1
    net_connect.disconnect()



'''
works python3
requirement pip3 install netmiko
if not run, you "venv"
python3 -m venv venv
source venv/bin/activate
and then, run
'''
