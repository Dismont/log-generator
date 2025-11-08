import random
from datetime import datetime, timezone


class Device:

    def __init__(self, hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain):
        self.hostname = hostname
        self.os = os
        self.category = category
        self.log_format = log_format
        self.asset_number = asset_number
        self.ip_addr = ip_addr
        self.mac_addr = mac_addr
        self.domain = domain

    def get_hostname(self):
        return self.hostname

    def get_os(self):
        return self.os

    def get_category(self):
        return self.category

    def get_asset_number(self):
        return self.asset_number

    def get_ip_addr(self):
        return self.ip_addr

    def get_mac_addr(self):
        return self.mac_addr

    @staticmethod
    def get_timestamp():
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        return timestamp


class PersonalComputerLinux(Device):

    def __init__(self, hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain):
        super().__init__(
            hostname,
            os,
            category,
            log_format,
            asset_number,
            ip_addr,
            mac_addr,
            domain)

        self.destination_ip = [
            "8.8.8.8",  # Google DNS
            "1.1.1.1",  # Cloudflare DNS
            "9.9.9.9",  # Quad9
            "142.250.185.206",  # Google
            "140.82.121.4",  # GitHub
            "104.16.132.229",  # Cloudflare (example.com)
            "40.126.35.10",  # Microsoft
            "17.253.144.10",  # Apple
            "13.32.187.123",  # Amazon
            "31.13.71.36",  # Facebook
            "104.244.42.1",  # Twitter/X
            "142.250.186.174",  # YouTube
            "91.198.174.192",  # Wikipedia
            "151.101.1.69",  # Stack Overflow
            "173.194.222.108",  # Gmail
            "52.100.160.10",  # Outlook
            "162.125.1.1",  # Dropbox
            "3.233.128.10",  # Zoom
            "34.102.136.180",  # Slack
            "13.107.246.10",  # Windows Update
            "91.189.91.83",  # Ubuntu
            "34.224.140.168",  # Docker Hub
            "104.16.23.35",  # NPM
            "151.101.193.223"  # PyPI
        ]
        self.software_attr = [
            {"bash": 1},  # FACILITY
            {"libreoffice": 1},
            {"yandex-stable": 1},
            {"thunderbird": 2},
            {"rsync": 1},
            {"python3": 16},
            {"konsole": 1},
            {"nautilus": 1},
            {"ssh": 8}
        ]
        self.users_attr = [
            "root",  # Суперпользователь
            "deamon",  # Управление демонами
            "bin",  # Владелец бинарников
            "sys",  # Системные логи и ядро
            "sync",  # Вледелец `sync`
            "nobody",  # Минимальные привилегии
            "lp",  # Печать
            "mail",  # Почтовая система
            "backup",  # Резервное копирование
            "uucp",  # Unix-to-Unix Copy
            "www-data",  # Веб-сервер
            f"user-{self.asset_number.replace('IN-', '')}",
            "auditd"
        ]
        self.software_files_attr = [
            "/bin/bash",
            "/usr/bin/libreoffice",
            "/usr/bin/yandex-browser-stable",
            "/usr/bin/thunderbird",
            "/usr/bin/rsync",
            "/usr/bin/python3",
            "/usr/bin/konsole",
            "/usr/bin/nautilus",
            "/usr/bin/ssh"
        ]
        self.system_files_attr = [
            "/var/log/syslog",
            "/var/log/messages",
            "/var/log/auth.log",
            "/var/log/kern.log",
            "/var/log/daemon.log",
            "/var/log/debug",
            "/var/log/mail.log",
            "/var/log/user.log",
            "/var/log/cron",
            "/var/log/boot.log",
            "/var/log/dpkg.log",
            "/var/log/apt/history.log",
            "/var/log/yum.log",
            "/var/log/audit/audit.log",
            "/var/log/journal/",
            "/var/log/nginx/access.log",
            "/var/log/nginx/error.log",
            "/var/log/apache2/access.log",
            "/var/log/apache2/error.log",
            "/var/log/mysql/error.log",
            "/var/log/postgresql/",
            "/var/log/redis/redis-server.log",
            "/var/log/samba/",
            "/var/log/Xorg.0.log",
        ]
        self.config_files_attr = [
            "/etc/passwd",
            "/etc/shadow",
            "/etc/group",
            "/etc/hosts",
            "/etc/resolv.conf",
            "/etc/fstab",
            "/etc/ssh/sshd_config",
            "/etc/ssh/ssh_host_rsa_key",
            "/etc/sudoers",
            "/etc/crontab",
            "/etc/cron.d/",
            "/etc/systemd/system/",
            "/etc/systemd/user/",
            "/etc/network/interfaces",
            "/etc/netplan/",
            "/etc/NetworkManager/",
            "/etc/security/"
        ]
        self.home_files_attr = [
            f"/home/user-{self.asset_number.replace('IN-', '')}/.bash_history",
            f"/home/user-{self.asset_number.replace('IN-', '')}/.ssh/id_rsa",
            f"/home/user-{self.asset_number.replace('IN-', '')}/.ssh/authorized_keys",
            f"/home/user-{self.asset_number.replace('IN-', '')}/.config/",
            f"/home/user-{self.asset_number.replace('IN-', '')}/.mozilla/firefox/",
            f"/home/user-{self.asset_number.replace('IN-', '')}/.cache/",
            f"/home/user-{self.asset_number.replace('IN-', '')}/Documents/",
            f"/home/user-{self.asset_number.replace('IN-', '')}/Downloads/",
            f"/home/user-{self.asset_number.replace('IN-', '')}/.local/share/applications/"
        ]
        self.tmp_files_attr = [
            "/tmp/",
            "/var/tmp/",
            "/run/",
            "/dev/shm/",
            f"/home/user-{self.asset_number.replace('IN-', '')}/.cache/"
        ]
        self.socket_files_attr = [
            "/run/systemd/private",
            "/run/dbus/system_bus_socket",
            "/var/run/",
            "/tmp/.X11-unix/"
        ]

    def auth_info_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "user_login",
                "category": "authentication",
                "type": ["connection", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}"
            },
            "source": {
                "ip": f"{random.choice(other_ips)}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def auth_warning_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "user_login",
                "category": "authentication",
                "type": ["connection", "failed"],
                "outcome": "failure",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}"
            },
            "source": {
                "ip": f"{random.choice(other_ips)}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def auth_crit_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "intrusion_attempt",
                "category": "intrusion_detection",
                "type": ["connection", "failed"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}"
            },
            "source": {
                "ip": f"{random.choice(other_ips)}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def start_process_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        all_files_attr = self.software_files_attr
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "process_started",
                "category": "process",
                "type": ["process", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": f"{random.choice(all_files_attr)}",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def start_process_warning_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        all_files_attr = self.software_files_attr
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "process_suspicious",
                "category": "process",
                "type": ["process", "stoped"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": f"{random.choice(all_files_attr)}",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def start_process_debug_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        all_files_attr = self.software_files_attr
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "debug_process",
                "category": "process",
                "type": ["process", "debug"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": f"{random.choice(all_files_attr)}",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def open_file_info_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "file_open",
                "category": "file",
                "type": ["file", "opened"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": f"{random.choice(all_files_attr)}"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def open_file_warning_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "file_access",
                "category": "file",
                "type": ["file", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": f"{random.choice(all_files_attr)}"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def open_file_crit_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "critical",
                "category": "file",
                "type": ["file", "broken"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": f"{random.choice(all_files_attr)}"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def network_activity_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "network_connection",
                "category": "network",
                "type": ["network", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": random.randint(8080, 25500),
                "user": f"user-{self.asset_number.replace('IN-', '')}",
                "executable": f"{app_name}",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": random.randint(8080, 25500),
            },
            "network": {
                "protocol": f"{random.choice(['tcp', 'udp'])}"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def network_activity_warning_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "network_connection_app",
                "category": "network",
                "type": ["network", "app_connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": random.randint(8080, 25500),
                "user": f"user-{self.asset_number.replace('IN-', '')}",
                "executable": f"{app_name}",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": random.randint(8080, 25500),
            },
            "network": {
                "protocol": f"{random.choice(['tcp', 'udp'])}"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def network_activity_debug_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "tcp_connection",
                "category": "network",
                "type": ["network", "tcp"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": random.randint(8080, 25500),
                "user": f"user-{self.asset_number.replace('IN-', '')}",
                "executable": f"{app_name}",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": random.randint(8080, 25500),
            },
            "network": {
                "protocol": f"{random.choice(['tcp', 'udp'])}"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def edit_policies_notice_json(self):
        app = "systemd"
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "applied_policy",
                "category": "settings",
                "type": ["policy", "info"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "systemd"
        }

    def edit_policies_warning_json(self):
        app = "systemd"
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "failed_policy",
                "category": "settings",
                "type": ["policy", "failed"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "systemd"
        }

    def edit_policies_info_json(self):
        app = "systemd"
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "reload_policy",
                "category": "settings",
                "type": ["policy", "reload"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "systemd"
        }

    def remote_control_info_json(self):
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "rdp_connection",
                "category": "remote_desktop_protocol",
                "type": ["rdp", "connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def remote_control_warning_json(self):
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "rdp_failed_login",
                "category": "remote_desktop_protocol",
                "type": ["rdp", "failed"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def remote_control_alert_json(self):
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "rdp_brute-force_detected",
                "category": "remote_desktop_protocol",
                "type": ["rdp", "attacked"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": 0,
                "user": f"{random.choice(self.users_attr)}",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def update_system_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "installation_package",
                "category": "update_system",
                "type": ["apt", "install"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": f"{app_name}",
                "size": "-"
            },
            "app": "-"
        }

    def update_system_err_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "failed_installation_package",
                "category": "update_system",
                "type": ["apt", "failed"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": f"{app_name}",
                "size": "-"
            },
            "app": "-"
        }

    def update_system_notice_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "security_update",
                "category": "update_system",
                "type": ["apt", "upgrade"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": f"{app_name}",
                "size": f"{random.randint(1000, 9999)}{random.randint(100, 999)} KB"
            },
            "app": "-"
        }


class PersonalComputerWindows(Device):

    def __init__(self, hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain):
        super().__init__(
            hostname,
            os,
            category,
            log_format,
            asset_number,
            ip_addr,
            mac_addr,
            domain)

        self.destination_ip = [
            "8.8.8.8",  # Google DNS
            "1.1.1.1",  # Cloudflare DNS
            "9.9.9.9",  # Quad9
            "142.250.185.206",  # Google
            "140.82.121.4",  # GitHub
            "104.16.132.229",  # Cloudflare (example.com)
            "40.126.35.10",  # Microsoft
            "17.253.144.10",  # Apple
            "13.32.187.123",  # Amazon
            "31.13.71.36",  # Facebook
            "104.244.42.1",  # Twitter/X
            "142.250.186.174",  # YouTube
            "91.198.174.192",  # Wikipedia
            "151.101.1.69",  # Stack Overflow
            "173.194.222.108",  # Gmail
            "52.100.160.10",  # Outlook
            "162.125.1.1",  # Dropbox
            "3.233.128.10",  # Zoom
            "34.102.136.180",  # Slack
            "13.107.246.10",  # Windows Update
            "91.189.91.83",  # Ubuntu
            "34.224.140.168",  # Docker Hub
            "104.16.23.35",  # NPM
            "151.101.193.223"  # PyPI
        ]
        self.software_attr = [
            {"explorer.exe": 1},  # user — стандартный UI
            {"yandex.exe": 1},  # user — браузер
            {"powershell.exe": 16},  # local0 — административная оболочка
            {"cmd.exe": 16},  # local0 — командная строка
            {"notepad.exe": 1},  # user — текстовый редактор
            {"HxCalendarAppImm.exe": 2},  # mail — календарь/почта Microsoft
            {"Acrobat.exe": 1},  # user — PDF-ридер
            {"7-zip.exe": 1},  # user — архиватор
            {"MsMpEng.exe": 17},  # local1 — антивирус (безопасность)
            {"winword.exe": 1},  # user — Word
            {"excel.exe": 1},  # user — Excel
            {"code.exe": 1},  # user — VS Code
            {"vlc.exe": 1},  # user — медиаплеер
            {"audiodg.exe": 1},  # user — системный аудио-процесс
        ]
        self.users_attr = [
            "NT AUTHORITY SYSTEM",
            "NT AUTHORITY LOCAL SERVICE",
            "NT AUTHORITY NETWORK SERVICE",
            "Administrator",
            "Guest",
            "DefaultAccount",
            "WDAGUtilityAccount",
            "ANONYMOUS LOGON",
            f"user-{self.asset_number.replace('IN-', '')}"
        ]
        self.software_files_attr = [
            "C:\\Windows\\explorer.exe",
            "C:\\Users\\{user}\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe",
            "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
            "C:\\Windows\\System32\\cmd.exe",
            "C:\\Windows\\System32\\notepad.exe",
            "C:\\Windows\\System32\\HxCalendarAppImm.exe",
            "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe",
            "C:\\Program Files\\7-Zip\\7zFM.exe",
            "C:\\Program Files\\Windows Defender\\MsMpEng.exe",
            "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
            "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
            "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
        ]
        self.system_files_attr = [
            "C:\\Windows\\System32\\winevt\\Logs\\Application.evtx",
            "C:\\Windows\\System32\\winevt\\Logs\\Security.evtx",
            "C:\\Windows\\System32\\winevt\\Logs\\System.evtx",
            "C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-PowerShell%4Operational.evtx",
            "C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-Sysmon%4Operational.evtx",
            "C:\\Windows\\System32\\LogFiles\\",
            "C:\\Windows\\System32\\LogFiles\\W3SVC1\\",
            "C:\\Windows\\Temp\\",
            "C:\\Windows\\debug\\NetSetup.LOG",
            "C:\\Windows\\Panther\\setupact.log",
            "C:\\Windows\\INF\\setupapi.dev.log",
            "C:\\ProgramData\\Microsoft\\Windows Defender\\Support\\MPLog-*.log",
            "C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportArchive\\",
            "C:\\Windows\\System32\\config\\AppEvent.Evt",  # (устаревший, XP/2003)
            "C:\\Windows\\System32\\config\\SecEvent.Evt"  # (устаревший)
        ]
        self.config_files_attr = [
            "C:\\Windows\\System32\\drivers\\etc\\hosts",
            "C:\\Windows\\System32\\config\\SAM",
            "C:\\Windows\\System32\\config\\SYSTEM",
            "C:\\Windows\\System32\\config\\SOFTWARE",
            "C:\\Windows\\System32\\config\\SECURITY",
            "C:\\Windows\\Prefetch\\",
            "C:\\Windows\\Tasks\\",
            "C:\\Windows\\SchedLgU.txt",
            "C:\\boot.ini",  # (устаревший, до Windows 7)
            "C:\\Windows\\System32\\GroupPolicy\\",
            "C:\\Windows\\System32\\sru\\SRUDB.dat",  # Diagnostic Tracking
            "C:\\Windows\\System32\\LicenseManager\\",
            "C:\\Windows\\System32\\spool\\drivers\\",
            "C:\\Windows\\System32\\wbem\\Repository\\",
            "C:\\Windows\\System32\\catroot2\\"
        ]
        self.home_files_attr = [
            "C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt",
            "C:\\Users\\{user}\\NTUSER.DAT",
            "C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\",
            "C:\\Users\\{user}\\Documents\\",
            "C:\\Users\\{user}\\Downloads\\",
            "C:\\Users\\{user}\\Desktop\\",
            "C:\\Users\\{user}\\AppData\\Local\\Temp\\",
            "C:\\Users\\{user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\",
            "C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History",
            "C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History",
            "C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\",
            "C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\",
            "C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Windows\\INetCache\\",
            "C:\\Users\\{user}\\.ssh\\id_rsa",  # если используется OpenSSH
            "C:\\Users\\{user}\\.ssh\\authorized_keys"
        ]
        self.tmp_files_attr = [
            "C:\\Windows\\Temp\\",
            "C:\\Users\\{user}\\AppData\\Local\\Temp\\",
            "%TEMP%",
            "C:\\Windows\\Prefetch\\",
            "C:\\Windows\\SoftwareDistribution\\Download\\"
        ]
        self.socket_files_attr = []

    def auth_info_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "user_login",
                "category": "authentication",
                "type": ["connection", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}"
            },
            "source": {
                "ip": f"{random.choice(other_ips)}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def auth_warning_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "user_login",
                "category": "authentication",
                "type": ["connection", "failed"],
                "outcome": "failure",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}"
            },
            "source": {
                "ip": f"{random.choice(other_ips)}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def auth_crit_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "intrusion_attempt",
                "category": "intrusion_detection",
                "type": ["connection", "failed"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}"
            },
            "source": {
                "ip": f"{random.choice(other_ips)}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def start_process_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        all_files_attr = self.software_files_attr
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "process_started",
                "category": "process",
                "type": ["process", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": f"{random.choice(all_files_attr)}",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def start_process_warning_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        all_files_attr = self.software_files_attr
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "process_suspicious",
                "category": "process",
                "type": ["process", "stoped"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": f"{random.choice(all_files_attr)}",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def start_process_debug_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        all_files_attr = self.software_files_attr
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "debug_process",
                "category": "process",
                "type": ["process", "debug"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"{random.choice(self.users_attr)}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": f"{random.choice(all_files_attr)}",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def open_file_info_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "file_open",
                "category": "file",
                "type": ["file", "opened"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": f"{random.choice(all_files_attr)}"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def open_file_warning_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "file_access",
                "category": "file",
                "type": ["file", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": f"{random.choice(all_files_attr)}"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def open_file_crit_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "critical",
                "category": "file",
                "type": ["file", "broken"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": f"{random.choice(all_files_attr)}"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def network_activity_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "network_connection",
                "category": "network",
                "type": ["network", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": random.randint(8080, 25500),
                "user": f"user-{self.asset_number.replace('IN-', '')}",
                "executable": f"{app_name}",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": random.randint(8080, 25500),
            },
            "network": {
                "protocol": f"{random.choice(['tcp', 'udp'])}"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def network_activity_warning_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "network_connection_app",
                "category": "network",
                "type": ["network", "app_connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": random.randint(8080, 25500),
                "user": f"user-{self.asset_number.replace('IN-', '')}",
                "executable": f"{app_name}",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": random.randint(8080, 25500),
            },
            "network": {
                "protocol": f"{random.choice(['tcp', 'udp'])}"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def network_activity_debug_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app_name}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "tcp_connection",
                "category": "network",
                "type": ["network", "tcp"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}"
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": random.randint(8080, 25500),
                "user": f"user-{self.asset_number.replace('IN-', '')}",
                "executable": f"{app_name}",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": random.randint(8080, 25500),
            },
            "network": {
                "protocol": f"{random.choice(['tcp', 'udp'])}"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def edit_policies_notice_json(self):
        app = "GroupPolicy"
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "applied_policy",
                "category": "settings",
                "type": ["policy", "info"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "systemd"
        }

    def edit_policies_warning_json(self):
        app = "GroupPolicy"
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "failed_policy",
                "category": "settings",
                "type": ["policy", "failed"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "systemd"
        }

    def edit_policies_info_json(self):
        app = "GroupPolicy"
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": f"{app}",
                "pid": random.randint(115, 1999)
            },
            "event": {
                "action": "reload_policy",
                "category": "settings",
                "type": ["policy", "reload"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "systemd"
        }

    def remote_control_info_json(self):
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "rdp_connection",
                "category": "remote_desktop_protocol",
                "type": ["rdp", "connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def remote_control_warning_json(self):
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "rdp_failed_login",
                "category": "remote_desktop_protocol",
                "type": ["rdp", "failed"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def remote_control_alert_json(self):
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "rdp_brute-force_detected",
                "category": "remote_desktop_protocol",
                "type": ["rdp", "attacked"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": f"{self.get_ip_addr()}",
                "port": 0,
                "user": f"{random.choice(self.users_attr)}",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": f"{random.choice(self.destination_ip)}",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "-",
                "size": "-"
            },
            "app": "-"
        }

    def update_system_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "installation_package",
                "category": "update_system",
                "type": ["WindowsUpdate", "install"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": f"{app_name}",
                "size": "-"
            },
            "app": "-"
        }

    def update_system_err_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "failed_installation_package",
                "category": "update_system",
                "type": ["WindowsUpdate", "failed"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": f"{app_name}",
                "size": "-"
            },
            "app": "-"
        }

    def update_system_notice_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        return {
            "@timestamp": f"{self.get_timestamp()}",
            "hostname": f"{self.hostname}",
            "process": {
                "name": "TermService",
                "pid": 0
            },
            "event": {
                "action": "security_update",
                "category": "update_system",
                "type": ["WindowsUpdate", "upgrade"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": f"user-{self.asset_number.replace('IN-', '')}",
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "-"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": f"{app_name}",
                "size": f"{random.randint(1000, 9999)}{random.randint(100, 999)} KB"
            },
            "app": "-"
        }


class Switch(Device):

    def __init__(self, hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain):
        super().__init__(
            hostname,
            os,
            category,
            log_format,
            asset_number,
            ip_addr,
            mac_addr,
            domain)

        self.destination_ip = [
            "8.8.8.8",  # Google DNS
            "1.1.1.1",  # Cloudflare DNS
            "9.9.9.9",  # Quad9
            "142.250.185.206",  # Google
            "140.82.121.4",  # GitHub
            "104.16.132.229",  # Cloudflare (example.com)
            "40.126.35.10",  # Microsoft
            "17.253.144.10",  # Apple
            "13.32.187.123",  # Amazon
            "31.13.71.36",  # Facebook
            "104.244.42.1",  # Twitter/X
            "142.250.186.174",  # YouTube
            "91.198.174.192",  # Wikipedia
            "151.101.1.69",  # Stack Overflow
            "173.194.222.108",  # Gmail
            "52.100.160.10",  # Outlook
            "162.125.1.1",  # Dropbox
            "3.233.128.10",  # Zoom
            "34.102.136.180",  # Slack
            "13.107.246.10",  # Windows Update
            "91.189.91.83",  # Ubuntu
            "34.224.140.168",  # Docker Hub
            "104.16.23.35",  # NPM
            "151.101.193.223"  # PyPI
        ]
        self.port = [
            "Fa1/1",
            "Fa1/2",
            "Fa1/3",
            "Fa1/4",
            "Fa1/5",
            "Fa1/6",
            "Fa1/7",
            "Fa1/8",
            "Fa1/9",
            "Fa1/10",
            "Fa1/11",
            "Fa1/12",
            "Fa1/13",
            "Fa1/14",
            "Fa1/15",
            "Fa1/16",
            "Fa1/17",
            "Fa1/18",
            "Fa1/19",
            "Fa1/20",
            "Fa1/21",
            "Fa1/22",
            "Fa1/23",
            "Fa1/24",
            "Fa1/25",
            "Fa1/26",
            "Fa1/27",
            "Fa1/28",
            "Fa1/29",
            "Fa1/30",
            "Fa1/31",
            "Fa1/32",
            "Fa1/33",
            "Fa1/34",
            "Fa1/35",
            "Fa1/36",
            "Fa1/37",
            "Fa1/38",
            "Fa1/39",
            "Fa1/40",
            "Fa1/41",
            "Fa1/42",
            "Fa1/43",
            "Fa1/44",
            "Fa1/45",
            "Fa1/46",
            "Fa1/47",
            "Fa1/48",
            "Gi1/0/0",
            "Gi1/0/1",
            "Gi1/0/2",
            "Gi1/0/3"
        ]

    def change_status_port_info(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "LINK-UPDOWN",
                "pid": 1
            },
            "event": {
                "action": f"Interface {port} changed state to up",
                "category": "network",
                "type": ["change", "info"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def change_status_port_warning(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "LINK-FLAP",
                "pid": 1
            },
            "event": {
                "action": f"Interface {port} flapping",
                "category": "network",
                "type": ["change", "warning"],
                "outcome": "success",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def change_status_port_crit(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "HWIC-PORT_FAIL",
                "pid": 1
            },
            "event": {
                "action": f"Hardware failure on {port}",
                "category": "network",
                "type": ["error", "failure"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def learn_mac_addr_info(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        mac_addr = random.choice(other_mac)
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "MAC-LEARN",
                "pid": 1
            },
            "event": {
                "action": f"MAC {mac_addr} learned on {port}",
                "category": "network",
                "type": ["info", "change"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def learn_mac_addr_warning(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        mac_addr = random.choice(other_mac)
        from_port = random.choice(self.port)
        to_port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "MAC-MOVE",
                "pid": 1
            },
            "event": {
                "action": f"MAC {mac_addr} move from {from_port} to {to_port}",
                "category": "network",
                "type": ["change", "warning"],
                "outcome": "success",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def learn_mac_addr_debug(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        mac_addr = random.choice(other_mac)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "MAC-TABLE",
                "pid": 1
            },
            "event": {
                "action": f"MAC table entry added {mac_addr}",
                "category": "network",
                "type": ["info", "debug"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def violation_port_security_warning(self):
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "PORTSEC-VIOLATION",
                "pid": 1
            },
            "event": {
                "action": f"Security violation on {port}",
                "category": "network",
                "type": ["warning", "security"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def violation_port_security_crit(self):
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "PORTSEC-CAM_FLOOD",
                "pid": 1
            },
            "event": {
                "action": "CAM table overflow attack detected",
                "category": "network",
                "type": ["security", "attack"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def violation_port_security_alert(self):
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "SECURITY-COMPROMISE",
                "pid": 1
            },
            "event": {
                "action": "Unauthorized device connected",
                "category": "network",
                "type": ["security", "alert"],
                "outcome": "failure",
                "severity": 1
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def stp_event_info(self):
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "STP-PORTSTATE",
                "pid": 1
            },
            "event": {
                "action": f"Port {port} to forwarding",
                "category": "network",
                "type": ["info", "change"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def stp_event_warning(self):
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "STP-TOPOLOGY_CHANGE",
                "pid": 1
            },
            "event": {
                "action": "Topology change detected",
                "category": "network",
                "type": ["warning", "change"],
                "outcome": "success",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def stp_event_crit(self):
        vlan = random.randint(2, 19)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "STP-LOOP_DETECTED",
                "pid": 1
            },
            "event": {
                "action": f"Network loop detected on VLAN {vlan}",
                "category": "network",
                "type": ["error", "critical"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def duplex_error_warning(self):
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "INTERFACE-CRC",
                "pid": 1
            },
            "event": {
                "action": f"CRC errors on {port}",
                "category": "network",
                "type": ["warning", "error"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def duplex_error_err(self):
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "PHY-DUPLEX_MISMATCH",
                "pid": 1
            },
            "event": {
                "action": f"Duplex mismatch on {port}",
                "category": "network",
                "type": ["error", "failure"],
                "outcome": "failure",
                "severity": 3
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def duplex_error_crit(self):
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "HWIC-HARDWARE_ERR",
                "pid": 1
            },
            "event": {
                "action": f"Physical layer failure on {port}",
                "category": "network",
                "type": ["error", "critical"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def vlan_event_info(self):
        port = random.choice(self.port)
        vlan = random.randint(2, 19)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "VLAN-ASSIGN",
                "pid": 1
            },
            "event": {
                "action": f"Port {port} assigned to VLAN {vlan}",
                "category": "network",
                "type": ["info", "change"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def vlan_event_warning(self):
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "VLAN-NATIVE_MISMATCH",
                "pid": 1
            },
            "event": {
                "action": f"Native VLAN mismatch on {port}",
                "category": "network",
                "type": ["warning", "misconfiguration"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def vlan_event_debug(self):
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "VLAN-DEBUG",
                "pid": 1
            },
            "event": {
                "action": f"VLAN membership updated for {port}",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def auth_802_1x_info(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        mac_addr = random.choice(other_mac)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "DOT1X-SUCCESS",
                "pid": 1
            },
            "event": {
                "action": f"Auth succeeded for MAC {mac_addr}",
                "category": "network",
                "type": ["info", "authentication"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def auth_802_1x_warning(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        mac_addr = random.choice(other_mac)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "DOT1X-FAIL",
                "pid": 1
            },
            "event": {
                "action": f"Auth failed for MAC {mac_addr}",
                "category": "network",
                "type": ["warning", "authentication"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }

    def auth_802_1x_alert(self, list_mac_addr):
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "DOT1X-ATTACK",
                "pid": 1
            },
            "event": {
                "action": "EAPOL flood attack detected",
                "category": "network",
                "type": ["alert", "attack"],
                "outcome": "failure",
                "severity": 1
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ethernet"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "network-device"
        }


class Router(Device):

    def __init__(self, hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain):
        super().__init__(
            hostname,
            os,
            category,
            log_format,
            asset_number,
            ip_addr,
            mac_addr,
            domain)

        self.destination_ip = [
            "8.8.8.8",  # Google DNS
            "1.1.1.1",  # Cloudflare DNS
            "9.9.9.9",  # Quad9
            "142.250.185.206",  # Google
            "140.82.121.4",  # GitHub
            "104.16.132.229",  # Cloudflare (example.com)
            "40.126.35.10",  # Microsoft
            "17.253.144.10",  # Apple
            "13.32.187.123",  # Amazon
            "31.13.71.36",  # Facebook
            "104.244.42.1",  # Twitter/X
            "142.250.186.174",  # YouTube
            "91.198.174.192",  # Wikipedia
            "151.101.1.69",  # Stack Overflow
            "173.194.222.108",  # Gmail
            "52.100.160.10",  # Outlook
            "162.125.1.1",  # Dropbox
            "3.233.128.10",  # Zoom
            "34.102.136.180",  # Slack
            "13.107.246.10",  # Windows Update
            "91.189.91.83",  # Ubuntu
            "34.224.140.168",  # Docker Hub
            "104.16.23.35",  # NPM
            "151.101.193.223"  # PyPI
        ]
        self.port = [
            "Gi1/0/0",
            "Gi1/0/1",
            "Gi1/0/2",
            "Gi1/0/3"
        ]

    def change_status_int_info(self):
        interface = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "LINEPROTO-UPDOWN",
                "pid": 1
            },
            "event": {
                "action": f"{interface} changed state to up",
                "category": "network",
                "type": ["info", "change"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def change_status_int_warning(self):
        interface = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "INTERFACE-FLAP",
                "pid": 1
            },
            "event": {
                "action": f"{interface} flapping",
                "category": "network",
                "type": ["warning", "change"],
                "outcome": "success",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def change_status_int_crit(self):
        interface = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "HWIC-LINK_FAIL",
                "pid": 1
            },
            "event": {
                "action": f"Carrier loss on {interface}",
                "category": "network",
                "type": ["error", "critical"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def change_roadmap_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        route = random.choice(self.destination_ip + other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "IP-ROUTE",
                "pid": 1
            },
            "event": {
                "action": f"Route {route} added",
                "category": "network",
                "type": ["info", "change"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def change_roadmap_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        route = random.choice(self.destination_ip + other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "IP-ROUTE_FLAP",
                "pid": 1
            },
            "event": {
                "action": f"Route {route} flapping",
                "category": "network",
                "type": ["warning", "change"],
                "outcome": "success",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def change_roadmap_alert(self):
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "IP-ROUTING_LOSS",
                "pid": 1
            },
            "event": {
                "action": "All default routes lost",
                "category": "network",
                "type": ["alert", "failure"],
                "outcome": "failure",
                "severity": 1
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def dynamic_routing_event_info(self):
        neighbor = random.choice(self.destination_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "OSPF-ADJCHG",
                "pid": 1
            },
            "event": {
                "action": f"Nbr {neighbor} from DOWN to FULL",
                "category": "network",
                "type": ["info", "change"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ospf"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def dynamic_routing_event_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        neighbor = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "BGP-ADJCHANGE",
                "pid": 1
            },
            "event": {
                "action": f"Neighbor {neighbor} Down",
                "category": "network",
                "type": ["warning", "failure"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "bgp"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def dynamic_routing_event_crit(self):
        interface = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "OSPF-PROTOCOL_ERR",
                "pid": 1
            },
            "event": {
                "action": f"OSPF checksum error on {interface}",
                "category": "network",
                "type": ["error", "critical"],
                "outcome": "failure",
                "severity": 2
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ospf"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def acl_activity_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(other_ip)
        dst_ip = random.choice(self.destination_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ACL-PERMIT",
                "pid": 1
            },
            "event": {
                "action": f"Permitted tcp from {src_ip} to {dst_ip}",
                "category": "network",
                "type": ["info", "access"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": 0
            },
            "network": {
                "protocol": "tcp"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def acl_activity_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(self.destination_ip)
        dst_ip = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ACL-DENIED",
                "pid": 1
            },
            "event": {
                "action": f"Denied tcp from {src_ip} to {dst_ip}",
                "category": "network",
                "type": ["warning", "access"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": 0
            },
            "network": {
                "protocol": "tcp"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def acl_activity_debug(self):
        rule_id = random.randint(100, 187)
        protocol = random.choice(['tcp', 'udp'])
        src = random.choice(self.port + ['any'])
        dst = random.choice(self.port + ['any'])
        port = random.choice([20, 21, 22, 23, 25, 53, 80, 8080, 110, 135, 143, 443, 445, 993, 9600, 9200, 3306, 5432])

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ACL-MATCH",
                "pid": 1
            },
            "event": {
                "action": f"Matched rule {rule_id}: permit {protocol} {src} {dst} eq {port}",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": protocol
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def nat_event_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(other_ip)
        translated_ip = random.choice(self.destination_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "NAT-ADDR",
                "pid": 1
            },
            "event": {
                "action": f"Translated {src_ip} to {translated_ip}",
                "category": "network",
                "type": ["info", "translation"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": translated_ip,
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def nat_event_warning(self, list_ip_addr):
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "NAT-POOL_EXHAUSTED",
                "pid": 1
            },
            "event": {
                "action": "NAT pool exhausted",
                "category": "network",
                "type": ["warning", "resource"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def nat_event_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(other_ip)
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(100, 65500)
        dst_port = random.randint(100, 65500)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "NAT-DEBUG",
                "pid": 1
            },
            "event": {
                "action": f"NAT entry created: {src_ip}:{src_port} to {dst_ip}:{dst_port}",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": src_port,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def icmp_message_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        dst_ip = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ICMP-ECHO",
                "pid": 1
            },
            "event": {
                "action": f"Echo reply sent to {dst_ip}",
                "category": "network",
                "type": ["info", "communication"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": 0
            },
            "network": {
                "protocol": "icmp"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def icmp_message_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        dst_ip = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ICMP-DSTUNREACH",
                "pid": 1
            },
            "event": {
                "action": f"Destination {dst_ip} unreachable",
                "category": "network",
                "type": ["warning", "error"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": 0
            },
            "network": {
                "protocol": "icmp"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def icmp_message_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(other_ip)
        icmp_type = random.randint(3, 12)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ICMP-DEBUG",
                "pid": 1
            },
            "event": {
                "action": f"Received ICMP type {icmp_type} from {src_ip}",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "icmp"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def violation_traffic_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(other_ip)
        traffic_class = random.choice(['VOICE', 'VIDEO CONF', 'BUSINESS-DATA', 'EFFORT'])

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "QOS-CLASSIFIED",
                "pid": 1
            },
            "event": {
                "action": f"Traffic from {src_ip} classified as {traffic_class}",
                "category": "network",
                "type": ["info", "classification"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def violation_traffic_warning(self):
        interface = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "QOS-RATE_EXCEEDED",
                "pid": 1
            },
            "event": {
                "action": f"Rate limit exceeded on {interface}",
                "category": "network",
                "type": ["warning", "resource"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }

    def violation_traffic_debug(self):
        marking = random.choice(['DSCP', 'COS'])

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "QOS-DEBUG",
                "pid": 1
            },
            "event": {
                "action": f"Packet marked with {marking}",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "router"
        }


class Firewall(Device):

    def __init__(self, hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain):
        super().__init__(
            hostname,
            os,
            category,
            log_format,
            asset_number,
            ip_addr,
            mac_addr,
            domain)

        self.destination_ip = [
            "8.8.8.8",  # Google DNS
            "1.1.1.1",  # Cloudflare DNS
            "9.9.9.9",  # Quad9
            "142.250.185.206",  # Google
            "140.82.121.4",  # GitHub
            "104.16.132.229",  # Cloudflare (example.com)
            "40.126.35.10",  # Microsoft
            "17.253.144.10",  # Apple
            "13.32.187.123",  # Amazon
            "31.13.71.36",  # Facebook
            "104.244.42.1",  # Twitter/X
            "142.250.186.174",  # YouTube
            "91.198.174.192",  # Wikipedia
            "151.101.1.69",  # Stack Overflow
            "173.194.222.108",  # Gmail
            "52.100.160.10",  # Outlook
            "162.125.1.1",  # Dropbox
            "3.233.128.10",  # Zoom
            "34.102.136.180",  # Slack
            "13.107.246.10",  # Windows Update
            "91.189.91.83",  # Ubuntu
            "34.224.140.168",  # Docker Hub
            "104.16.23.35",  # NPM
            "151.101.193.223"  # PyPI
        ]
        self.port = [
            "Gi1/0/0",
            "Gi1/0/1",
            "Gi1/0/2",
            "Gi1/0/3"
        ]

    def allow_traffic_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(self.destination_ip)
        dst_ip = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ASA-302013",
                "pid": 1
            },
            "event": {
                "action": f"Built TCP connection for outside: {src_ip} to inside: {dst_ip}",
                "category": "network",
                "type": ["info", "connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": 0
            },
            "network": {
                "protocol": "tcp"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def allow_traffic_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(self.destination_ip)
        dst_ip = random.choice(other_ip)
        app_proto = random.choice(['ssh', 'ssl', 'tls', 'http', 'telnet'])

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "PAN-SESSION",
                "pid": 1
            },
            "event": {
                "action": f"Session created: src={src_ip}, dst={dst_ip}, app={app_proto}",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": 0
            },
            "network": {
                "protocol": app_proto
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def lock_traffic_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        protocol = random.choice(['tcp', 'udp'])
        src_ip = random.choice(self.destination_ip)
        dst_ip = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ASA-106015",
                "pid": 1
            },
            "event": {
                "action": f"Deny {protocol} src outside:{src_ip}, dst inside:{dst_ip}",
                "category": "network",
                "type": ["warning", "access"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": src_ip,
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": dst_ip,
                "port": 0
            },
            "network": {
                "protocol": protocol
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def lock_traffic_alert(self, list_ip_addr):
        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "PAN-THREAT",
                "pid": 1
            },
            "event": {
                "action": "Critical threat: Exploit attempt blocked",
                "category": "network",
                "type": ["alert", "security"],
                "outcome": "success",
                "severity": 1
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def lock_traffic_debug(self):
        rule_app = random.choice(['ssh', 'ssl', 'tls', 'http', 'telnet'])

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "FW-RULE_MATCH",
                "pid": 1
            },
            "event": {
                "action": f"Matched rule 'block-external-{rule_app}'",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": rule_app
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def change_session_info_connect(self, list_ip_addr):
        protocol = random.choice(['TCP', 'UDP'])
        conn_id = random.randint(1000, 20000)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ASA-6-302013",
                "pid": 1
            },
            "event": {
                "action": f"Built {protocol} connection {conn_id}",
                "category": "network",
                "type": ["info", "connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": protocol.lower()
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def change_session_info_breakup(self, list_ip_addr):
        protocol = random.choice(['TCP', 'UDP'])
        conn_id = random.randint(1000, 20000)
        duration = random.randint(60, 600)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "ASA-6-302014",
                "pid": 1
            },
            "event": {
                "action": f"Teardown {protocol} connection {conn_id} duration {duration}sec",
                "category": "network",
                "type": ["info", "connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": protocol.lower()
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def change_session_debug(self, list_ip_addr):
        bytes_in = random.randint(10000, 200000)
        bytes_out = random.randint(10000, 200000)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "FW-SESSION",
                "pid": 1
            },
            "event": {
                "action": f"Session stats: bytes_in={bytes_in}, bytes_out= {bytes_out}",
                "category": "network",
                "type": ["debug", "info"],
                "outcome": "success",
                "severity": 7
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": "-",
                "port": 0
            },
            "network": {
                "protocol": "ip"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def vpn_tunnel_info(self):
        peer_ip = random.choice(self.destination_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "IPSEC-VPNUP",
                "pid": 1
            },
            "event": {
                "action": f"VPN tunnel to {peer_ip} established",
                "category": "network",
                "type": ["info", "connection"],
                "outcome": "success",
                "severity": 6
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": peer_ip,
                "port": 0
            },
            "network": {
                "protocol": "ipsec"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }

    def vpn_tunnel_warning(self):
        peer_ip = random.choice(self.destination_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "hostname": self.hostname,
            "process": {
                "name": "IPSEC-VPNDOWN",
                "pid": 1
            },
            "event": {
                "action": f"VPN tunnel to {peer_ip} disconnected",
                "category": "network",
                "type": ["warning", "connection"],
                "outcome": "failure",
                "severity": 4
            },
            "user": {
                "name": "-"
            },
            "source": {
                "ip": "-",
                "port": 0,
                "user": "-",
                "executable": "-",
                "file": "-"
            },
            "destination": {
                "ip": peer_ip,
                "port": 0
            },
            "network": {
                "protocol": "ipsec"
            },
            "file": {
                "path": "-"
            },
            "package": {
                "name": "firmware",
                "size": "0 KB"
            },
            "app": "firewall"
        }
