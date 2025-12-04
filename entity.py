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

# --- NEW GENERATION ENTITIES ---

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
        # Выбираем IP-адрес источника из внешних хостов (не самого себя)
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        src_ip = random.choice(other_ips)
        dst_ip = self.get_ip_addr()

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication"],
                "type": ["access", "start"],
                "action": "ssh_login",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-AUTH-001",
                    "name": "SSH login successful"
                }
            },
            "user": {
                "name": random.choice(self.users_attr)
            },
            "source": {
                "ip": src_ip,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": dst_ip,
                "port": 22
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999),
                "executable": "/usr/sbin/sshd"
            },
            "service": {
                "name": "SSH",
                "type": "ssh"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [random.choice(self.users_attr)]
            }
        }

    def auth_warning_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        src_ip = random.choice(other_ips)
        dst_ip = self.get_ip_addr()

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication"],
                "type": ["access", "end"],
                "action": "ssh_login_failed",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",  # или "high", но 4 → medium по вашей шкале
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-AUTH-002",
                    "name": "Failed SSH login attempt"
                }
            },
            "user": {
                "name": random.choice(self.users_attr)
            },
            "source": {
                "ip": src_ip,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": dst_ip,
                "port": 22
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999),
                "executable": "/usr/sbin/sshd"
            },
            "service": {
                "name": "SSH",
                "type": "ssh"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [random.choice(self.users_attr)]
            }
        }

    def auth_crit_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        src_ip = random.choice(other_ips)
        dst_ip = self.get_ip_addr()

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["intrusion_detection"],
                "type": ["access", "attempt"],
                "action": "ssh_brute_force_detected",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-AUTH-003",
                    "name": "SSH brute-force attack detected"
                }
            },
            "user": {
                "name": random.choice(self.users_attr)
            },
            "source": {
                "ip": src_ip,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": dst_ip,
                "port": 22
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "process": {
                "name": "sshd",
                "pid": random.randint(115, 1999),
                "executable": "/usr/sbin/sshd"
            },
            "service": {
                "name": "SSH",
                "type": "ssh"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [random.choice(self.users_attr)]
            }
        }

    def start_process_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["process"],
                "type": ["start", "access"],
                "action": "process_started",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-PROC-001",
                    "name": "Process started successfully"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "user": [user]
            }
        }

    def start_process_warning_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["process"],
                "type": ["end", "denied"],
                "action": "process_suspicious",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-PROC-002",
                    "name": "Suspicious process terminated"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "user": [user]
            }
        }

    def start_process_debug_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["process"],
                "type": ["info", "debug"],
                "action": "debug_process",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-PROC-003",
                    "name": "Process debug event"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "user": [user]
            }
        }

    def open_file_info_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = f"user-{self.asset_number.replace('IN-', '')}"
        file_path = random.choice(all_files_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["file"],
                "type": ["access", "opened"],
                "action": "file_open",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-FILE-001",
                    "name": "File opened successfully"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "file": {
                "path": file_path
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "user": [user]
            }
        }

    def open_file_warning_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = f"user-{self.asset_number.replace('IN-', '')}"
        file_path = random.choice(all_files_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["file"],
                "type": ["access", "denied"],
                "action": "file_access_denied",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-FILE-002",
                    "name": "File access attempt denied"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "file": {
                "path": file_path
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "user": [user]
            }
        }

    def open_file_crit_json(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = f"user-{self.asset_number.replace('IN-', '')}"
        file_path = random.choice(all_files_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["file"],
                "type": ["deletion", "corruption"],
                "action": "file_corrupted_or_deleted",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-FILE-003",
                    "name": "Critical system file modified or missing"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "file": {
                "path": file_path
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "user": [user]
            }
        }

    def network_activity_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = self.get_ip_addr()
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)
        protocol = random.choice(['tcp', 'udp'])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": src_ip,
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": src_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["connection", "access"],
                "action": "network_connection",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-NET-001",
                    "name": "Outbound network connection established"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "outbound"
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def network_activity_warning_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = self.get_ip_addr()
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)
        protocol = random.choice(['tcp', 'udp'])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": src_ip,
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": src_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["connection", "unusual"],
                "action": "network_connection_app",
                "outcome": "success",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-NET-002",
                    "name": "Unusual application network activity"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "outbound"
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def network_activity_debug_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = self.get_ip_addr()
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)
        protocol = "tcp"  # так как действие — "tcp_connection"

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": src_ip,
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": src_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["connection", "info"],
                "action": "tcp_connection",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-NET-003",
                    "name": "TCP connection debug event"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "outbound"
            },
            "service": {
                "name": app_name,
                "type": app_name.lower()
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def edit_policies_notice_json(self):
        app = "systemd"
        executable = "/usr/bin/systemctl"
        user = f"user-{self.asset_number.replace('IN-', '')}"
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["settings"],
                "type": ["change", "info"],
                "action": "applied_policy",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-POL-001",
                    "name": "System policy applied successfully"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "service": {
                "name": "systemd",
                "type": "system"
            },
            "related": {
                "user": [user]
            }
        }

    def edit_policies_warning_json(self):
        app = "systemd"
        executable = "/usr/bin/systemctl"
        user = f"user-{self.asset_number.replace('IN-', '')}"
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["settings"],
                "type": ["change", "denied"],
                "action": "failed_policy",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-POL-002",
                    "name": "System policy application failed"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "service": {
                "name": "systemd",
                "type": "system"
            },
            "related": {
                "user": [user]
            }
        }

    def edit_policies_info_json(self):
        app = "systemd"
        executable = "/usr/bin/systemctl"
        user = f"user-{self.asset_number.replace('IN-', '')}"
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["settings"],
                "type": ["change", "reload"],
                "action": "reload_policy",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-POL-003",
                    "name": "System policy reloaded"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app,
                "pid": random.randint(115, 1999),
                "executable": executable
            },
            "service": {
                "name": "systemd",
                "type": "system"
            },
            "related": {
                "user": [user]
            }
        }

    def remote_control_info_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = random.choice(self.destination_ip)  # внешний источник подключения
        dst_ip = self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = 3389  # стандартный порт RDP

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication", "network"],
                "type": ["connection", "access"],
                "action": "rdp_connection",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-RDP-001",
                    "name": "RDP connection established"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "xrdp",  # или "TermService" для Windows, но Linux → xrdp
                "pid": random.randint(1000, 5000),
                "executable": "/usr/sbin/xrdp"
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "RDP",
                "type": "rdp"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def remote_control_warning_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = random.choice(self.destination_ip)
        dst_ip = self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = 3389

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication", "network"],
                "type": ["connection", "denied"],
                "action": "rdp_failed_login",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-RDP-002",
                    "name": "Failed RDP login attempt"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "xrdp",
                "pid": random.randint(1000, 5000),
                "executable": "/usr/sbin/xrdp"
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "RDP",
                "type": "rdp"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def remote_control_alert_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = random.choice(self.destination_ip)
        dst_ip = self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = 3389

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["intrusion_detection", "authentication", "network"],
                "type": ["connection", "attack"],
                "action": "rdp_brute-force_detected",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-RDP-003",
                    "name": "RDP brute-force attack detected"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "xrdp",
                "pid": random.randint(1000, 5000),
                "executable": "/usr/sbin/xrdp"
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "RDP",
                "type": "rdp"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def update_system_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        user = f"user-{self.asset_number.replace('IN-', '')}"
        package_size_bytes = random.randint(1_000_000, 50_000_000)  # 1 MB – 50 MB

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["package"],
                "type": ["install", "change"],
                "action": "installation_package",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-UPD-001",
                    "name": "Software package installed"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "apt",
                "pid": random.randint(1000, 5000),
                "executable": "/usr/bin/apt"
            },
            "package": {
                "name": app_name,
                "size": package_size_bytes  # в байтах (число!)
            },
            "service": {
                "name": "Package Manager",
                "type": "apt"
            },
            "related": {
                "user": [user]
            }
        }

    def update_system_err_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        user = f"user-{self.asset_number.replace('IN-', '')}"

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["package"],
                "type": ["install", "error"],
                "action": "failed_installation_package",
                "outcome": "failure",
                "severity": 3,
                "severity_label": "high",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-UPD-002",
                    "name": "Failed to install software package"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "apt",
                "pid": random.randint(1000, 5000),
                "executable": "/usr/bin/apt"
            },
            "package": {
                "name": app_name
            },
            "service": {
                "name": "Package Manager",
                "type": "apt"
            },
            "related": {
                "user": [user]
            }
        }

    def update_system_notice_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        user = f"user-{self.asset_number.replace('IN-', '')}"
        package_size_bytes = random.randint(500_000, 10_000_000)  # 0.5–10 MB

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ubuntu"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["package"],
                "type": ["upgrade", "change"],
                "action": "security_update",
                "outcome": "success",
                "severity": 5,
                "severity_label": "medium",
                "provider": "simulated-linux",
                "rule": {
                    "id": "SIM-UPD-003",
                    "name": "Security update applied"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "apt",
                "pid": random.randint(1000, 5000),
                "executable": "/usr/bin/apt"
            },
            "package": {
                "name": app_name,
                "size": package_size_bytes
            },
            "service": {
                "name": "Package Manager",
                "type": "apt"
            },
            "related": {
                "user": [user]
            }
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
        src_ip = random.choice(other_ips)
        dst_ip = self.get_ip_addr()
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication"],
                "type": ["access", "start"],
                "action": "user_login",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-AUTH-WIN-001",
                    "name": "Windows user login successful"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "lsass.exe",
                "pid": random.randint(500, 2000),
                "executable": "C:\\Windows\\System32\\lsass.exe"
            },
            "source": {
                "ip": src_ip,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": dst_ip,
                "port": 445  # или 3389 для RDP, но общий вход — через SMB/NetLogon
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Windows Authentication",
                "type": "windows"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def auth_warning_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        src_ip = random.choice(other_ips)
        dst_ip = self.get_ip_addr()
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication"],
                "type": ["access", "end"],
                "action": "user_login_failed",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-AUTH-WIN-002",
                    "name": "Failed Windows login attempt"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "lsass.exe",
                "pid": random.randint(500, 2000),
                "executable": "C:\\Windows\\System32\\lsass.exe"
            },
            "source": {
                "ip": src_ip,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": dst_ip,
                "port": 445
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Windows Authentication",
                "type": "windows"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def auth_crit_json(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        src_ip = random.choice(other_ips)
        dst_ip = self.get_ip_addr()
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["intrusion_detection", "authentication"],
                "type": ["access", "attack"],
                "action": "brute_force_detected",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-AUTH-WIN-003",
                    "name": "Windows brute-force attack detected"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "lsass.exe",
                "pid": random.randint(500, 2000),
                "executable": "C:\\Windows\\System32\\lsass.exe"
            },
            "source": {
                "ip": src_ip,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": dst_ip,
                "port": 445
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Windows Authentication",
                "type": "windows"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def start_process_info_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["process"],
                "type": ["start", "access"],
                "action": "process_started",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-PROC-001",
                    "name": "Windows process started successfully"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "service": {
                "name": app_name,
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "user": [user]
            }
        }

    def start_process_warning_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["process"],
                "type": ["end", "denied"],
                "action": "process_suspicious",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-PROC-002",
                    "name": "Suspicious Windows process terminated"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "service": {
                "name": app_name,
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "user": [user]
            }
        }

    def start_process_debug_json(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr)
        user = random.choice(self.users_attr)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["process"],
                "type": ["info", "debug"],
                "action": "debug_process",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-PROC-003",
                    "name": "Windows process debug event"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "service": {
                "name": app_name,
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "user": [user]
            }
        }

    def open_file_info_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        # Подставляем имя пользователя в пути
        home_files = [path.format(user=user) for path in self.home_files_attr]
        all_files = home_files + self.config_files_attr + self.system_files_attr  # socket_files_attr пуст у Windows
        file_path = random.choice(all_files)

        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr).format(user=user)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["file"],
                "type": ["access", "opened"],
                "action": "file_open",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-FILE-001",
                    "name": "File opened successfully"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "file": {
                "path": file_path
            },
            "service": {
                "name": app_name.replace(".exe", ""),
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "user": [user]
            }
        }

    def open_file_warning_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        home_files = [path.format(user=user) for path in self.home_files_attr]
        all_files = home_files + self.config_files_attr + self.system_files_attr
        file_path = random.choice(all_files)

        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr).format(user=user)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["file"],
                "type": ["access", "denied"],
                "action": "file_access_denied",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-FILE-002",
                    "name": "File access attempt denied"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "file": {
                "path": file_path
            },
            "service": {
                "name": app_name.replace(".exe", ""),
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "user": [user]
            }
        }

    def open_file_crit_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        home_files = [path.format(user=user) for path in self.home_files_attr]
        all_files = home_files + self.config_files_attr + self.system_files_attr
        file_path = random.choice(all_files)

        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr).format(user=user)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["file"],
                "type": ["deletion", "corruption"],
                "action": "critical_file_modified",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-FILE-003",
                    "name": "Critical system file modified or deleted"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "file": {
                "path": file_path
            },
            "service": {
                "name": app_name.replace(".exe", ""),
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "user": [user]
            }
        }

    def network_activity_info_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr).format(user=user)

        src_ip = self.get_ip_addr()
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)
        protocol = random.choice(['tcp', 'udp'])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": src_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": src_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["connection", "access"],
                "action": "network_connection",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-NET-001",
                    "name": "Outbound network connection established"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "outbound"
            },
            "service": {
                "name": app_name.replace(".exe", ""),
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def network_activity_warning_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr).format(user=user)

        src_ip = self.get_ip_addr()
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)
        protocol = random.choice(['tcp', 'udp'])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": src_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": src_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["connection", "unusual"],
                "action": "network_connection_app",
                "outcome": "success",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-NET-002",
                    "name": "Unusual application network activity"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "outbound"
            },
            "service": {
                "name": app_name.replace(".exe", ""),
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def network_activity_debug_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        executable = random.choice(self.software_files_attr).format(user=user)

        src_ip = self.get_ip_addr()
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)
        protocol = "tcp"  # действие — "tcp_connection"

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": src_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": src_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["connection", "info"],
                "action": "tcp_connection",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-NET-003",
                    "name": "TCP connection debug event"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": app_name,
                "pid": random.randint(1000, 5000),
                "executable": executable
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "outbound"
            },
            "service": {
                "name": app_name.replace(".exe", ""),
                "type": app_name.replace(".exe", "").lower()
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def edit_policies_notice_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["settings"],
                "type": ["change", "info"],
                "action": "applied_policy",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-POL-001",
                    "name": "Group Policy applied successfully"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "GroupPolicy",
                "pid": random.randint(1000, 5000),
                "executable": "C:\\Windows\\System32\\gpsvc.dll"
            },
            "service": {
                "name": "Group Policy",
                "type": "gpo"
            },
            "related": {
                "user": [user]
            }
        }

    def edit_policies_warning_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["settings"],
                "type": ["change", "error"],
                "action": "failed_policy",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-POL-002",
                    "name": "Group Policy application failed"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "GroupPolicy",
                "pid": random.randint(1000, 5000),
                "executable": "C:\\Windows\\System32\\gpsvc.dll"
            },
            "service": {
                "name": "Group Policy",
                "type": "gpo"
            },
            "related": {
                "user": [user]
            }
        }

    def edit_policies_info_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["settings"],
                "type": ["change", "reload"],
                "action": "reload_policy",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-POL-003",
                    "name": "Group Policy reloaded"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "GroupPolicy",
                "pid": random.randint(1000, 5000),
                "executable": "C:\\Windows\\System32\\gpsvc.dll"
            },
            "service": {
                "name": "Group Policy",
                "type": "gpo"
            },
            "related": {
                "user": [user]
            }
        }

    def remote_control_info_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = random.choice(self.destination_ip)  # Внешний клиент
        dst_ip = self.get_ip_addr()  # Целевой хост
        src_port = random.randint(32768, 65535)
        dst_port = 3389  # RDP

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication", "network"],
                "type": ["connection", "access"],
                "action": "rdp_connection",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-RDP-001",
                    "name": "RDP connection established"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "TermService",
                "pid": random.randint(500, 2000),
                "executable": "C:\\Windows\\System32\\termsrv.dll"
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Remote Desktop",
                "type": "rdp"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def remote_control_warning_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = random.choice(self.destination_ip)
        dst_ip = self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = 3389

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["authentication", "network"],
                "type": ["connection", "denied"],
                "action": "rdp_failed_login",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-RDP-002",
                    "name": "Failed RDP login attempt"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "TermService",
                "pid": random.randint(500, 2000),
                "executable": "C:\\Windows\\System32\\termsrv.dll"
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Remote Desktop",
                "type": "rdp"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def remote_control_alert_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        src_ip = random.choice(self.destination_ip)
        dst_ip = self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = 3389

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": dst_ip,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["intrusion_detection", "authentication", "network"],
                "type": ["connection", "attack"],
                "action": "rdp_brute-force_detected",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-RDP-003",
                    "name": "RDP brute-force attack detected"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "TermService",
                "pid": random.randint(500, 2000),
                "executable": "C:\\Windows\\System32\\termsrv.dll"
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Remote Desktop",
                "type": "rdp"
            },
            "related": {
                "ip": [src_ip, dst_ip],
                "user": [user]
            }
        }

    def update_system_info_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        package_size_bytes = random.randint(1_000_000, 50_000_000)  # 1–50 MB

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["package"],
                "type": ["install", "change"],
                "action": "installation_package",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-UPD-001",
                    "name": "Windows software package installed"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "TiWorker.exe",
                "pid": random.randint(1000, 5000),
                "executable": "C:\\Windows\\System32\\TiWorker.exe"
            },
            "package": {
                "name": app_name,
                "size": package_size_bytes  # число в байтах
            },
            "service": {
                "name": "Windows Update",
                "type": "windows_update"
            },
            "related": {
                "user": [user]
            }
        }

    def update_system_err_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["package"],
                "type": ["install", "error"],
                "action": "failed_installation_package",
                "outcome": "failure",
                "severity": 3,
                "severity_label": "high",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-UPD-002",
                    "name": "Failed to install Windows software package"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "TiWorker.exe",
                "pid": random.randint(1000, 5000),
                "executable": "C:\\Windows\\System32\\TiWorker.exe"
            },
            "package": {
                "name": app_name
            },
            "service": {
                "name": "Windows Update",
                "type": "windows_update"
            },
            "related": {
                "user": [user]
            }
        }

    def update_system_notice_json(self):
        user = f"user-{self.asset_number.replace('IN-', '')}"
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        package_size_bytes = random.randint(500_000, 10_000_000)  # 0.5–10 MB

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "windows"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "host"
            },
            "event": {
                "kind": "event",
                "category": ["package"],
                "type": ["upgrade", "change"],
                "action": "security_update",
                "outcome": "success",
                "severity": 5,
                "severity_label": "medium",
                "provider": "simulated-windows",
                "rule": {
                    "id": "SIM-WIN-UPD-003",
                    "name": "Windows security update applied"
                }
            },
            "user": {
                "name": user
            },
            "process": {
                "name": "TiWorker.exe",
                "pid": random.randint(1000, 5000),
                "executable": "C:\\Windows\\System32\\TiWorker.exe"
            },
            "package": {
                "name": app_name,
                "size": package_size_bytes
            },
            "service": {
                "name": "Windows Update",
                "type": "windows_update"
            },
            "related": {
                "user": [user]
            }
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
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"  # или "nxos", "cumulus", в зависимости от вашей модели
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["change", "info"],
                "action": f"Interface {port} changed state to up",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-PORT-001",
                    "name": "Switch port state changed to up"
                }
            },
            "process": {
                "name": "LINK-UPDOWN",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Switch Management",
                "type": "switch"
            }
        }

    def change_status_port_warning(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["change", "warning"],
                "action": f"Interface {port} flapping",
                "outcome": "success",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-PORT-002",
                    "name": "Switch port flapping detected"
                }
            },
            "process": {
                "name": "LINK-FLAP",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Switch Management",
                "type": "switch"
            }
        }

    def change_status_port_crit(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "alert",
                "category": ["network"],
                "type": ["error", "failure"],
                "action": f"Hardware failure on {port}",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-PORT-003",
                    "name": "Switch hardware port failure"
                }
            },
            "process": {
                "name": "HWIC-PORT_FAIL",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Switch Management",
                "type": "switch"
            }
        }

    def learn_mac_addr_info(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        if not other_mac:
            return None  # защита от пустого списка
        mac_addr = random.choice(other_mac)
        port = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "change"],
                "action": f"MAC {mac_addr} learned on {port}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-MAC-001",
                    "name": "Switch learned new MAC address"
                }
            },
            "process": {
                "name": "MAC-LEARN",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Switch Forwarding",
                "type": "switch"
            }
        }

    def learn_mac_addr_warning(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        if not other_mac:
            return None
        mac_addr = random.choice(other_mac)
        from_port = random.choice(self.port)
        to_port = random.choice([p for p in self.port if p != from_port] or self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["change", "warning"],
                "action": f"MAC {mac_addr} moved from {from_port} to {to_port}",
                "outcome": "success",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-MAC-002",
                    "name": "MAC address moved between switch ports"
                }
            },
            "process": {
                "name": "MAC-MOVE",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Switch Forwarding",
                "type": "switch"
            }
        }

    def learn_mac_addr_debug(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        if not other_mac:
            return None
        mac_addr = random.choice(other_mac)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "debug"],
                "action": f"MAC table entry added: {mac_addr}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-MAC-003",
                    "name": "Switch MAC table debug entry"
                }
            },
            "process": {
                "name": "MAC-TABLE",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Switch Forwarding",
                "type": "switch"
            }
        }

    def violation_port_security_warning(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["security", "warning"],
                "action": f"Security violation on {port}",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-PORTSEC-001",
                    "name": "Port security violation detected"
                }
            },
            "process": {
                "name": "PORTSEC-VIOLATION",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Port Security",
                "type": "switch"
            }
        }

    def violation_port_security_crit(self):
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["security", "attack"],
                "action": "CAM table overflow attack detected",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-PORTSEC-002",
                    "name": "CAM table flooding attack"
                }
            },
            "process": {
                "name": "PORTSEC-CAM_FLOOD",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Port Security",
                "type": "switch"
            }
        }

    def violation_port_security_alert(self):
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["security", "alert"],
                "action": "Unauthorized device connected",
                "outcome": "failure",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-PORTSEC-003",
                    "name": "Unauthorized device detected on switch port"
                }
            },
            "process": {
                "name": "SECURITY-COMPROMISE",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Port Security",
                "type": "switch"
            }
        }

    def stp_event_info(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "change"],
                "action": f"Port {port} to forwarding",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-STP-001",
                    "name": "STP port transitioned to forwarding state"
                }
            },
            "process": {
                "name": "STP-PORTSTATE",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Spanning Tree Protocol",
                "type": "stp"
            }
        }

    def stp_event_warning(self):
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "change"],
                "action": "Topology change detected",
                "outcome": "success",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-STP-002",
                    "name": "STP topology change detected"
                }
            },
            "process": {
                "name": "STP-TOPOLOGY_CHANGE",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Spanning Tree Protocol",
                "type": "stp"
            }
        }

    def stp_event_crit(self):
        vlan = random.randint(2, 19)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["error", "critical"],
                "action": f"Network loop detected on VLAN {vlan}",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-STP-003",
                    "name": "STP loop detected — potential network outage"
                }
            },
            "process": {
                "name": "STP-LOOP_DETECTED",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Spanning Tree Protocol",
                "type": "stp"
            }
        }

    def duplex_error_warning(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "error"],
                "action": f"CRC errors on {port}",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-DUPLEX-001",
                    "name": "CRC errors detected on switch port"
                }
            },
            "process": {
                "name": "INTERFACE-CRC",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Interface Diagnostics",
                "type": "switch"
            }
        }

    def duplex_error_err(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["error", "failure"],
                "action": f"Duplex mismatch on {port}",
                "outcome": "failure",
                "severity": 3,
                "severity_label": "high",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-DUPLEX-002",
                    "name": "Duplex mismatch on switch port"
                }
            },
            "process": {
                "name": "PHY-DUPLEX_MISMATCH",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Interface Diagnostics",
                "type": "switch"
            }
        }

    def duplex_error_crit(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "hardware"],
                "type": ["error", "critical"],
                "action": f"Physical layer failure on {port}",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-DUPLEX-003",
                    "name": "Physical layer failure on switch port"
                }
            },
            "process": {
                "name": "HWIC-HARDWARE_ERR",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "Interface Diagnostics",
                "type": "switch"
            }
        }

    def vlan_event_info(self):
        port = random.choice(self.port)
        vlan = random.randint(2, 19)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "change"],
                "action": f"Port {port} assigned to VLAN {vlan}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-VLAN-001",
                    "name": "Switch port assigned to VLAN"
                }
            },
            "process": {
                "name": "VLAN-ASSIGN",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "VLAN Management",
                "type": "switch"
            }
        }

    def vlan_event_warning(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "misconfiguration"],
                "action": f"Native VLAN mismatch on {port}",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-VLAN-002",
                    "name": "Native VLAN mismatch detected"
                }
            },
            "process": {
                "name": "VLAN-NATIVE_MISMATCH",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "VLAN Management",
                "type": "switch"
            }
        }

    def vlan_event_debug(self):
        port = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"VLAN membership updated for {port}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-VLAN-003",
                    "name": "VLAN membership debug update"
                }
            },
            "process": {
                "name": "VLAN-DEBUG",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "VLAN Management",
                "type": "switch"
            }
        }

    def auth_802_1x_info(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        if not other_mac:
            return None
        mac_addr = random.choice(other_mac)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network", "authentication"],
                "type": ["info", "access"],
                "action": f"Auth succeeded for MAC {mac_addr}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-8021X-001",
                    "name": "802.1X authentication succeeded"
                }
            },
            "process": {
                "name": "DOT1X-SUCCESS",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "802.1X Authentication",
                "type": "dot1x"
            }
        }

    def auth_802_1x_warning(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        if not other_mac:
            return None
        mac_addr = random.choice(other_mac)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "event",
                "category": ["network", "authentication"],
                "type": ["warning", "access"],
                "action": f"Auth failed for MAC {mac_addr}",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-8021X-002",
                    "name": "802.1X authentication failed"
                }
            },
            "process": {
                "name": "DOT1X-FAIL",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "802.1X Authentication",
                "type": "dot1x"
            }
        }

    def auth_802_1x_alert(self, list_mac_addr):
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "switch"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection", "authentication"],
                "type": ["alert", "attack"],
                "action": "EAPOL flood attack detected",
                "outcome": "failure",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-switch",
                "rule": {
                    "id": "SIM-SW-8021X-003",
                    "name": "802.1X EAPOL flood attack"
                }
            },
            "process": {
                "name": "DOT1X-ATTACK",
                "pid": 1
            },
            "network": {
                "protocol": "ethernet"
            },
            "service": {
                "name": "802.1X Authentication",
                "type": "dot1x"
            }
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
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"  # или "nxos", "cumulus" и т.д.
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "change"],
                "action": f"{interface} changed state to up",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-INT-001",
                    "name": "Router interface state changed to up"
                }
            },
            "process": {
                "name": "LINEPROTO-UPDOWN",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "Interface Management",
                "type": "router"
            }
        }

    def change_status_int_warning(self):
        interface = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "change"],
                "action": f"{interface} flapping",
                "outcome": "success",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-INT-002",
                    "name": "Router interface flapping detected"
                }
            },
            "process": {
                "name": "INTERFACE-FLAP",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "Interface Management",
                "type": "router"
            }
        }

    def change_status_int_crit(self):
        interface = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "hardware"],
                "type": ["error", "critical"],
                "action": f"Carrier loss on {interface}",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-INT-003",
                    "name": "Router interface carrier loss — physical layer failure"
                }
            },
            "process": {
                "name": "HWIC-LINK_FAIL",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "Interface Management",
                "type": "router"
            }
        }

    def change_roadmap_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        route = random.choice(self.destination_ip + other_ip)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "change"],
                "action": f"Route {route} added",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ROUTE-001",
                    "name": "Static or dynamic route added to routing table"
                }
            },
            "process": {
                "name": "IP-ROUTE",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "Routing Engine",
                "type": "routing"
            }
        }

    def change_roadmap_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        route = random.choice(self.destination_ip + other_ip)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "change"],
                "action": f"Route {route} flapping",
                "outcome": "success",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ROUTE-002",
                    "name": "Route flapping detected — unstable path"
                }
            },
            "process": {
                "name": "IP-ROUTE_FLAP",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "Routing Engine",
                "type": "routing"
            }
        }

    def change_roadmap_alert(self):
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "availability"],
                "type": ["alert", "failure"],
                "action": "All default routes lost",
                "outcome": "failure",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ROUTE-003",
                    "name": "Critical routing failure — no default route available"
                }
            },
            "process": {
                "name": "IP-ROUTING_LOSS",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "Routing Engine",
                "type": "routing"
            }
        }

    def dynamic_routing_event_info(self):
        neighbor = random.choice(self.destination_ip)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "change"],
                "action": f"Nbr {neighbor} from DOWN to FULL",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-DYN-001",
                    "name": "OSPF adjacency established"
                }
            },
            "process": {
                "name": "OSPF-ADJCHG",
                "pid": 1
            },
            "network": {
                "protocol": "ospf"
            },
            "service": {
                "name": "Dynamic Routing",
                "type": "routing"
            }
        }

    def dynamic_routing_event_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            neighbor = random.choice(self.destination_ip)
        else:
            neighbor = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "failure"],
                "action": f"Neighbor {neighbor} Down",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-DYN-002",
                    "name": "BGP neighbor down"
                }
            },
            "process": {
                "name": "BGP-ADJCHANGE",
                "pid": 1
            },
            "network": {
                "protocol": "bgp"
            },
            "service": {
                "name": "Dynamic Routing",
                "type": "routing"
            }
        }

    def dynamic_routing_event_crit(self):
        interface = random.choice(self.port)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "integrity"],
                "type": ["error", "critical"],
                "action": f"OSPF checksum error on {interface}",
                "outcome": "failure",
                "severity": 2,
                "severity_label": "critical",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-DYN-003",
                    "name": "OSPF protocol integrity violation"
                }
            },
            "process": {
                "name": "OSPF-PROTOCOL_ERR",
                "pid": 1
            },
            "network": {
                "protocol": "ospf"
            },
            "service": {
                "name": "Dynamic Routing",
                "type": "routing"
            }
        }

    def acl_activity_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            src_ip = "0.0.0.0"
        else:
            src_ip = random.choice(other_ip)
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([20, 21, 22, 23, 25, 53, 80, 443, 3389, 8080])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "access"],
                "action": f"Permitted tcp from {src_ip} to {dst_ip}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ACL-001",
                    "name": "ACL permit rule matched"
                }
            },
            "process": {
                "name": "ACL-PERMIT",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Access Control List",
                "type": "acl"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def acl_activity_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(self.destination_ip)
        if not other_ip:
            dst_ip = "0.0.0.0"
        else:
            dst_ip = random.choice(other_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([20, 21, 22, 23, 25, 53, 80, 443, 3389, 8080])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "access"],
                "action": f"Denied tcp from {src_ip} to {dst_ip}",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ACL-002",
                    "name": "ACL deny rule matched"
                }
            },
            "process": {
                "name": "ACL-DENIED",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Access Control List",
                "type": "acl"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def acl_activity_debug(self):
        rule_id = random.randint(100, 187)
        protocol = random.choice(['tcp', 'udp'])
        src = random.choice(self.port + ['any'])
        dst = random.choice(self.port + ['any'])
        dst_port = random.choice(
            [20, 21, 22, 23, 25, 53, 80, 8080, 110, 135, 143, 443, 445, 993, 9600, 9200, 3306, 5432])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"Matched rule {rule_id}: permit {protocol} {src} {dst} eq {dst_port}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ACL-003",
                    "name": "ACL debug match"
                }
            },
            "process": {
                "name": "ACL-MATCH",
                "pid": 1
            },
            "network": {
                "protocol": protocol
            },
            "service": {
                "name": "Access Control List",
                "type": "acl"
            }
        }

    def nat_event_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            src_ip = "0.0.0.0"
        else:
            src_ip = random.choice(other_ip)
        translated_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "translation"],
                "action": f"Translated {src_ip} to {translated_ip}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-NAT-001",
                    "name": "NAT translation performed"
                }
            },
            "process": {
                "name": "NAT-ADDR",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": translated_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "ip",
                "direction": "outbound"
            },
            "service": {
                "name": "Network Address Translation",
                "type": "nat"
            },
            "related": {
                "ip": [src_ip, translated_ip]
            }
        }

    def nat_event_warning(self, list_ip_addr):
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "resource"],
                "action": "NAT pool exhausted",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-NAT-002",
                    "name": "NAT address pool exhausted"
                }
            },
            "process": {
                "name": "NAT-POOL_EXHAUSTED",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "Network Address Translation",
                "type": "nat"
            }
        }

    def nat_event_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            src_ip = "0.0.0.0"
        else:
            src_ip = random.choice(other_ip)
        dst_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.randint(1, 65535)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"NAT entry created: {src_ip}:{src_port} to {dst_ip}:{dst_port}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-NAT-003",
                    "name": "NAT debug session created"
                }
            },
            "process": {
                "name": "NAT-DEBUG",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "ip",
                "direction": "outbound"
            },
            "service": {
                "name": "Network Address Translation",
                "type": "nat"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def icmp_message_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            dst_ip = "0.0.0.0"
        else:
            dst_ip = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "communication"],
                "action": f"Echo reply sent to {dst_ip}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ICMP-001",
                    "name": "ICMP echo reply sent"
                }
            },
            "process": {
                "name": "ICMP-ECHO",
                "pid": 1
            },
            "source": {
                "ip": self.get_ip_addr()
            },
            "destination": {
                "ip": dst_ip
            },
            "network": {
                "protocol": "icmp"
            },
            "service": {
                "name": "ICMP Handling",
                "type": "icmp"
            },
            "related": {
                "ip": [self.get_ip_addr(), dst_ip]
            }
        }

    def icmp_message_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            dst_ip = "0.0.0.0"
        else:
            dst_ip = random.choice(other_ip)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "error"],
                "action": f"Destination {dst_ip} unreachable",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ICMP-002",
                    "name": "ICMP destination unreachable"
                }
            },
            "process": {
                "name": "ICMP-DSTUNREACH",
                "pid": 1
            },
            "source": {
                "ip": self.get_ip_addr()
            },
            "destination": {
                "ip": dst_ip
            },
            "network": {
                "protocol": "icmp"
            },
            "service": {
                "name": "ICMP Handling",
                "type": "icmp"
            },
            "related": {
                "ip": [self.get_ip_addr(), dst_ip]
            }
        }

    def icmp_message_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            src_ip = "0.0.0.0"
        else:
            src_ip = random.choice(other_ip)
        icmp_type = random.randint(3, 12)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"Received ICMP type {icmp_type} from {src_ip}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-ICMP-003",
                    "name": "ICMP debug message received"
                }
            },
            "process": {
                "name": "ICMP-DEBUG",
                "pid": 1
            },
            "source": {
                "ip": src_ip
            },
            "destination": {
                "ip": self.get_ip_addr()
            },
            "network": {
                "protocol": "icmp"
            },
            "service": {
                "name": "ICMP Handling",
                "type": "icmp"
            },
            "related": {
                "ip": [src_ip, self.get_ip_addr()]
            }
        }

    def violation_traffic_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            src_ip = "0.0.0.0"
        else:
            src_ip = random.choice(other_ip)
        traffic_class = random.choice(['VOICE', 'VIDEO CONF', 'BUSINESS-DATA', 'EFFORT'])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "classification"],
                "action": f"Traffic from {src_ip} classified as {traffic_class}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-QOS-001",
                    "name": "QoS traffic classification"
                }
            },
            "process": {
                "name": "QOS-CLASSIFIED",
                "pid": 1
            },
            "source": {
                "ip": src_ip
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "QoS Engine",
                "type": "qos"
            },
            "related": {
                "ip": [src_ip, self.get_ip_addr()]
            }
        }

    def violation_traffic_warning(self):
        interface = random.choice(self.port)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "resource"],
                "action": f"Rate limit exceeded on {interface}",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-QOS-002",
                    "name": "QoS rate limit exceeded"
                }
            },
            "process": {
                "name": "QOS-RATE_EXCEEDED",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "QoS Engine",
                "type": "qos"
            }
        }

    def violation_traffic_debug(self):
        marking = random.choice(['DSCP', 'COS'])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "ios"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "router"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"Packet marked with {marking}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-router",
                "rule": {
                    "id": "SIM-RT-QOS-003",
                    "name": "QoS packet marking debug"
                }
            },
            "process": {
                "name": "QOS-DEBUG",
                "pid": 1
            },
            "network": {
                "protocol": "ip"
            },
            "service": {
                "name": "QoS Engine",
                "type": "qos"
            }
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
        if not other_ip:
            dst_ip = "0.0.0.0"
        else:
            dst_ip = random.choice(other_ip)
        src_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([22, 25, 53, 80, 443, 3389, 8080])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "panos"  # или "asa", "fortios" — в зависимости от модели
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "connection"],
                "action": f"Built TCP connection for outside: {src_ip} to inside: {dst_ip}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-ALLOW-001",
                    "name": "Allowed outbound TCP connection"
                }
            },
            "process": {
                "name": "ASA-302013",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "inbound"
            },
            "service": {
                "name": "Firewall Policy Engine",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def allow_traffic_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            dst_ip = "0.0.0.0"
        else:
            dst_ip = random.choice(other_ip)
        src_ip = random.choice(self.destination_ip)
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([22, 25, 53, 80, 443, 3389, 8080])
        app_proto = random.choice(['ssh', 'ssl', 'tls', 'http', 'telnet'])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "panos"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"Session created: src={src_ip}, dst={dst_ip}, app={app_proto}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-ALLOW-002",
                    "name": "Firewall session debug event"
                }
            },
            "process": {
                "name": "PAN-SESSION",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": app_proto,
                "direction": "inbound"
            },
            "service": {
                "name": "Firewall Session Tracker",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def lock_traffic_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        if not other_ip:
            dst_ip = "0.0.0.0"
        else:
            dst_ip = random.choice(other_ip)
        src_ip = random.choice(self.destination_ip)
        protocol = random.choice(['tcp', 'udp'])
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([22, 23, 25, 53, 80, 443, 3389, 8080])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "panos"  # или "asa", "fortios" — в зависимости от модели
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "access"],
                "action": f"Deny {protocol} src outside:{src_ip}, dst inside:{dst_ip}",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-DENY-001",
                    "name": "Firewall denied outbound traffic"
                }
            },
            "process": {
                "name": "ASA-106015",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "inbound"
            },
            "service": {
                "name": "Firewall Policy Engine",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def lock_traffic_alert(self, list_ip_addr):
        # Для атаки генерируем реалистичные IP
        src_ip = random.choice(self.destination_ip)
        dst_ip = self.get_ip_addr()  # или внутренний хост, но для простоты — сам фаервол
        protocol = "tcp"
        src_port = random.randint(32768, 65535)
        dst_port = 445  # типичная цель для эксплойтов

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "panos"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["alert", "security"],
                "action": "Critical threat: Exploit attempt blocked",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-THREAT-001",
                    "name": "Firewall blocked critical exploit attempt"
                }
            },
            "process": {
                "name": "PAN-THREAT",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol,
                "direction": "inbound"
            },
            "service": {
                "name": "Threat Prevention",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def lock_traffic_debug(self):
        rule_app = random.choice(['ssh', 'ssl', 'tls', 'http', 'telnet'])
        src_ip = random.choice(self.destination_ip)
        dst_ip = self.get_ip_addr()  # или внутренний адрес, но для простоты — сам фаервол
        src_port = random.randint(32768, 65535)
        dst_port = {'ssh': 22, 'http': 80, 'ssl': 443, 'tls': 443, 'telnet': 23}.get(rule_app, 0)

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "panos"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"Matched rule 'block-external-{rule_app}'",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-DEBUG-001",
                    "name": "Firewall debug rule match"
                }
            },
            "process": {
                "name": "FW-RULE_MATCH",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": rule_app,
                "direction": "inbound"
            },
            "service": {
                "name": "Firewall Policy Engine",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def change_session_info_connect(self, list_ip_addr):
        protocol = random.choice(['TCP', 'UDP'])
        conn_id = random.randint(1000, 20000)
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(self.destination_ip)
        dst_ip = random.choice(other_ip) if other_ip else self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([22, 25, 53, 80, 443, 3389, 8080])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "asa"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "connection"],
                "action": f"Built {protocol} connection {conn_id}",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-CONN-001",
                    "name": "Firewall session established"
                }
            },
            "process": {
                "name": "ASA-6-302013",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol.lower(),
                "direction": "inbound"
            },
            "service": {
                "name": "Firewall Session Tracker",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def change_session_info_breakup(self, list_ip_addr):
        protocol = random.choice(['TCP', 'UDP'])
        conn_id = random.randint(1000, 20000)
        duration = random.randint(60, 600)

        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(self.destination_ip)
        dst_ip = random.choice(other_ip) if other_ip else self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([22, 25, 53, 80, 443, 3389, 8080])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "asa"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "connection"],
                "action": f"Teardown {protocol} connection {conn_id} duration {duration}sec",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-SESSION-001",
                    "name": "Firewall session teardown"
                }
            },
            "process": {
                "name": "ASA-6-302014",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": protocol.lower(),
                "direction": "inbound"
            },
            "service": {
                "name": "Firewall Session Tracker",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def change_session_debug(self, list_ip_addr):
        bytes_in = random.randint(10000, 200000)
        bytes_out = random.randint(10000, 200000)

        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        src_ip = random.choice(self.destination_ip)
        dst_ip = random.choice(other_ip) if other_ip else self.get_ip_addr()
        src_port = random.randint(32768, 65535)
        dst_port = random.choice([22, 25, 53, 80, 443, 3389, 8080])

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "os": {
                    "name": self.os,
                    "platform": "asa"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.get_ip_addr(),
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["debug", "info"],
                "action": f"Session stats: bytes_in={bytes_in}, bytes_out={bytes_out}",
                "outcome": "success",
                "severity": 7,
                "severity_label": "low",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-SESSION-002",
                    "name": "Firewall session debug statistics"
                }
            },
            "process": {
                "name": "FW-SESSION",
                "pid": 1
            },
            "source": {
                "ip": src_ip,
                "port": src_port
            },
            "destination": {
                "ip": dst_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "ip",
                "direction": "inbound"
            },
            "service": {
                "name": "Firewall Session Tracker",
                "type": "firewall"
            },
            "related": {
                "ip": [src_ip, dst_ip]
            }
        }

    def vpn_tunnel_info(self):
        peer_ip = random.choice(self.destination_ip)
        local_ip = self.get_ip_addr()
        src_port = 500  # стандартный порт IKE
        dst_port = 500

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": local_ip,
                "os": {
                    "name": self.os,
                    "platform": "panos"  # или "asa", "fortios" — в зависимости от модели
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": local_ip,
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["info", "connection"],
                "action": f"VPN tunnel to {peer_ip} established",
                "outcome": "success",
                "severity": 6,
                "severity_label": "medium",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-VPN-001",
                    "name": "IPsec VPN tunnel established"
                }
            },
            "process": {
                "name": "IPSEC-VPNUP",
                "pid": 1
            },
            "source": {
                "ip": local_ip,
                "port": src_port
            },
            "destination": {
                "ip": peer_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "ipsec",
                "direction": "outbound"
            },
            "service": {
                "name": "IPsec VPN",
                "type": "vpn"
            },
            "related": {
                "ip": [local_ip, peer_ip]
            }
        }

    def vpn_tunnel_warning(self):
        peer_ip = random.choice(self.destination_ip)
        local_ip = self.get_ip_addr()
        src_port = 500
        dst_port = 500

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": local_ip,
                "os": {
                    "name": self.os,
                    "platform": "panos"
                }
            },
            "observer": {
                "hostname": self.hostname,
                "ip": local_ip,
                "type": "firewall"
            },
            "event": {
                "kind": "event",
                "category": ["network"],
                "type": ["warning", "connection"],
                "action": f"VPN tunnel to {peer_ip} disconnected",
                "outcome": "failure",
                "severity": 4,
                "severity_label": "medium",
                "provider": "simulated-firewall",
                "rule": {
                    "id": "SIM-FW-VPN-002",
                    "name": "IPsec VPN tunnel disconnected"
                }
            },
            "process": {
                "name": "IPSEC-VPNDOWN",
                "pid": 1
            },
            "source": {
                "ip": local_ip,
                "port": src_port
            },
            "destination": {
                "ip": peer_ip,
                "port": dst_port
            },
            "network": {
                "protocol": "ipsec",
                "direction": "outbound"
            },
            "service": {
                "name": "IPsec VPN",
                "type": "vpn"
            },
            "related": {
                "ip": [local_ip, peer_ip]
            }
        }

