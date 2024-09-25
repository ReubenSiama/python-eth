import scapy.all as scapy
import argparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []

    for answered in answered_list:
        client = {
            "ip": answered[1].psrc,
            "mac": answered[1].hwsrc
        }
        client_list.append(client)

    print_result(client_list)

def print_result(results):
    print("ip\t\t\tmac")
    print("------------------------------------------------------")
    for result in results:
        print(result["ip"] + "\t\t" + result["mac"])

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--target", dest="ip_address", help="The target IP address to be scanned")
(options, args) = parser.parse_args()

if not options.ip_address:
    parser.error("Enter an IP address to scan using the -t or -target flag")

scan(options.ip_address)