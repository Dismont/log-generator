from tqdm import tqdm
import entity
import json
import random
import opensearchpy
from time import sleep



def main():
    # basic_create()
    # print("BASIC CREATE")
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
    switch_data = generator_device(2,{"Switch":None}, 2)
    router_data = generator_device(2, {"Router": None}, 2)
    firewall_data = generator_device(1, {"Firewall": None}, 3)

    # Добавляем (расширяем списки)
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

    client = connect_opensearch()
    
    # client.indices.delete(index='siem_index')

    create_index_opensearch(client)
    all_users = pc["users"] + switch["users"] + router["users"] + firewall["users"]
    generator_protocols(client, all_users, list_ip_addr, list_mac_addr)

    # print(data)



def mac_addr_generator():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ':'.join(f'{byte:02x}' for byte in mac).upper()



def generator_device(count_users: int, category: dict[str,str] | dict [str, None], number_network: int):
    users = []
    list_ip_addr = []
    list_mac_addr = []
    match category:
        case {"PC": "Linux"}:
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
            return {"users" : users, "ip" : list_ip_addr, "mac" : list_mac_addr}


        case {"PC": "Windows"}:
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

        case {"Switch":None}:
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

        case {"Router": None}:
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

        case {"Firewall": None}:
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


        case _: return [], [], []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def generator_protocols(client, users, list_ip_addr, list_mac_addr):
    operations = []
    for i in range(500000):
        operations.append(random.randint(1, 21))

    for i in range(len(operations)):
        count_sec = random.uniform(0.1, 4)
        print(f"Спим {count_sec} сек.")
        sleep(count_sec)
        user = random.choice(users)

        if type(user) == entity.PersonalComputerLinux or type(user) == entity.PersonalComputerWindows:
            print("Linux / Windows -> ",end="")
            if operations[i] == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_info_json(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_warning_json(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.auth_crit_json(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.start_process_info_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.start_process_warning_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.start_process_debug_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.open_file_info_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.open_file_warning_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.open_file_crit_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs = (user.network_activity_info_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 11:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.network_activity_warning_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 12:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.network_activity_debug_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 13:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.edit_policies_notice_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 14:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.edit_policies_warning_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 15:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.edit_policies_info_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 16:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.remote_control_info_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 17:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.remote_control_warning_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 18:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.remote_control_alert_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 19:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.update_system_info_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 20:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.update_system_err_json())
                insert_data_opensearch(client, logs)
            elif operations[i] == 21:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.update_system_notice_json())
                insert_data_opensearch(client, logs)

        if type(user) == entity.Switch:
            print("Switch -> ",end="")
            if operations[i] == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_status_port_info())
                insert_data_opensearch(client, logs)
            elif operations[i] == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_status_port_warning())
                insert_data_opensearch(client, logs)
            elif operations[i] == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_status_port_crit())
                insert_data_opensearch(client, logs)
            elif operations[i] == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.learn_mac_addr_info(list_mac_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.learn_mac_addr_warning(list_mac_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.learn_mac_addr_debug(list_mac_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.violation_port_security_warning())
                insert_data_opensearch(client, logs)
            elif operations[i] == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.violation_port_security_crit())
                insert_data_opensearch(client, logs)
            elif operations[i] == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.violation_port_security_alert())
                insert_data_opensearch(client, logs)
            elif operations[i] == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.stp_event_info())
                insert_data_opensearch(client, logs)
            elif operations[i] == 11:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.stp_event_warning())
                insert_data_opensearch(client, logs)
            elif operations[i] == 12:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.stp_event_crit())
                insert_data_opensearch(client, logs)
            elif operations[i] == 13:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.duplex_error_warning())
                insert_data_opensearch(client, logs)
            elif operations[i] == 14:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.duplex_error_err())
                insert_data_opensearch(client, logs)
            elif operations[i] == 15:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.duplex_error_crit())
                insert_data_opensearch(client, logs)
            elif operations[i] == 16:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.vlan_event_info())
                insert_data_opensearch(client, logs)
            elif operations[i] == 17:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.vlan_event_warning())
                insert_data_opensearch(client, logs)
            elif operations[i] == 18:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.vlan_event_debug())
                insert_data_opensearch(client, logs)
            elif operations[i] == 19:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.auth_802_1x_info(list_mac_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 20:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.auth_802_1x_warning(list_mac_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 21:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.auth_802_1x_alert(list_mac_addr))
                insert_data_opensearch(client, logs)

        if type(user) == entity.Router:
            print("Router -> ", end="")
            if operations[i] == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_status_int_info())
                insert_data_opensearch(client, logs)
            elif operations[i] == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_status_int_warning())
                insert_data_opensearch(client, logs)
            elif operations[i] == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_status_int_crit())
                insert_data_opensearch(client, logs)
            elif operations[i] == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_roadmap_info(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_roadmap_warning(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_roadmap_alert())
                insert_data_opensearch(client, logs)
            elif operations[i] == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.dynamic_routing_event_info())
                insert_data_opensearch(client, logs)
            elif operations[i] == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.dynamic_routing_event_warning(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.dynamic_routing_event_crit())
                insert_data_opensearch(client, logs)
            elif operations[i] == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.acl_activity_info(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 11:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.acl_activity_warning(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 12:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.acl_activity_debug())
                insert_data_opensearch(client, logs)
            elif operations[i] == 13:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.nat_event_info(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 14:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.nat_event_warning(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 15:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.nat_event_debug(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 16:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.icmp_message_info(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 17:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.icmp_message_warning(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 18:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.icmp_message_debug(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 19:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.violation_traffic_info(list_mac_addr))
                insert_data_opensearch(client, logs)
            elif operations[i] == 20:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.violation_traffic_warning())
                insert_data_opensearch(client, logs)
            elif operations[i] == 21:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.violation_traffic_debug())
                insert_data_opensearch(client, logs)

        if type(user) == entity.Firewall:
            print("Firewall -> ", end="")
            if (operations[i] % 10) == 1 or operations[i]  == 1:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.allow_traffic_info(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 2 or operations[i]  == 2:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.allow_traffic_debug(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 3 or operations[i]  == 3:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.lock_traffic_warning(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 4 or operations[i]  == 4:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.lock_traffic_alert(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 5 or operations[i]  == 5:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.lock_traffic_debug())
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 6 or operations[i]  == 6:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_session_info_connect(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 7 or operations[i]  == 7:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_session_info_breakup(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 8 or operations[i]  == 8:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.change_session_debug(list_ip_addr))
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 9 or operations[i]  == 9:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.vpn_tunnel_info())
                insert_data_opensearch(client, logs)
            elif (operations[i] % 10) == 0 or operations[i]  == 10:
                print(f"{i}, {operations[i]} |", end=", ")
                logs=(user.vpn_tunnel_warning())
                insert_data_opensearch(client, logs)



def connect_opensearch():
    # Настройки подключения
    host = '192.168.245.134'
    port = 9200
    auth = ('admin', 'MySecret123@')  # Для базовой аутентификации (если включена)

    # Создание клиента
    client = opensearchpy.OpenSearch(
        hosts=[{'host': host, 'port': port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=False,  # Только для тестов! В продакшене — True
        ssl_show_warn=False
    )

    # Проверка подключения
    info = client.info()
    print(f"OpenSearch Info: {info}")
    return client



def create_index_opensearch(client):

    index_name = 'siem_index'

    # Опционально: задать настройки и маппинг
    # index_body = {
    #     "settings": {
    #         "index": {
    #             "number_of_shards": 1,
    #             "number_of_replicas": 0
    #         }
    #     },
    #     "mappings": {
    #         "properties": {
    #             "@timestamp": {
    #                 "type": "date",
    #                 "format": "strict_date_optional_time||epoch_millis"
    #             },
    #             "host": {
    #                 "properties": {
    #                     "hostname": {"type": "keyword"}
    #                 }
    #             },
    #             "process": {
    #                 "properties": {
    #                     "name": {"type": "keyword"},
    #                     "pid": {"type": "integer"}
    #                 }
    #             },
    #             "event": {
    #                 "properties": {
    #                     "action": {"type": "keyword"},
    #                     "category": {"type": "keyword"},
    #                     "type": {"type": "keyword"},
    #                     "outcome": {"type": "keyword"},
    #                     "severity": {"type": "integer"}
    #                 }
    #             },
    #             "user": {
    #                 "properties": {
    #                     "name": {"type": "keyword"}
    #                 }
    #             },
    #             "source": {
    #                 "properties": {
    #                     "ip": {"type": "ip"}
    #                 }
    #             }
    #         }
    #     }
    # }



    # Создаём индекс
    if not client.indices.exists(index=index_name):
        response = client.indices.create(index=index_name)
        print("Индекс создан:", response)

    else:
        print("Индекс уже существует")



def insert_data_opensearch(client, data):

    client.index(index='siem_index', body=data)
    print("Документ добавлен.")



if __name__ == "__main__":
        main()