class Attacker(Device):

    def __init__(self, hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain):
        super().__init__(hostname, os, category, log_format, asset_number, ip_addr, mac_addr, domain)
        self.destination_ip = [
            "8.8.8.8", "1.1.1.1", "9.9.9.9", "142.250.185.206", "140.82.121.4",
            "104.16.132.229", "40.126.35.10", "17.253.144.10", "13.32.187.123",
            "31.13.71.36", "104.244.42.1", "142.250.186.174", "91.198.174.192",
            "151.101.1.69", "173.194.222.108", "52.100.160.10", "162.125.1.1",
            "3.233.128.10", "34.102.136.180", "13.107.246.10", "91.189.91.83",
            "34.224.140.168", "104.16.23.35", "151.101.193.223"
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
        self.user = random.choice(self.users_attr)

    def ssh_bruteforce(self, target_ip, target_port=22):

        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["intrusion_detection", "authentication"],
                "type": ["access", "attack"],
                "action": "ssh_brute_force_launched",
                "outcome": "success", # Атака запущена
                "severity": 1, # Критическая для атакующего
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-SSH-BF-001",
                    "name": "Simulated SSH brute-force attack launched"
                }
            },
            "user": {"name": "attacker"},
            "process": {
                "name": "hydra",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/bin/hydra"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": target_ip,
                "port": target_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "outbound"
            },
            "service": {
                "name": "SSH",
                "type": "ssh"
            },
            "related": {
                "ip": [self.ip_addr, target_ip],
                "user": self.user
            }
        }

    def rdp_bruteforce(self, target_ip, target_port=3389):
        """
        Генерирует событие атаки brute-force по RDP.
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["intrusion_detection", "authentication"],
                "type": ["connection", "attack"],
                "action": "rdp_brute-force_launched",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-RDP-BF-001",
                    "name": "Simulated RDP brute-force attack launched"
                }
            },
            "user": {"name": self.user},
            "process": {
                "name": "crowbar",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/bin/crowbar"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": target_ip,
                "port": target_port
            },
            "network": {
                "protocol": "tcp",
                "direction": "outbound"
            },
            "service": {
                "name": "RDP",
                "type": "rdp"
            },
            "related": {
                "ip": [self.ip_addr, target_ip],
                "user": self.user
            }
        }

    def data_exfiltration(self, target_ip, exfiltrated_data_size_bytes):
        """
        Генерирует событие передачи данных (data exfiltration) на внешний IP.
        """
        destination_ip = random.choice(self.destination_ip)
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Windows", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["connection", "data_exfiltration"],
                "action": "outbound_data_transfer",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-DATA-EXF-001",
                    "name": "Simulated data exfiltration"
                }
            },
            "user": {"name": "attacker"},
            "process": {
                "name": "nc.exe", # Netcat как пример инструмента
                "pid": random.randint(10000, 20000),
                "executable": "C:\\Tools\\nc.exe"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": destination_ip,
                "port": random.randint(1, 65535)
            },
            "network": {
                "protocol": "tcp",
                "direction": "outbound"
            },
            "file": {
                "size": exfiltrated_data_size_bytes
            },
            "service": {
                "name": "Data Transfer",
                "type": "data_exfiltration"
            },
            "related": {
                "ip": [self.ip_addr, destination_ip],
                "user": ["attacker"]
            }
        }

    def living_off_the_land_powershell(self, target_command):
        """
        Генерирует событие использования PowerShell для выполнения вредоносной команды (Living-off-the-Land).
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Windows", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["process", "intrusion_detection"],
                "type": ["start", "malicious"],
                "action": "powershell_execution",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-LOT-PWSH-001",
                    "name": "Simulated Living-off-the-Land PowerShell execution"
                }
            },
            "user": {"name": "attacker"},
            "process": {
                "name": "powershell.exe",
                "pid": random.randint(10000, 20000),
                "executable": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "command_line": target_command
            },
            "service": {
                "name": "PowerShell",
                "type": "powershell"
            },
            "related": {
                "user": ["attacker"]
            }
        }

    def living_off_the_land_wmi(self, target_wmi_query):
        """
        Генерирует событие использования WMI для выполнения вредоносного запроса (Living-off-the-Land).
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Windows", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["process", "intrusion_detection"],
                "type": ["start", "malicious"],
                "action": "wmi_query_execution",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-LOT-WMI-001",
                    "name": "Simulated Living-off-the-Land WMI query execution"
                }
            },
            "user": {"name": "attacker"},
            "process": {
                "name": "wmic.exe",
                "pid": random.randint(10000, 20000),
                "executable": "C:\\Windows\\System32\\wbem\\wmic.exe",
                "command_line": target_wmi_query
            },
            "service": {
                "name": "WMI",
                "type": "wmi"
            },
            "related": {
                "user": ["attacker"]
            }
        }

    def cam_overflow(self, switch_ip, switch_port):
        """
        Генерирует событие атаки CAM-таблица overflow на коммутаторе.
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["security", "attack"],
                "action": "CAM table overflow launched",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-CAM-OVF-001",
                    "name": "Simulated CAM table flooding attack launched"
                }
            },
            "process": {
                "name": "macof",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/bin/macof"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": switch_ip,
                "port": switch_port
            },
            "network": {
                "protocol": "ethernet",
                "direction": "outbound"
            },
            "service": {
                "name": "CAM Overflow",
                "type": "switch_attack"
            },
            "related": {
                "ip": [self.ip_addr, switch_ip]
            }
        }

    def unauthorized_acl_modification(self, router_ip, target_acl_name):
        """
        Генерирует событие несанкционированного изменения ACL на маршрутизаторе.
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["configuration", "attack"],
                "action": "ACL modification launched",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-ACL-MOD-001",
                    "name": "Simulated unauthorized ACL modification launched"
                }
            },
            "process": {
                "name": "nmap",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/bin/nmap"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": router_ip,
                "port": 22 # SSH для конфигурации
            },
            "network": {
                "protocol": "tcp",
                "direction": "outbound"
            },
            "service": {
                "name": "Router ACL",
                "type": "router"
            },
            "related": {
                "ip": [self.ip_addr, router_ip]
            }
        }

    def stp_root_bridge_hijacking(self, switch_ip):
        """
        Генерирует событие атаки STP Root Bridge Hijacking на коммутаторе.
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["configuration", "attack"],
                "action": "STP Root Bridge Hijacking launched",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-STP-HIJACK-001",
                    "name": "Simulated STP Root Bridge Hijacking attack launched"
                }
            },
            "process": {
                "name": "yersinia",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/bin/yersinia"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": switch_ip,
                "port": 802 # STP порт
            },
            "network": {
                "protocol": "ethernet",
                "direction": "outbound"
            },
            "service": {
                "name": "STP",
                "type": "stp"
            },
            "related": {
                "ip": [self.ip_addr, switch_ip]
            }
        }

    def rogue_dhcp_server(self, target_subnet):
        """
        Генерирует событие запуска ложного DHCP-сервера (Rogue DHCP Server).
        """
        rogue_ip = f"{target_subnet}.{random.randint(100, 200)}"
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["service", "attack"],
                "action": "Rogue DHCP server launched",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-DHCP-ROGUE-001",
                    "name": "Simulated Rogue DHCP server launched"
                }
            },
            "process": {
                "name": "dhcpd",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/sbin/dhcpd"
            },
            "source": {
                "ip": rogue_ip, # IP, который будет раздавать фейковый DHCP
                "port": 67
            },
            "network": {
                "protocol": "udp",
                "direction": "outbound"
            },
            "service": {
                "name": "DHCP",
                "type": "dhcp"
            }
        }

    def route_injection(self, target_router_ip):
        """
        Генерирует событие атаки Route Injection на маршрутизаторе.
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["network", "intrusion_detection"],
                "type": ["routing", "attack"],
                "action": "Route injection launched",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-ROUTE-INJ-001",
                    "name": "Simulated Route injection attack launched"
                }
            },
            "process": {
                "name": "quagga",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/sbin/zebra"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": target_router_ip,
                "port": 179 # BGP
            },
            "network": {
                "protocol": "bgp",
                "direction": "outbound"
            },
            "service": {
                "name": "BGP",
                "type": "routing"
            },
            "related": {
                "ip": [self.ip_addr, target_router_ip]
            }
        }

    def snmp_bruteforce(self, target_router_ip, target_port=161):
        """
        Генерирует событие атаки SNMP Bruteforce на маршрутизаторе.
        """
        return {
            "@timestamp": self.get_timestamp(),
            "host": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "os": {"name": "Linux", "platform": "attack_tool"}
            },
            "observer": {
                "hostname": self.hostname,
                "ip": self.ip_addr,
                "type": "host"
            },
            "event": {
                "kind": "alert",
                "category": ["intrusion_detection", "network"],
                "type": ["access", "attack"],
                "action": "snmp_brute_force_launched",
                "outcome": "success",
                "severity": 1,
                "severity_label": "critical",
                "provider": "simulated-linux",
                "rule": {
                    "id": "ATT-SIM-SNMP-BF-001",
                    "name": "Simulated SNMP brute-force attack launched"
                }
            },
            "user": {"name": "attacker"},
            "process": {
                "name": "onesixtyone",
                "pid": random.randint(10000, 20000),
                "executable": "/usr/bin/onesixtyone"
            },
            "source": {
                "ip": self.ip_addr,
                "port": random.randint(32768, 65535)
            },
            "destination": {
                "ip": target_router_ip,
                "port": target_port
            },
            "network": {
                "protocol": "udp",
                "direction": "outbound"
            },
            "service": {
                "name": "SNMP",
                "type": "snmp"
            },
            "related": {
                "ip": [self.ip_addr, target_router_ip],
                "user": [self.user]
            }
        }
