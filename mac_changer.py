import subprocess
import optparse
import re

def get_current_mac(interface):
    try:
        if_config_result = subprocess.check_output(["ifconfig", interface])
        pattern_search_result = re.search(r"(\w{2}:){5}\w{2}", str(if_config_result))

        if pattern_search_result:
            return pattern_search_result.group(0)
        else:
            print("Could not read MAC address.")
    except subprocess.CalledProcessError as e:
        # Capture and print the error message
        print("Error executing command:", e.output.decode('utf-8'))
    except Exception as e:
        print("An unexpecte d error occurred:", e)

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The network interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address that you want to change to")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("Enter the interface")
    elif not options.new_mac:
        parser.error("Enter the mac address")
    return options

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

user_options = get_options()
current_mac_address = get_current_mac(user_options.interface)
print("Current MAC: " + str(current_mac_address))
# change_mac(user_options.interface, user_options.new_mac)
