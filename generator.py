from itertools import count

import entity
import network
import json
import random
import opensearchpy
from time import sleep

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

    if topology_name == "images/top-3A.jpg":
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

        print(f"> DEBUG: {subnetwork_list[3]}")

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


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    else:
        print("Ошибка передачи топологии!")

    print(
    f" --- Personal Computers ---\n"
    f"PC = {len(pc['users'])}\n"
    f"{pc['users']}\n"
    f"{pc['ip']}\n"
    f"{pc['mac']}\n"
    f" --- Switches ---\n"
    f"SW = {len(switch['users'])}\n"
    f"{switch['users']}\n"
    f"{switch['ip']}\n"
    f"{switch['mac']}\n"
    f" --- Routers ---\n"
    f"RT = {len(router['users'])}\n"
    f"{router['users']}\n"
    f"{router['ip']}\n"
    f"{router['mac']}\n"
    f" --- Firewalls ---\n"
    f"FW = {len(firewall['users'])}\n"
    f"{firewall['users']}\n"
    f"{firewall['ip']}\n"
    f"{firewall['mac']}\n"
    )



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

    else:
        return {
            "user": [],
            "ip": [],
            "mac": []
        }



def generator_protocols(client, index_name, users, list_ip_addr, list_mac_addr):

    # --- ATTENTION! --- USE IN INFINITELY LOOP! --- ONE-TIME ACTION! ---

    operations = []
    operations_index = 0

    operations.append(random.randint(1, 21))
    while operations_index < len(operations):

        count_sec = random.uniform(0.1, 10)
        sleep(count_sec)
        user = random.choice(users)

        if type(user) == entity.PersonalComputerLinux or type(user) == entity.PersonalComputerWindows:
            if type(user) == entity.PersonalComputerLinux:
                print("Linux -> ", end="")
            if type(user) == entity.PersonalComputerWindows:
                print("Windows -> ", end="")
            if operations[operations_index] == 1:
                print(f"{operations_index}, {operations[operations_index]} | auth_info", end=", ")
                logs = (user.auth_info_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[operations_index] == 2:
                print(f"{operations_index}, {operations[operations_index]} | auth_warning", end=", ")
                logs = (user.auth_warning_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 3:
                print(f"{operations_index}, {operations[operations_index]} | auth_crit", end=", ")
                logs = (user.auth_crit_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 4:
                print(f"{operations_index}, {operations[operations_index]} | start_process_info", end=", ")
                logs = (user.start_process_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 5:
                print(f"{operations_index}, {operations[operations_index]} | start_process_warning", end=", ")
                logs = (user.start_process_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 6:
                print(f"{operations_index}, {operations[operations_index]} | start_process_debug", end=", ")
                logs = (user.start_process_debug_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 7:
                print(f"{operations_index}, {operations[operations_index]} | open_file_info", end=", ")
                logs = (user.open_file_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 8:
                print(f"{operations_index}, {operations[operations_index]} | open_file_warning", end=", ")
                logs = (user.open_file_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 9:
                print(f"{operations_index}, {operations[operations_index]} | open_file_crit", end=", ")
                logs = (user.open_file_crit_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 10:
                print(f"{operations_index}, {operations[operations_index]} | network_activity_info", end=", ")
                logs = (user.network_activity_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 11:
                print(f"{operations_index}, {operations[operations_index]} | network_activity_warning", end=", ")
                logs = (user.network_activity_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 12:
                print(f"{operations_index}, {operations[operations_index]} | network_activity_debug", end=", ")
                logs = (user.network_activity_debug_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 13:
                print(f"{operations_index}, {operations[operations_index]} | edit_policies_notice", end=", ")
                logs = (user.edit_policies_notice_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 14:
                print(f"{operations_index}, {operations[operations_index]} | edit_policies_warning", end=", ")
                logs = (user.edit_policies_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 15:
                print(f"{operations_index}, {operations[operations_index]} | edit_policies_info", end=", ")
                logs = (user.edit_policies_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 16:
                print(f"{operations_index}, {operations[operations_index]} | remote_control_info", end=", ")
                logs = (user.remote_control_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 17:
                print(f"{operations_index}, {operations[operations_index]} | remote_control_warning", end=", ")
                logs = (user.remote_control_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 18:
                print(f"{operations_index}, {operations[operations_index]} | remote_control_alert", end=", ")
                logs = (user.remote_control_alert_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 19:
                print(f"{operations_index}, {operations[operations_index]} | update_system_info", end=", ")
                logs = (user.update_system_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 20:
                print(f"{operations_index}, {operations[operations_index]} | update_system_err", end=", ")
                logs = (user.update_system_err_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 21:
                print(f"{operations_index}, {operations[operations_index]} | update_system_notice", end=", ")
                logs = (user.update_system_notice_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        elif type(user) == entity.Switch:
            print("Switch -> ", end="")
            if operations[operations_index] == 1:
                print(f"{operations_index}, {operations[operations_index]} | change_status_port_info", end=", ")
                logs = (user.change_status_port_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 2:
                print(f"{operations_index}, {operations[operations_index]} | change_status_port_warning", end=", ")
                logs = (user.change_status_port_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 3:
                print(f"{operations_index}, {operations[operations_index]} | change_status_port_crit", end=", ")
                logs = (user.change_status_port_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 4:
                print(f"{operations_index}, {operations[operations_index]} | learn_mac_addr_info", end=", ")
                logs = (user.learn_mac_addr_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 5:
                print(f"{operations_index}, {operations[operations_index]} | learn_mac_addr_warning", end=", ")
                logs = (user.learn_mac_addr_warning(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 6:
                print(f"{operations_index}, {operations[operations_index]} | learn_mac_addr_debug", end=", ")
                logs = (user.learn_mac_addr_debug(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 7:
                print(f"{operations_index}, {operations[operations_index]} | violation_port_security_warning", end=", ")
                logs = (user.violation_port_security_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 8:
                print(f"{operations_index}, {operations[operations_index]} | violation_port_security_crit", end=", ")
                logs = (user.violation_port_security_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 9:
                print(f"{operations_index}, {operations[operations_index]} | violation_port_security_alert", end=", ")
                logs = (user.violation_port_security_alert())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 10:
                print(f"{operations_index}, {operations[operations_index]} | stp_event_info", end=", ")
                logs = (user.stp_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 11:
                print(f"{operations_index}, {operations[operations_index]} | stp_event_warning", end=", ")
                logs = (user.stp_event_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 12:
                print(f"{operations_index}, {operations[operations_index]} | stp_event_crit", end=", ")
                logs = (user.stp_event_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 13:
                print(f"{operations_index}, {operations[operations_index]} | duplex_error_warning", end=", ")
                logs = (user.duplex_error_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 14:
                print(f"{operations_index}, {operations[operations_index]} | duplex_error_err", end=", ")
                logs = (user.duplex_error_err())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 15:
                print(f"{operations_index}, {operations[operations_index]} | duplex_error_crit", end=", ")
                logs = (user.duplex_error_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 16:
                print(f"{operations_index}, {operations[operations_index]} | vlan_event_info", end=", ")
                logs = (user.vlan_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 17:
                print(f"{operations_index}, {operations[operations_index]} | vlan_event_info", end=", ")
                logs = (user.vlan_event_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 18:
                print(f"{operations_index}, {operations[operations_index]} | vlan_event_debug", end=", ")
                logs = (user.vlan_event_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 19:
                print(f"{operations_index}, {operations[operations_index]} | auth_802_1x_info", end=", ")
                logs = (user.auth_802_1x_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 20:
                print(f"{operations_index}, {operations[operations_index]} | auth_802_1x_warning", end=", ")
                logs = (user.auth_802_1x_warning(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 21:
                print(f"{operations_index}, {operations[operations_index]} | auth_802_1x_alert", end=", ")
                logs = (user.auth_802_1x_alert(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        elif type(user) == entity.Router:
            print("Router -> ", end="")
            if operations[operations_index] == 1:
                print(f"{operations_index}, {operations[operations_index]} | change_status_int_info", end=", ")
                logs = (user.change_status_int_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 2:
                print(f"{operations_index}, {operations[operations_index]} | change_status_int_warning", end=", ")
                logs = (user.change_status_int_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 3:
                print(f"{operations_index}, {operations[operations_index]} | change_status_int_crit", end=", ")
                logs = (user.change_status_int_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 4:
                print(f"{operations_index}, {operations[operations_index]} | change_roadmap_info", end=", ")
                logs = (user.change_roadmap_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 5:
                print(f"{operations_index}, {operations[operations_index]} | change_roadmap_warning", end=", ")
                logs = (user.change_roadmap_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 6:
                print(f"{operations_index}, {operations[operations_index]} | change_roadmap_alert", end=", ")
                logs = (user.change_roadmap_alert())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 7:
                print(f"{operations_index}, {operations[operations_index]} | dynamic_routing_event_info", end=", ")
                logs = (user.dynamic_routing_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 8:
                print(f"{operations_index}, {operations[operations_index]} | dynamic_routing_event_warning", end=", ")
                logs = (user.dynamic_routing_event_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 9:
                print(f"{operations_index}, {operations[operations_index]} | dynamic_routing_event_crit", end=", ")
                logs = (user.dynamic_routing_event_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 10:
                print(f"{operations_index}, {operations[operations_index]} | acl_activity_info", end=", ")
                logs = (user.acl_activity_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 11:
                print(f"{operations_index}, {operations[operations_index]} | acl_activity_warning", end=", ")
                logs = (user.acl_activity_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 12:
                print(f"{operations_index}, {operations[operations_index]} | acl_activity_debug", end=", ")
                logs = (user.acl_activity_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 13:
                print(f"{operations_index}, {operations[operations_index]} | nat_event_info", end=", ")
                logs = (user.nat_event_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 14:
                print(f"{operations_index}, {operations[operations_index]} | nat_event_warning", end=", ")
                logs = (user.nat_event_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 15:
                print(f"{operations_index}, {operations[operations_index]} | nat_event_debug", end=", ")
                logs = (user.nat_event_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 16:
                print(f"{operations_index}, {operations[operations_index]} | icmp_message_info", end=", ")
                logs = (user.icmp_message_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 17:
                print(f"{operations_index}, {operations[operations_index]} | icmp_message_warning", end=", ")
                logs = (user.icmp_message_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 18:
                print(f"{operations_index}, {operations[operations_index]} | icmp_message_debug", end=", ")
                logs = (user.icmp_message_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 19:
                print(f"{operations_index}, {operations[operations_index]} | violation_traffic_info", end=", ")
                logs = (user.violation_traffic_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 20:
                print(f"{operations_index}, {operations[operations_index]} | violation_traffic_warning", end=", ")
                logs = (user.violation_traffic_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif operations[operations_index] == 21:
                print(f"{operations_index}, {operations[operations_index]} | violation_traffic_debug", end=", ")
                logs = (user.violation_traffic_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        elif type(user) == entity.Firewall:
            print("Firewall -> ", end="")
            if (operations[operations_index] % 10) == 1 or operations[operations_index] == 1:
                print(f"{operations_index}, {operations[operations_index]} | allow_traffic_info", end=", ")
                logs = (user.allow_traffic_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 2 or operations[operations_index] == 2:
                print(f"{operations_index}, {operations[operations_index]} | allow_traffic_debug", end=", ")
                logs = (user.allow_traffic_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 3 or operations[operations_index] == 3:
                print(f"{operations_index}, {operations[operations_index]} | lock_traffic_warning", end=", ")
                logs = (user.lock_traffic_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 4 or operations[operations_index] == 4:
                print(f"{operations_index}, {operations[operations_index]} | lock_traffic_alert", end=", ")
                logs = (user.lock_traffic_alert(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 5 or operations[operations_index] == 5:
                print(f"{operations_index}, {operations[operations_index]} | lock_traffic_debug", end=", ")
                logs = (user.lock_traffic_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 6 or operations[operations_index] == 6:
                print(f"{operations_index}, {operations[operations_index]} | change_session_info_connect", end=", ")
                logs = (user.change_session_info_connect(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 7 or operations[operations_index] == 7:
                print(f"{operations_index}, {operations[operations_index]} | change_session_info_breakup", end=", ")
                logs = (user.change_session_info_breakup(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 8 or operations[operations_index] == 8:
                print(f"{operations_index}, {operations[operations_index]} | change_session_debug", end=", ")
                logs = (user.change_session_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 9 or operations[operations_index] == 9:
                print(f"{operations_index}, {operations[operations_index]} | vpn_tunnel_info", end=", ")
                logs = (user.vpn_tunnel_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1
            elif (operations[operations_index] % 10) == 0 or operations[operations_index] == 10:
                print(f"{operations_index}, {operations[operations_index]} | vpn_tunnel_warning", end=", ")
                logs = (user.vpn_tunnel_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
                operations_index += 1

        else:
            print("Stop!")
            break


def unit_test():
    pass

if __name__ == "__main__":
    unit_test()