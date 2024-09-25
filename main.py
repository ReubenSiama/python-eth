import subprocess

interface = input("Enter the interface name you want to change the MAC Address: ")
newMac = input("Enter the new MAC Address you want to change to: ")

print("[+] changing MAC address for " + interface + " to " + newMac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
subprocess.call(["ifconfig", interface, "up"])
