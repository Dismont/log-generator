import entity
import network
import json
import random
import opensearchpy
from time import sleep


def main():
    users = []
    list_mac_addr = []
    list_ip_addr = []

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
    
    linux_data = generator_device(5, {"PC": "Linux"}, 2)
    windows_data = generator_device(5, {"PC": "Windows"}, 2)
    switch_data = generator_device(2, {"Switch": None}, 2)
    router_data = generator_device(2, {"Router": None}, 2)
    firewall_data = generator_device(1, {"Firewall": None}, 3)

    pc["users"] += linux_data["users"]
    pc["ip"] += linux_data["ip"]
    pc["mac"] += linux_data["mac"]

    pc["users"] += windows_data["users"]
    pc["ip"] += windows_data["ip"]
    pc["mac"] += windows_data["mac"]

    switch["users"] += switch_data["users"]
    switch["ip"] += switch_data["ip"]
    switch["mac"] += switch_data["mac"]

    router["users"] += router_data["users"]
    router["ip"] += router_data["ip"]
    router["mac"] += router_data["mac"]

    firewall["users"] += firewall_data["users"]
    firewall["ip"] += firewall_data["ip"]
    firewall["mac"] += firewall_data["mac"]

    list_ip_addr = pc["ip"] + switch["ip"] + router["ip"] + firewall["ip"]
    list_mac_addr = pc["mac"] + switch["mac"] + router["mac"] + firewall["mac"]

    client, index_name, index_mapping = network.initialization_opensearch()
    network.create_index_opensearch(client, index_name, index_mapping)

    all_users = pc["users"] + switch["users"] + router["users"] + firewall["users"]
    generator_protocols(client, index_name, all_users, list_ip_addr, list_mac_addr)



