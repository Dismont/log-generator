from tqdm import tqdm
import entity
import json
import random




def main():
    # basic_create()
    # print("BASIC CREATE")
    generator_device(5,{"PC":"Linux"},2)

def basic_create():
    list_ip_addr = []
    list_mac_addr = []

    pc1 = entity.PersonalComputer("PC-1","192.168.10.3","AB-CD-EF-12-13-45","System administrator","syslog","Linux","telecom.technology", "IN-124578")
    list_ip_addr.append(pc1.get_ip_addr())
    list_mac_addr.append(pc1.get_mac_addr())

    pc2 = entity.PersonalComputer("PC-2","192.168.10.4","AB-CD-EF-12-13-46","Sector Sell","syslog","Windows","telecom.technology", "IN-124579")
    list_ip_addr.append(pc2.get_ip_addr())
    list_mac_addr.append(pc2.get_mac_addr())

    sw1 = entity.Switch("SW-1","192.168.10.10","AB-CD-EF-12-45-78","Switch","Wazuh","IOS","telecom.technology", "IN-124580")
    list_ip_addr.append(sw1.get_ip_addr())
    list_mac_addr.append(sw1.get_mac_addr())

    rt1 = entity.Router("RT-1","192.168.10.15","AB-CD-EF-12-45-89","Router","Wazuh","IOS","telecom.technology", "IN-124582")
    list_ip_addr.append(rt1.get_ip_addr())
    list_mac_addr.append(rt1.get_mac_addr())

    fw1 = entity.FireWall("FW-1","192.168.10.27","AB-CD-EF-12-12-45","Firewall New Generation","Wazuh","IOS","telecom.technology", "IN-124589")
    list_ip_addr.append(fw1.get_ip_addr())
    list_mac_addr.append(fw1.get_mac_addr())

    print("IP: ",end=""),print(*list_ip_addr,sep=", ")
    print("MAC: ",end=""),print(*list_mac_addr,sep=", ")
    print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")



    print(pc1.show_info())
    print(pc2.show_info())
    print(sw1.show_info())

    # print(pc1.get_init())
    # print(pc1.get_attr())
    #
    # print(pc2.get_init())
    # print(pc2.get_attr())

    # print(pc1.get_timestamp())

    print(pc1.auth_info(list_ip_addr))
    print(pc1.auth_warning(list_ip_addr))
    print(pc1.auth_crit(list_ip_addr))

    print(json.dumps(pc1.auth_info_json(list_ip_addr), indent=4, ensure_ascii=False))
    print(json.dumps(pc1.auth_warning_json(list_ip_addr), indent=4, ensure_ascii=False))
    print(json.dumps(pc1.auth_crit_json(list_ip_addr), indent=4, ensure_ascii=False))

    print(pc1.start_process_info())
    print(pc1.start_process_warning())
    print(pc1.start_process_debug())

    print(json.dumps(pc1.start_process_info_json(), indent=4, ensure_ascii=False))
    print(json.dumps(pc1.start_process_warning_json(), indent=4, ensure_ascii=False))
    print(json.dumps(pc1.start_process_debug_json(), indent=4, ensure_ascii=False))

    print(pc1.open_file_info())
    print(pc1.open_file_warning())
    print(pc1.open_file_crit())

    print(pc1.network_activity_info())
    print(pc1.network_activity_warning())
    print(pc1.network_activity_debug())

    print(pc1.edit_policies_notice())
    print(pc1.edit_policies_warning())
    print(pc1.edit_policies_info())

    print(pc1.remote_control_info())
    print(pc1.remote_control_warning())
    print(pc1.remote_control_alert())

    print(pc1.update_system_info())
    print(pc1.update_system_err())
    print(pc1.update_system_notice())

    print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

    print(pc2.auth_info(list_ip_addr))
    print(pc2.auth_warning(list_ip_addr))
    print(pc2.auth_crit(list_ip_addr))

    print(pc2.start_process_info())
    print(pc2.start_process_warning())
    print(pc2.start_process_debug())

    print(pc2.open_file_info())
    print(pc2.open_file_warning())
    print(pc2.open_file_crit())

    print(pc2.network_activity_info())
    print(pc2.network_activity_warning())
    print(pc2.network_activity_debug())

    print(pc2.edit_policies_notice())
    print(pc2.edit_policies_warning())
    print(pc2.edit_policies_info())

    print(pc2.remote_control_info())
    print(pc2.remote_control_warning())
    print(pc2.remote_control_alert())

    print(pc2.update_system_info())
    print(pc2.update_system_err())
    print(pc2.update_system_notice())

    print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

    print(sw1.change_status_port_info())
    print(sw1.change_status_port_warning())
    print(sw1.change_status_port_crit())

    print(sw1.learn_mac_addr_info(list_mac_addr))
    print(sw1.learn_mac_addr_warning(list_mac_addr))
    print(sw1.learn_mac_addr_debug(list_mac_addr))

    print(sw1.violation_port_security_warning())
    print(sw1.violation_port_security_crit())
    print(sw1.violation_port_security_alert())

    print(sw1.stp_event_info())
    print(sw1.stp_event_crit())
    print(sw1.stp_event_warning())

    print(sw1.duplex_error_warning())
    print(sw1.duplex_error_err())
    print(sw1.duplex_error_crit())

    print(sw1.vlan_event_info())
    print(sw1.vlan_event_debug())
    print(sw1.vlan_event_warning())

    print(sw1.auth_802_1x_info(list_mac_addr))
    print(sw1.auth_802_1x_warning(list_mac_addr))
    print(sw1.auth_802_1x_alert(list_mac_addr))

    print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

    print(rt1.change_status_int_info())
    print(rt1.change_status_int_warning())
    print(rt1.change_status_int_crit())

    print(rt1.change_roadmap_info(list_ip_addr))
    print(rt1.change_roadmap_warning(list_ip_addr))
    print(rt1.change_roadmap_alert())

    print(rt1.dynamic_routing_event_info())
    print(rt1.dynamic_routing_event_warning(list_ip_addr))
    print(rt1.dynamic_routing_event_crit())

    print(rt1.acl_activity_info(list_ip_addr))
    print(rt1.acl_activity_warning(list_ip_addr))
    print(rt1.acl_activity_debug())

    print(rt1.nat_event_info(list_ip_addr))
    print(rt1.nat_event_warning(list_ip_addr))
    print(rt1.nat_event_debug(list_ip_addr))

    print(rt1.icmp_message_info(list_ip_addr))
    print(rt1.icmp_message_warning(list_ip_addr))
    print(rt1.icmp_message_debug(list_ip_addr))

    print(rt1.violation_traffic_info(list_ip_addr))
    print(rt1.violation_traffic_warning())
    print(rt1.violation_traffic_debug())

    print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

    print(fw1.allow_traffic_info(list_ip_addr))
    print(fw1.allow_traffic_debug(list_ip_addr))

    print(fw1.allow_traffic_info(list_ip_addr))
    print(fw1.allow_traffic_debug(list_ip_addr))
    print(fw1.allow_traffic_info(list_ip_addr))

    print(fw1.lock_traffic_warning(list_ip_addr))
    print(fw1.lock_traffic_alert(list_ip_addr))
    print(fw1.lock_traffic_debug())

    print(fw1.change_session_info_connect(list_ip_addr))
    print(fw1.change_session_info_breakup(list_ip_addr))
    print(fw1.change_session_debug(list_ip_addr))

