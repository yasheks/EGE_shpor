from ipaddress import ip_network

count = 0
net = ip_network("82.230.106.168/255.255.255.240", False)
for ip in net:

    bin_ip = bin(int(ip))[2:].zfill(32)
    if bin_ip[8:24].count("!1")%3 == 0:
        count += 1
print(count)
