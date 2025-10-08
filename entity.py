import random
from datetime import datetime, timezone

class Device:

    def __init__(
        self,
        hostname:str ,
        ip_addr: str,
        mac_addr: str,
        role:str,
        log_format:str,
        asset_tag:str
    ):

        self.hostname = hostname
        self.ip_addr = ip_addr
        self.mac_addr = mac_addr
        self.role = role
        self.log_format = log_format
        self.asset_tag = asset_tag


    @staticmethod
    def get_timestamp() -> str:
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        return timestamp

    def get_ip_addr(self):
        return self.ip_addr

    def get_mac_addr(self):
        return self.mac_addr

    def show_info(self):
        print(f"___ {self.__class__.__name__} ___")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
        print(
            "_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")






class PersonalComputer(Device):

    def __init__(
            self,
            hostname:str,
            ip_addr:str,
            mac_addr:str,
            role:str,
            log_format:str,
            os:str,
            domain:str,
            asset_tag:str
    ):

        super().__init__(
            hostname,
            ip_addr,
            mac_addr,
            role,
            log_format,
            asset_tag
        )

        self.ip_addr = ip_addr
        self.mac_addr = mac_addr
        self.os = os
        self.domain = domain
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

        if self.os == "Linux":
            self.software_attr = [
                {"bash": 1}, # FACILITY
                {"libreoffice": 1},
                {"yandex-stable": 1},
                {"thunderbird": 2},
                {"rsync": 1},
                {"python3": 16},
                {"konsole": 1},
                {"nautilus": 1},
                {"ssh": 8}
            ]
            self.users_attr = {
                "root" ,  # Суперпользователь
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
                f"user-{self.asset_tag.replace('IN-', '')}"
                "auditd"
            }

            # ATTR FILESYSTEM
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
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.bash_history",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.ssh/id_rsa",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.ssh/authorized_keys",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.config/",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.mozilla/firefox/",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.cache/",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/Documents/",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/Downloads/",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.local/share/applications/"
            ]
            self.tmp_files_attr = [
                "/tmp/",
                "/var/tmp/",
                "/run/",
                "/dev/shm/",
                f"/home/user-{self.asset_tag.replace('IN-', '')}/.cache/"
            ]
            self.socket_files_attr = [
                "/run/systemd/private",
                "/run/dbus/system_bus_socket",
                "/var/run/",
                "/tmp/.X11-unix/"
            ]

        else:
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
            self.software_attr = [
                {"explorer.exe" : 1},
                {"yandex.exe" : 1},
                {"powershell.exe" : 16},
                {"cmd.exe" : 16},
                {"notepad.exe" : 1},
                {"HxCalendarAppImm.exe" : 2},
                {"Acrobat.exe" : 1},
                {"7-zip.exe" : 1},
                {"MsMpEng.exe" : 17}
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
                f"user-{self.asset_tag.replace('IN-', '')}"
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

    # AUTH - SEVRITY

    def auth_info(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return f"<{8*8+6}>\t1 {self.get_timestamp()} {self.hostname} sshd {random.randint(115,1999)} -- Accepted publickey for alice from {random.choice(other_ips)}"

    def auth_warning(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return f"<{8 * 8+4}>\t1 {self.get_timestamp()} {self.hostname} sshd {random.randint(115, 1999)} -- Failed password for root from {random.choice(other_ips)}"

    def auth_crit(self, list_ip_addr):
        other_ips = [ip for ip in list_ip_addr if ip != self.get_ip_addr()] + self.destination_ip
        return f"<{8 * 8+2}>\t1 {self.get_timestamp()} {self.hostname} sshd {random.randint(115, 1999)} -- Possible break-in attempt from {random.choice(other_ips)}"

    # START PROCESS - SEVERITY
    def start_process_info(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        all_files_attr = self.software_files_attr
        return f"<{8*facility+facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- execve(\"{random.choice(all_files_attr)}\")"

    def start_process_warning(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        all_files_attr = self.software_files_attr
        return f"<{8 * facility+facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- Suspicious process: \"{random.choice(all_files_attr)}\""

    def start_process_debug(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return f"<{8 * facility+facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- Debug: spawning process for user user-{self.asset_tag.replace('IN-', '')}"

    # OPEN FILE - SEVERITY

    def open_file_info(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return f"<{8 * facility+facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- name={random.choice(all_files_attr)}"

    def open_file_warning(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return f"<{8 * facility+facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- Access to {random.choice(all_files_attr)} by user user-{self.asset_tag.replace('IN-', '')}"

    def open_file_crit(self):
        all_files_attr = self.home_files_attr + self.config_files_attr + self.socket_files_attr + self.system_files_attr
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return f"<{8 * facility + facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- Critical: {second_app_name}"

    # NETWORK ACTIVITY - SEVERITY

    def network_activity_info(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        return f"<{8 * facility + facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- OUT src={self.get_ip_addr()} dst={random.choice(self.destination_ip)} dport={random.randint(8080,25500)}"

    def network_activity_warning(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return f"<{8 * facility + facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- OUT to {second_app_name} IP {random.choice(self.destination_ip)}"

    def network_activity_debug(self):
        severity_software = random.choice(self.software_attr)
        app_name = list(severity_software.keys())[0]
        facility = severity_software[app_name]
        second_software = random.choice(self.software_attr)
        second_app_name = list(second_software.keys())[0]
        return f"<{8 * facility + facility}>\t1 {self.get_timestamp()} {self.hostname} {app_name} {random.randint(115, 1999)} -- TCP: connect({self.get_ip_addr()}:{random.randint(8080,26500)} -> {random.choice(self.destination_ip)}:443)"

    # EDIT POLICIES - SEVERITY

    def edit_policies_notice(self):
        if self.os == "Linux":
            app = "systemd"
        else:
            app = "GroupPolicy"
        return f"<{8 * 1 + 1}>\t1 {self.get_timestamp()} {self.hostname} {app} -- Applied computer policy settings"

    def edit_policies_warning(self):
        if self.os == "Linux":
            app = "systemd"
        else:
            app = "GroupPolicy"
        return f"<{8 * 1 + 1}>\t1 {self.get_timestamp()} {self.hostname} {app} -- Failed to apply security policy"

    def edit_policies_info(self):
        if self.os == "Linux":
            app = "systemd"
        else:
            app = "GroupPolicy"
        return f"<{8 * 1 + 1}>\t1 {self.get_timestamp()} {self.hostname} {app} -- Reloading security policies"

    def remote_control_info(self):
        return f"<{8 * 1 + 4}>\t1 {self.get_timestamp()} {self.hostname} TermService -- RDP connection from {self.get_ip_addr()} accepted"

    def remote_control_warning(self):
        return f"<{8 * 1 + 4}>\t1 {self.get_timestamp()} {self.hostname} TermService -- RDP logon failed for user user-{self.asset_tag.replace('IN-', '')}"

    def remote_control_alert(self):
        return f"<{8 * 1 + 4}>\t1 {self.get_timestamp()} {self.hostname} Security -- Multiple RDP brute-force attempts detected"

    # UPDATE SYSTEM - SEVERITY

    def update_system_info(self):
        if self.os == "Linux":
            severity_software = random.choice(self.software_attr)
            app_name = list(severity_software.keys())[0]
            return f"<{8 * 1 + 15}>\t1 {self.get_timestamp()} {self.hostname} apt {random.randint(115, 1999)} -- Installed package: {app_name}"
        else:
            severity_software = random.choice(self.software_attr)
            app_name = list(severity_software.keys())[0]
            return f"<{8 * 1 + 15}>\t1 {self.get_timestamp()} {self.hostname} WindowsUpdate {random.randint(115, 1999)} -- Installed package: {app_name}"

    def update_system_err(self):
        if self.os == "Linux":
            return f"<{8 * 1 + 15}>\t1 {self.get_timestamp()} {self.hostname} apt {random.randint(115, 1999)} -- Failed to download updates"
        else:
            return f"<{8 * 1 + 15}>\t1 {self.get_timestamp()} {self.hostname} WindowsUpdate {random.randint(115, 1999)} -- Failed to download updates"

    def update_system_notice(self):
        if self.os == "Linux":
            return f"<{8 * 1 + 15}>\t1 {self.get_timestamp()} {self.hostname} apt {random.randint(115, 1999)} -- Security update KB{random.randint(1000,9999)}{random.randint(100,999)} installed"
        else:
            return f"<{8 * 1 + 15}>\t1 {self.get_timestamp()} {self.hostname} WindowsUpdate {random.randint(115, 1999)} -- Security update KB{random.randint(1000,9999)}{random.randint(100,999)} installed"

    def get_init(self) -> str:
        return f"___ Personal Computer ___\nhostname : {self.hostname}\nip_addr : {self.ip_addr}\nmac_addr : {self.mac_addr}\nrole : {self.role}\nlog_format : {self.log_format}\nos : {self.os}\ndomain : {self.domain}\nasset_tag : {self.asset_tag}\n___________________________\n"
    def get_attr(self) -> str:
        return f"___ Personal Computer Attr___\nSoftware Attr : {self.software_attr}\nUsers Attr : {self.users_attr}\n"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Switch(Device):

    def __init__(
            self,
            hostname:str,
            ip_addr:str,
            mac_addr:str,
            role:str,
            log_format:str,
            os:str,
            domain:str,
            asset_tag:str
                  ):
        super().__init__(
            hostname,
            ip_addr,
            mac_addr,
            role,
            log_format,
            asset_tag
        )

        self.ip_addr = ip_addr
        self.mac_addr = mac_addr
        self.os = os
        self.domain = domain
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

    # CHANGE STATUS PORT - SEVERITY

    def change_status_port_info(self):
        return f"<{8 * 21 + random.randint(10,16)}>\t1 {self.get_timestamp()} {self.hostname} LINK-UPDOWN -- Interface {random.choice(self.port)} changed state to up"

    def change_status_port_warning(self):
        return f"<{8 * 21 + + random.randint(10,16)}>\t1 {self.get_timestamp()} {self.hostname} LINK-FLAP -- Interface {random.choice(self.port)} flapping"

    def change_status_port_crit(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} HWIC-PORT_FAIL -- Hardware failure on {random.choice(self.port)}"

    # LEARN MAC ADDR - SEVERITY
    def learn_mac_addr_info(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} MAC-LEARN -- MAC {random.choice(other_mac)} learned on {random.choice(self.port)}"

    def learn_mac_addr_warning(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} MAC-MOVE -- MAC {random.choice(other_mac)} move from {random.choice(self.port)} to {random.choice(self.port)}"

    def learn_mac_addr_debug(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} MAC-TABLE -- MAC table entry added {random.choice(other_mac)}"

    # VIOLATION PORT SECURITY - SEVERITY

    def violation_port_security_warning(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} PORTSEC-VIOLATION -- Security violation on {random.choice(self.port)}"

    def violation_port_security_crit(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} PORTSEC-CAM_FLOOD -- CAM table overflow attack detected"

    def violation_port_security_alert(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} SECURITY-COMPROMISE -- Unauthorized device connected"

    # STP EVENT - SEVERITY

    def stp_event_info(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} STP-PORTSTATE -- Port {random.choice(self.port)} to forwarding"

    def stp_event_warning(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} STP-TOPOLOGY_CHANGE -- Topology change detected"

    def stp_event_crit(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} STP-LOOP_DETECTED -- Network loop detected on VLAN {random.randint(2,19)}"

    # DUPLEX ERROR - SEVERITY

    def duplex_error_warning(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} INTERFACE-CRC -- CRC errors on {random.choice(self.port)}"

    def duplex_error_err(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} PHY-DUPLEX_MISMATCH -- Duplex mismatch on {random.choice(self.port)}"

    def duplex_error_crit(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} HWIC-HARDWARE_ERR -- Physical layer failure on {random.choice(self.port)}"

    # VLAN EVENT - SEVERITY

    def vlan_event_info(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} VLAN-ASSIGN -- Port {random.choice(self.port)} assigned to VLAN {random.randint(2,19)}"

    def vlan_event_warning(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} VLAN-NATIVE_MISMATCH -- Native VLAN mismatch on {random.choice(self.port)}"

    def vlan_event_debug(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} VLAN-DEBUG -- VLAN membership updated for {random.choice(self.port)}"

    # AUTH 802.1X - SEVERITY

    def auth_802_1x_info(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} DOT1X-SUCCESS -- Auth succeeded for MAC {random.choice(other_mac)}"

    def auth_802_1x_warning(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} DOT1X-FAIL -- Auth failed for MAC {random.choice(other_mac)}"

    def auth_802_1x_alert(self, list_mac_addr):
        other_mac = [mac for mac in list_mac_addr if mac != self.get_mac_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} DOT1X-ATTACK -- EAPOL flood attack detected"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Router(Device):

    def __init__(self,
            hostname:str,
            ip_addr:str,
            mac_addr:str,
            role:str,
            log_format:str,
            os:str,
            domain:str,
            asset_tag:str ):

        super().__init__(
            hostname,
            ip_addr,
            mac_addr,
            role,
            log_format,
            asset_tag
        )

        self.ip_addr = ip_addr
        self.mac_addr = mac_addr
        self.os = os
        self.domain = domain
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

    # CHANGE STATUS INTERFACE - SEVERITY
    def change_status_int_info(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} LINEPROTO-UPDOWN -- {random.choice(self.port)} changed state to up"

    def change_status_int_warning(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} INTERFACE-FLAP -- {random.choice(self.port)} flapping"

    def change_status_int_crit(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} HWIC-LINK_FAIL -- Carrier loss on {random.choice(self.port)}"

    # CHANGE ROADMAP - SEVERITY

    def change_roadmap_info(self,list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} IP-ROUTE -- Route {random.choice(self.destination_ip+other_ip)} added"

    def change_roadmap_warning(self,list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} IP-ROUTE_FLAP -- Route {random.choice(self.destination_ip+other_ip)} flapping"

    def change_roadmap_alert(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} IP-ROUTING_LOSS -- All default routes lost"

    # DYNAMIC ROUTING EVENT - SEVERITY

    def dynamic_routing_event_info(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} OSPF-ADJCHG -- Nbr {random.choice(self.destination_ip)} from DOWN to FULL"

    def dynamic_routing_event_warning(self,list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} BGP-ADJCHANGE -- Neighbor {random.choice(other_ip)} Down"

    def dynamic_routing_event_crit(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} OSPF-PROTOCOL_ERR -- OSPF checksum error on {random.choice(self.port)}"

    # ACL ACTIVITY - SEVERITY

    def acl_activity_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ACL-PERMIT -- Permitted tcp from {random.choice(other_ip)} to {random.choice(self.destination_ip)}"

    def acl_activity_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ACL-DENIED -- Denied tcp from {random.choice(self.destination_ip)} to {random.choice(other_ip)}"

    def acl_activity_debug(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ACL-MATCH -- Matched rule {random.randint(100,187)}: permit {random.choice(['tcp', 'udp'])} {random.choice(self.port + ['any'])} {random.choice(self.port + ['any'])} eq {random.choice([20,21,22,23,25,53,80,8080,110,135,143,443,445,993,9600,9200,3306,5432])}"

    # NAT EVENT - SEVERITY

    def nat_event_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} NAT-ADDR -- Translated {random.choice(other_ip)} to {random.choice(self.destination_ip)}"

    def nat_event_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} NAT-POOL_EXHAUSTED -- NAT pool exhausted"

    def nat_event_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} NAT-DEBUG -- NAT entry created: {random.choice(other_ip)}:{random.randint(100,65500)} to {random.choice(self.destination_ip)}:{random.randint(100,65500)}"

    # ICMP MESSAGE - SEVERITY

    def icmp_message_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ICMP-ECHO -- Echo reply sent to {random.choice(other_ip)}"

    def icmp_message_warning(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ICMP-DSTUNREACH -- Destination {random.choice(other_ip)} unreachable"

    def icmp_message_debug(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ICMP-DEBUG -- Received ICMP type {random.randint(3,12)} from {random.choice(other_ip)}"

    # VIOLATION TRAFFIC -  SEVERITY

    def violation_traffic_info(self, list_ip_addr):
        other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} QOS-CLASSIFIED -- Traffic from {random.choice(other_ip)} classified as {random.choice(['VOICE','VIDEO CONF','BUSINESS-DATA','EFFORT'])}"

    def violation_traffic_warning(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} QOS-RATE_EXCEEDED -- Rate limit exceeded on {random.choice(self.port)} "

    def violation_traffic_debug(self):
        return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} QOS-DEBUG -- Packet marked with {random.choice(['DSCP','COS'])}"

    
class FireWall(Device):
        
        def __init__(
            self,
            hostname:str,
            ip_addr:str,
            mac_addr:str,
            role:str,
            log_format:str,
            os:str,
            domain:str,
            asset_tag:str ):

            super().__init__(
                hostname,
                ip_addr,
                mac_addr,
                role,
                log_format,
                asset_tag
            )
            self.ip_addr = ip_addr
            self.mac_addr = mac_addr
            self.os = os
            self.domain = domain
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

        # ALLOW TRAFFIC -  SEVERITY
        def allow_traffic_info(self, list_ip_addr):
            other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ASA-302013 -- Built TCP connection for outside: {random.choice(self.destination_ip)} to inside: {random.choice(other_ip)}"

        def allow_traffic_debug(self, list_ip_addr):
            other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} PAN-SESSION -- Session created: src={random.choice(self.destination_ip)}, dst={random.choice(other_ip)}, app={random.choice(['ssh','ssl','tls','http','telnet'])}"

        # LOCK TRAFFIC - SEVERITY

        def lock_traffic_warning(self,list_ip_addr):
            other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ASA-106015 -- Deny {random.choice(['tcp','udp'])} src outside:{random.choice(self.destination_ip)}, dst inside:{random.choice(other_ip)}"

        def lock_traffic_alert(self, list_ip_addr):
            other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} PAN-THREAT -- Critical threat: Exploit attempt blocked"

        def lock_traffic_debug(self):
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} FW-RULE_MATCH -- Matched rule 'block-external-{random.choice(['ssh', 'ssl', 'tls', 'http', 'telnet'])}'"

        # CHANGE STATUS SESSION - SEVERITY

        def change_session_info_connect(self,list_ip_addr):
            other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ASA-6-302013 -- Built {random.choice(['TCP','UDP'])} connection {random.randint(1000,20000)}"

        def change_session_info_breakup(self,list_ip_addr):
            other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} ASA-6-302014 -- Teardown {random.choice(['TCP','UDP'])} connection {random.randint(1000,20000)} duration {random.randint(60,600)}sec"

        def change_session_debug(self,list_ip_addr):
            other_ip = [ip for ip in list_ip_addr if ip != self.get_ip_addr()]
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} FW-SESSION -- Session stats: bytes_in={random.randint(10000,200000)}, bytes_out= {random.randint(10000,200000)}"

        # VPN TUNNEL - SEVERITY

        def vpn_tunnel_info(self):
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} IPSEC-VPNUP -- VPN tunnel to {random.choice(self.destination_ip)} established"

        def vpn_tunnel_warning(self):
            return f"<{8 * 21 + + random.randint(10, 16)}>\t1 {self.get_timestamp()} {self.hostname} IPSEC-VPNDOWN -- VPN tunnel to {random.choice(self.destination_ip)} disconnected"