def generator_device(count_users: int, category: dict[str, str] | dict[str, None], number_network: int):
    users = []
    list_ip_addr = []
    list_mac_addr = []

    if category == {"PC": "Linux"}:
        for i in range(count_users):
            users.append(
                entity.PersonalComputerLinux(
                    hostname=f"PC-{i + 1}",
                    ip_addr=f"192.168.{number_network}.{i + 1}",
                    mac_addr=mac_addr_generator(),
                    category="PC",
                    log_format="syslog",
                    os="Linux",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                )
            )
            list_mac_addr.append(users[i].get_mac_addr())
            list_ip_addr.append(users[i].get_ip_addr())
        return {"users": users, "ip": list_ip_addr, "mac": list_mac_addr}

    elif category == {"PC": "Windows"}:
        for i in range(count_users):
            users.append(
                entity.PersonalComputerWindows(
                    hostname=f"PC-{i + 1}",
                    ip_addr=f"192.168.{number_network}.{i + 1}",
                    mac_addr=mac_addr_generator(),
                    category="PC",
                    log_format="syslog",
                    os="Windows",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            list_mac_addr.append(users[i].get_mac_addr())
            list_ip_addr.append(users[i].get_ip_addr())
        return {"users": users, "ip": list_ip_addr, "mac": list_mac_addr}

    elif category == {"Switch": None}:
        for i in range(count_users):
            users.append(
                entity.Switch(
                    hostname=f"SW-{i + 1}",
                    ip_addr=f"192.168.{number_network}.{i + 1}",
                    mac_addr=mac_addr_generator(),
                    category="Switch",
                    log_format="systemd",
                    os="IOS",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            list_mac_addr.append(users[i].get_mac_addr())
            list_ip_addr.append(users[i].get_ip_addr())
        return {"users": users, "ip": list_ip_addr, "mac": list_mac_addr}

    elif category == {"Router": None}:
        for i in range(count_users):
            users.append(
                entity.Router(
                    hostname=f"RT-{i + 1}",
                    ip_addr=f"192.168.{number_network}.{i + 1}",
                    mac_addr=mac_addr_generator(),
                    category="Router",
                    log_format="systemd",
                    os="IOS",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            list_mac_addr.append(users[i].get_mac_addr())
            list_ip_addr.append(users[i].get_ip_addr())
        return {"users": users, "ip": list_ip_addr, "mac": list_mac_addr}

    elif category == {"Firewall": None}:
        for i in range(count_users):
            users.append(
                entity.Firewall(
                    hostname=f"FW-{i + 1}",
                    ip_addr=f"192.168.{number_network}.{i + 1}",
                    mac_addr=mac_addr_generator(),
                    category="Firewall",
                    log_format="systemd",
                    os="IOS",
                    domain="telecom.technology",
                    asset_number=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                ))
            list_mac_addr.append(users[i].get_mac_addr())
            list_ip_addr.append(users[i].get_ip_addr())
        return {"users": users, "ip": list_ip_addr, "mac": list_mac_addr}

    else:
        return [], [], []



def generator_protocols(client, index_name, users, list_ip_addr, list_mac_addr):
    operations = []
    for i in range(500000):
        operations.append(random.randint(1, 21))

    for i in range(len(operations)):
        count_sec = random.uniform(0.1, 4)
        print(f"Пауза {round(count_sec, 0)} сек.")
        sleep(count_sec)
        user = random.choice(users)

        if type(user) == entity.PersonalComputerLinux or type(user) == entity.PersonalComputerWindows:
            print("Linux / Windows -> ", end="")
            if operations[i] == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_info_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_warning_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_crit_json(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.start_process_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.start_process_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.start_process_debug_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.open_file_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.open_file_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.open_file_crit_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.network_activity_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 11:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.network_activity_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 12:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.network_activity_debug_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 13:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.edit_policies_notice_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 14:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.edit_policies_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 15:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.edit_policies_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 16:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.remote_control_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 17:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.remote_control_warning_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 18:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.remote_control_alert_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 19:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.update_system_info_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 20:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.update_system_err_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 21:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.update_system_notice_json())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)

        if type(user) == entity.Switch:
            print("Switch -> ", end="")
            if operations[i] == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_status_port_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_status_port_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_status_port_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.learn_mac_addr_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.learn_mac_addr_warning(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.learn_mac_addr_debug(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.violation_port_security_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.violation_port_security_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.violation_port_security_alert())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.stp_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 11:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.stp_event_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 12:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.stp_event_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 13:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.duplex_error_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 14:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.duplex_error_err())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 15:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.duplex_error_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 16:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.vlan_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 17:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.vlan_event_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 18:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.vlan_event_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 19:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_802_1x_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 20:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_802_1x_warning(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 21:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_802_1x_alert(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)

        if type(user) == entity.Router:
            print("Router -> ", end="")
            if operations[i] == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_status_int_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_status_int_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_status_int_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_roadmap_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_roadmap_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_roadmap_alert())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.dynamic_routing_event_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.dynamic_routing_event_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.dynamic_routing_event_crit())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.acl_activity_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 11:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.acl_activity_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 12:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.acl_activity_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 13:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.nat_event_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 14:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.nat_event_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 15:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.nat_event_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 16:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.icmp_message_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 17:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.icmp_message_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 18:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.icmp_message_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 19:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.violation_traffic_info(list_mac_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 20:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.violation_traffic_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif operations[i] == 21:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.violation_traffic_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)

        if type(user) == entity.Firewall:
            print("Firewall -> ", end="")
            if (operations[i] % 10) == 1 or operations[i] == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.allow_traffic_info(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 2 or operations[i] == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.allow_traffic_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 3 or operations[i] == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.lock_traffic_warning(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 4 or operations[i] == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.lock_traffic_alert(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 5 or operations[i] == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.lock_traffic_debug())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 6 or operations[i] == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_session_info_connect(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 7 or operations[i] == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_session_info_breakup(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 8 or operations[i] == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.change_session_debug(list_ip_addr))
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 9 or operations[i] == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.vpn_tunnel_info())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)
            elif (operations[i] % 10) == 0 or operations[i] == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.vpn_tunnel_warning())
                network.insert_index_opensearch(client=client, index_name=index_name, index_data=logs)



def mac_addr_generator():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ':'.join(f'{byte:02x}' for byte in mac).upper()



def ui_console_menu():

        print("\t---\tMENU:\t---\t")
        print(
            "1. Создать персональный компьютер\n2. Создать коммутатор\n3. Создать роутер\n4. Создать межсетевой экран\n5. Начать генерацию\n6. Выход\n\tПример ->\tPC ( кол-во устройств ) ( Windows \ Linux ) ( номер подсети ) ")
        number = input().strip().split(" ")
        if number[0] == "6":
            exit()
        if number[0] == "1":
            if number[2].lower() in ["linux"]:
                linux_data = generator_device(int(number[1]), {"PC": "Linux"}, int(number[3]))
            if number[2].lower() in ["windows"]:
                windows_data = generator_device(int(number[1]), {"PC": "Windows"}, int(number[3]))
        if number[0] == "2":
            switch_data = generator_device(int(number[1]), {"Switch": None}, int(number[3]))
        if number[0] == "3":
            router_data = generator_device(int(number[1]), {"Router": None}, int(number[3]))
        if number[0] == "4":
            firewall_data = generator_device(int(number[1]), {"Firewall": None}, int(number[3]))


if __name__ == "__main__":
    main()
