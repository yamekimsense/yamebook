import numpy, math

# i = interface port number
for i in range(1,49):
    #print ("i= ", i)

    f = open("netflow.txt", 'r')
    lines = f.readlines()
    f.close()

    #length is line number
    length = len (lines)
    #print ("LEN= ", length)

    j = 0
    #j = line number

    port = []

    k = 0
    #k = list number of port

    for line in lines:
        j = j + 1

        # j > 11 : until 11, header. from 12 there is data.
        if j > 11 and j < (length-1):
            data = line.split(",")
            #print ("J= ", j)

            interface = data[2]
            #print ("interafce= ", interface)
            inter = interface.split("/")
            #print (inter[0], inter[1], inter[2])

            #6 is TCP..
            if data[3] == "6\n" and inter[2] == str(i):
                #print (data[0], data[1], data[2], data[3])
                portno = int (data[1])
                #print ("port no type = ", type(portno))
                #print ("port no = ", portno)
                port.insert(k,portno)
                k = k + 1

    portlen = len(port)
    port.sort()

    if portlen > 0:
        max = port[portlen - 1]
        min = port[0]
        avg = math.ceil( numpy.mean(port) )
        var = math.ceil( numpy.var(port) )
        std = math.ceil( numpy.std(port) )

        print ("### interface= G1/0/", i, "tcp port numbers= ", portlen, "gap= ", max-min, "max= ", max, "min =", min, "avg= ", avg, "var= ", var, "std= ", std, "tcp ports are= ", port)