def mac_addr_generator():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ':'.join(f'{byte:02x}' for byte in mac).upper()


def generator_device(count_users: int, category: dict[str,str], number_network: int):

    users = []
    list_ip_addr = []
    list_mac_addr = []
    match category:
        case {"PC": "Linux"}:
            for i in range(count_users):
                users.append(
                    entity.PersonalComputer(
                        hostname=f"PC-{i+1}",
                        ip_addr=f"192.168.{number_network}.{i+1}",
                        mac_addr=mac_addr_generator(),
                        role="PC",
                        log_format="syslog",
                        os="Linux",
                        domain="telecom.technology",
                        asset_tag=f"IN-{random.randint(1000,9999)}{random.randint(1000,9999)}"
                )
                )
                list_mac_addr.append(users[i].get_mac_addr())
                list_ip_addr.append(users[i].get_ip_addr())
            return {"users" : users, "ip" : list_ip_addr, "mac" : list_mac_addr}


        case {"PC": "Windows"}:
            for i in range(count_users):
                users.append(
                    entity.PersonalComputer(
                        hostname=f"PC-{i + 1}",
                        ip_addr=f"192.168.{number_network}.{i + 1}",
                        mac_addr=mac_addr_generator(),
                        role="PC",
                        log_format="syslog",
                        os="Windows",
                        domain="telecom.technology",
                        asset_tag=f"IN-{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
                    )
                )
                list_mac_addr.append(users[i].get_mac_addr())
                list_ip_addr.append(users[i].get_ip_addr())

            return {"users" : users, "ip" : list_ip_addr, "mac" : list_mac_addr}


        case _: return [], [], []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def generator_protocols(users, list_ip_addr, list_mac_addr):
    print(*list_mac_addr, sep=", ")
    print(*list_ip_addr, sep=", ")
    operations = []
    logs = []
    for i in range(20000):
        operations.append(random.randint(1, 21))
        for operation in operations:
            if operation == 1:
                logs.append(random.choice(users).auth_info_json(list_ip_addr))
            elif operation == 2:
                logs.append(random.choice(users).auth_warning_json(list_ip_addr))
            elif operation == 3:
                logs.append(random.choice(users).auth_crit_json(list_ip_addr))
            elif operation == 4:
                logs.append(random.choice(users).start_process_info_json())
            elif operation == 5:
                logs.append(random.choice(users).start_process_warning_json())
            elif operation == 6:
                logs.append(random.choice(users).start_process_debug_json())
            elif operation == 7:
                logs.append(random.choice(users).open_file_info_json())
            elif operation == 8:
                logs.append(random.choice(users).open_file_warning_json())
            elif operation == 9:
                logs.append(random.choice(users).open_file_crit_json())
            elif operation == 10:
                logs.append(random.choice(users).network_activity_info_json())
            elif operation == 11:
                logs.append(random.choice(users).network_activity_warning_json())
            elif operation == 12:
                logs.append(random.choice(users).network_activity_debug_json())
            elif operation == 13:
                logs.append(random.choice(users).edit_policies_notice_json())
            elif operation == 14:
                logs.append(random.choice(users).edit_policies_warning_json())
            elif operation == 15:
                logs.append(random.choice(users).edit_policies_info_json())
            elif operation == 16:
                logs.append(random.choice(users).remote_control_info_json())
            elif operation == 17:
                logs.append(random.choice(users).remote_control_warning_json())
            elif operation == 18:
                logs.append(random.choice(users).remote_control_alert_json())
            elif operation == 19:
                logs.append(random.choice(users).update_system_info_json())
            elif operation == 20:
                logs.append(random.choice(users).update_system_err_json())
            else:
                logs.append(random.choice(users).update_system_notice_json())

                if i % 5000 == 0 and i != 0:
                    with open ("log_basic.txt","a+") as file:
                        for log in logs:
                            file.write(f"{json.dumps(log, indent=4, ensure_ascii = False)}\n")
                    logs = []
                else:
                    print(i,end=", ")







if __name__ == "__main__":
        main()







