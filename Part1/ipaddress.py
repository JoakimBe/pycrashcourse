import ipaddress

ipList = ['192.168.0.1', '10.0.0.1', '172.16.0.9', '192.168.2.1']
network = '172.16.0.0/16'

for ip in ipList:

    if ipaddress.IPv4Address(ip) in list(ipaddress.ip_network(network).hosts()):
        print("{ip} is obviously in {network}".format(ip=ip, network=network))
    else:
        print("{ip} is not in {network} :(".format(ip=ip, network=network))
