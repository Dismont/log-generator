# ПК (Endpoint) ✅
## Аутентификация✅
info (6) — успешный вход:
<134>1 2024-06-15T10:00:00Z pc01 sshd 1234 - - Accepted publickey for alice from 192.168.1.100
warning (4) — неудачная попытка:
<132>1 2024-06-15T10:01:00Z pc01 sshd 1235 - - Failed password for root from 203.0.113.50
crit (2) — множественные неудачи (возможный брут):
<130>1 2024-06-15T10:02:00Z pc01 sshd 1236 - - Possible break-in attempt from 203.0.113.50
## Запуск процесса✅
**info** (6) — обычный запуск:
<134>1 2024-06-15T10:10:00Z pc01 auditd 2001 - - execve("/usr/bin/firefox", [...])
**warning** (4) — подозрительный процесс:
<132>1 2024-06-15T10:11:00Z pc01 auditd 2002 - - Suspicious process: /tmp/.malware
**debug** (7) — отладка запуска:
<135>1 2024-06-15T10:12:00Z pc01 systemd 1 - - Debug: spawning process for user alice
## Доступ к файлам✅
**info** (6) — обычный доступ:
<134>1 2024-06-15T10:20:00Z pc01 auditd 2003 - - name="/home/alice/report.docx"
**warning** (4) — доступ к чувствительным файлам:
<132>1 2024-06-15T10:21:00Z pc01 auditd 2004 - - Access to /etc/shadow by user bob
**crit (2)** — изменение системных файлов:
<130>1 2024-06-15T10:22:00Z pc01 auditd 2005 - - Critical: /bin/bash modified
## Сетевая активность✅
info (6) — обычное соединение:
<134>1 2024-06-15T10:30:00Z pc01 netflow - - OUT src=192.168.1.10 dst=8.8.8.8 dport=53
warning (4) — подозрительный IP:
<132>1 2024-06-15T10:31:00Z pc01 netflow - - OUT to known-malicious IP 198.51.100.100
debug (7) — детали соединения:
<135>1 2024-06-15T10:32:00Z pc01 kernel - - TCP: connect(192.168.1.10:50000 -> 8.8.8.8:443)
## Изменение политик✅
**notice** (5) — применение политик:
<133>1 2024-06-15T10:40:00Z pc-win GroupPolicy - - Applied computer policy settings
**warning** (4) — ошибка применения:
<132>1 2024-06-15T10:41:00Z pc-win GroupPolicy - - Failed to apply security policy
**info** (6) — обновление политик:
<134>1 2024-06-15T10:42:00Z pc-linux systemd - - Reloading security policies
## Удалённое управление✅
**info** (6) — успешное подключение:
<134>1 2024-06-15T10:50:00Z pc-win TermService - - RDP connection from 192.168.10.50 accepted
**warning** (4) — неудачная попытка:
<132>1 2024-06-15T10:51:00Z pc-win TermService - - RDP logon failed for user admin
**alert** (1) — атака на RDP:
<129>1 2024-06-15T10:52:00Z pc-win Security - - Multiple RDP brute-force attempts detected
## Обновления / Патчи✅
**info** (6) — успешная установка:
<134>1 2024-06-15T11:00:00Z pc-linux apt 3001 - - Installed package: firefox 125.0
**err** (3) — ошибка обновления:
<131>1 2024-06-15T11:01:00Z pc-linux apt 3002 - - Failed to download updates
**notice** (5) — обновление безопасности:
<133>1 2024-06-15T11:02:00Z pc-win WindowsUpdate - - Security update KB1234567 installed

# Коммутатор✅
## Изменение состояния порта✅
**info** (6) — порт up/down:
<189>1 2024-06-15T11:10:00Z sw01 LINK-3-UPDOWN - - Interface Gi1/0/5, changed state to up
**warning** (4) — частые переключения:
<188>1 2024-06-15T11:11:00Z sw01 LINK-4-FLAP - - Interface Gi1/0/5 flapping
**crit** (2) — отказ порта:
<186>1 2024-06-15T11:12:00Z sw01 HWIC-2-PORT_FAIL - - Hardware failure on Gi1/0/5
## Изучение MAC-адреса✅
**info** (6) — обычное изучение:
<189>1 2024-06-15T11:20:00Z sw01 MAC-4-LEARN - - MAC 00:11:22:33:44:55 learned on Gi1/0/5
**warning** (4) — перемещение MAC:
<188>1 2024-06-15T11:21:00Z sw01 MAC-4-MOVE - - MAC moved from Gi1/0/3 to Gi1/0/7
**debug** (7) — отладка таблицы:
<191>1 2024-06-15T11:22:00Z sw01 MAC-7-TABLE - - MAC table entry added: 00:11:22:33:44:55
## Нарушение безопасности порта✅
**warning** (4) — стандартное нарушение:
<188>1 2024-06-15T11:30:00Z sw01 PORTSEC-2-VIOLATION - - Security violation on Gi1/0/5
**crit** (2) — атака на CAM-таблицу:
<186>1 2024-06-15T11:31:00Z sw01 PORTSEC-2-CAM_FLOOD - - CAM table overflow attack detected
**alert** (1) — компрометация:
<185>1 2024-06-15T11:32:00Z sw01 SECURITY-1-COMPROMISE - - Unauthorized device connected
## STP-события✅
**info** (6) — изменение состояния:
<189>1 2024-06-15T11:40:00Z sw01 STP-5-PORTSTATE - - Port Gi1/0/1 to forwarding
**warning** (4) — топология изменилась:
<188>1 2024-06-15T11:41:00Z sw01 STP-4-TOPOLOGY_CHANGE - - Topology change detected
**crit** (2) — петля в сети:
<186>1 2024-06-15T11:42:00Z sw01 STP-2-LOOP_DETECTED - - Network loop detected on VLAN 1
## Ошибки дуплекса / CRC✅
**warning** (4) — ошибки CRC:
<188>1 2024-06-15T11:50:00Z sw01 INTERFACE-4-CRC - - CRC errors on Gi1/0/10
**err** (3) — дуплекс-несовпадение:
<187>1 2024-06-15T11:51:00Z sw01 PHY-3-DUPLEX_MISMATCH - - Duplex mismatch on Gi1/0/15
**crit** (2) — аппаратная ошибка:
<186>1 2024-06-15T11:52:00Z sw01 HWIC-2-HARDWARE_ERR - - Physical layer failure on Gi1/0/20
## VLAN-события✅
**info** (6) — назначение VLAN:
<189>1 2024-06-15T12:00:00Z sw01 VLAN-5-ASSIGN - - Port Gi1/0/5 assigned to VLAN 10
**warning** (4) — несоответствие native VLAN:
<188>1 2024-06-15T12:01:00Z sw01 VLAN-4-NATIVE_MISMATCH - - Native VLAN mismatch on Gi1/0/1
**debug** (7) — отладка VLAN:
<191>1 2024-06-15T12:02:00Z sw01 VLAN-7-DEBUG - - VLAN membership updated for Gi1/0/5
## Аутентификация (802.1X)✅
info (6) — успешная аутентификация:
<189>1 2024-06-15T12:10:00Z sw01 DOT1X-5-SUCCESS - - Auth succeeded for MAC 00:11:22:33:44:55
warning (4) — неудачная попытка:
<188>1 2024-06-15T12:11:00Z sw01 DOT1X-4-FAIL - - Auth failed for MAC aa:bb:cc:dd:ee:ff
alert (1) — атака на 802.1X:
<185>1 2024-06-15T12:12:00Z sw01 DOT1X-1-ATTACK - - EAPOL flood attack detected

# Маршрутизатор✅
## Изменение состояния интерфейса✅
info (6) — интерфейс up/down:
<189>1 2024-06-15T12:20:00Z rtr01 LINEPROTO-5-UPDOWN - - Gi0/1 changed state to up
warning (4) — нестабильность:
<188>1 2024-06-15T12:21:00Z rtr01 INTERFACE-4-FLAP - - Gi0/1 flapping
crit (2) — отказ линка:
<186>1 2024-06-15T12:22:00Z rtr01 HWIC-2-LINK_FAIL - - Carrier loss on Gi0/2
## Изменение маршрутов✅
info (6) — добавление маршрута:
<189>1 2024-06-15T12:30:00Z rtr01 IP-5-ROUTE - - Route 10.10.0.0/16 added
warning (4) — нестабильность маршрута:
<188>1 2024-06-15T12:31:00Z rtr01 IP-4-ROUTE_FLAP - - Route 10.10.0.0/16 flapping
alert (1) — потеря маршрутизации:
<185>1 2024-06-15T12:32:00Z rtr01 IP-1-ROUTING_LOSS - - All default routes lost
## События динамической маршрутизации✅
info (6) — сосед появился:
<189>1 2024-06-15T12:40:00Z rtr01 OSPF-5-ADJCHG - - Nbr 10.0.0.2 from DOWN to FULL
warning (4) — сосед пропал:
<188>1 2024-06-15T12:41:00Z rtr01 BGP-4-ADJCHANGE - - Neighbor 192.0.2.1 Down
crit (2) — сбой протокола:
<186>1 2024-06-15T12:42:00Z rtr01 OSPF-2-PROTOCOL_ERR - - OSPF checksum error on Gi0/1
## ACL-срабатывания✅
info (6) — разрешение:
<189>1 2024-06-15T12:50:00Z rtr01 ACL-5-PERMIT - - Permitted tcp from 192.168.1.10 to 8.8.8.8
warning (4) — блокировка:
<188>1 2024-06-15T12:51:00Z rtr01 ACL-4-DENIED - - Denied tcp from 203.0.113.50 to 192.168.10.5
debug (7) — детали ACL:
<191>1 2024-06-15T12:52:00Z rtr01 ACL-7-MATCH - - Matched rule 101: permit tcp any any eq 80
## NAT-события✅
info (6) — создание трансляции:
<189>1 2024-06-15T13:00:00Z rtr01 NAT-5-ADDR - - Translated 192.168.10.10 to 203.0.113.1
warning (4) — исчерпание пула:
<188>1 2024-06-15T13:01:00Z rtr01 NAT-4-POOL_EXHAUSTED - - NAT pool exhausted
debug (7) — отладка NAT:
<191>1 2024-06-15T13:02:00Z rtr01 NAT-7-DEBUG - - NAT entry created: 192.168.10.10:50000 → 203.0.113.1:50000
## ICMP-сообщения✅
info (6) — echo reply:
<189>1 2024-06-15T13:10:00Z rtr01 ICMP-5-ECHO - - Echo reply sent to 192.168.1.20
warning (4) — недоступность:
<188>1 2024-06-15T13:11:00Z rtr01 ICMP-4-DSTUNREACH - - Destination 192.168.20.10 unreachable
debug (7) — отладка ICMP:
<191>1 2024-06-15T13:12:00Z rtr01 ICMP-7-DEBUG - - Received ICMP type 8 from 192.168.1.20
## QoS / Политики трафика✅
info (6) — классификация:
<189>1 2024-06-15T13:20:00Z rtr01 QOS-5-CLASSIFIED - - Traffic from 192.168.1.10 classified as VOICE
warning (4) — превышение лимита:
<188>1 2024-06-15T13:21:00Z rtr01 QOS-4-RATE_EXCEEDED - - Rate limit exceeded on Gi0/0
debug (7) — отладка QoS:
<191>1 2024-06-15T13:22:00Z rtr01 QOS-7-DEBUG - - Packet marked with DSCP EF

# Межсетевой экран (FW)✅
## Разрешение трафика✅
info (6) — разрешённый трафик:
<134>1 2024-06-15T13:30:00Z fw01 ASA-6-302013 - - Built TCP connection for outside:203.0.113.50 to inside:192.168.10.20
debug (7) — детали сессии:
<135>1 2024-06-15T13:31:00Z fw01 PAN-7-SESSION - - Session created: src=203.0.113.50, dst=192.168.10.20, app=ssl
## Блокировка трафика✅
warning (4) — стандартная блокировка:
<132>1 2024-06-15T13:40:00Z fw01 ASA-4-106015 - - Deny tcp src outside:203.0.113.50 dst inside:192.168.10.5
alert (1) — атака:
<129>1 2024-06-15T13:41:00Z fw01 PAN-1-THREAT - - Critical threat: Exploit attempt blocked
debug (7) — отладка правила:
<135>1 2024-06-15T13:42:00Z fw01 FW-7-RULE_MATCH - - Matched rule 'block-external-ssh'
## Установка/разрыв сессии✅
info (6) — создание сессии:
<134>1 2024-06-15T14:00:00Z fw01 ASA-6-302013 - - Built TCP connection 12345
info (6) — разрыв сессии:
<134>1 2024-06-15T14:01:00Z fw01 ASA-6-302014 - - Teardown TCP connection 12345 duration 120s
debug (7) — детали сессии:
<135>1 2024-06-15T14:02:00Z fw01 FW-7-SESSION - - Session stats: bytes_in=1024, bytes_out=2048
## Изменение политики❌
notice (5) — применение изменений:
<133>1 2024-06-15T14:10:00Z fw01 PAN-5-CONFIG - - Admin committed policy changes
warning (4) — ошибка конфигурации:
<132>1 2024-06-15T14:11:00Z fw01 ASA-4-111008 - - Error in ACL 'block-test': syntax error
info (6) — экспорт конфигурации:
<134>1 2024-06-15T14:12:00Z fw01 FW-6-CONFIG - - Configuration backup initiated
## Туннели / VPN✅
info (6) — туннель установлен:
<134>1 2024-06-15T14:20:00Z fw01 IPSEC-6-VPNUP - - VPN tunnel to 203.0.113.250 established
warning (4) — туннель разорван:
<132>1 2024-06-15T14:21:00Z fw01 IPSEC-4-VPNDOWN - - VPN tunnel to 203.0.113.250 disconnected
alert (1) — атака на VPN:
<129>1 2024-06-15T14:22:00Z fw01 SSLVPN-1-ATTACK - - Brute-force attack on SSL VPN detected
## DoS-защита❌
alert (1) — активация защиты:
<129>1 2024-06-15T14:30:00Z fw01 DOS-1-ATTACK - - SYN flood attack detected from 203.0.113.200
warning (4) — подозрительный трафик:
<132>1 2024-06-15T14:31:00Z fw01 DOS-4-PROTECTION - - High rate of ICMP packets from 198.51.100.100
crit (2) — перегрузка системы:
<130>1 2024-06-15T14:32:00Z fw01 DOS-2-SYSTEM_OVERLOAD - - DoS protection causing high CPU usage

# Пример конвертации syslog в JSON ✅
### 🖥️ **ПК: Аутентификация (SSH)**

**Syslog**: 
`<70>1 2025-10-08T21:44:46Z PC-1 sshd 896 -- Accepted publickey for alice from 40.126.35.10`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "PC-1"},
  "process": {"name": "sshd", "pid": 896},
  "event": {
    "action": "user_login",
    "category": "authentication",
    "type": ["start", "access"],
    "outcome": "success",
    "severity": 6
  },
  "user": {"name": "alice"},
  "source": {"ip": "40.126.35.10"}
}
```

---

### 🖥️ **ПК: Неудачный вход**

**Syslog**:  
`<68>1 2025-10-08T21:44:46Z PC-1 sshd 1135 -- Failed password for root from 34.102.136.180`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "PC-1"},
  "process": {"name": "sshd", "pid": 1135},
  "event": {
    "action": "user_login",
    "category": "authentication",
    "outcome": "failure",
    "severity": 4
  },
  "user": {"name": "root"},
  "source": {"ip": "34.102.136.180"}
}
```

---

### 🖥️ **ПК: Подозрительная активность**

**Syslog**:  
`<66>1 2025-10-08T21:44:46Z PC-1 sshd 1079 -- Possible break-in attempt from 8.8.8.8`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "PC-1"},
  "process": {"name": "sshd", "pid": 1079},
  "event": {
    "action": "intrusion_attempt",
    "category": "intrusion_detection",
    "outcome": "failure",
    "severity": 2
  },
  "source": {"ip": "8.8.8.8"}
}
```

---

### 🖥️ **ПК: Запуск процесса**

**Syslog**:  
`<18>1 2025-10-08T21:44:46Z PC-1 thunderbird 1841 -- execve("/usr/bin/rsync")`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "PC-1"},
  "process": {"name": "thunderbird", "pid": 1841},
  "event": {
    "action": "process_started",
    "category": "process",
    "severity": 6
  },
  "process": {
    "executable": "/usr/bin/rsync",
    "name": "rsync"
  }
}
```

> ⚠️ Здесь `process.name` в корне — это **родительский процесс** (`thunderbird`), а вложенный `process` — **дочерний** (`rsync`).  
> В ECS для дочернего процесса используется `process.parent.*`, но для простоты можно оставить так.

---

### 🖥️ **ПК: Доступ к файлу**

**Syslog**:  
`<72>1 2025-10-08T21:44:46Z PC-1 ssh 1565 -- name=/var/log/samba/`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "PC-1"},
  "process": {"name": "ssh", "pid": 1565},
  "event": {
    "action": "file_access",
    "category": "file",
    "severity": 6
  },
  "file": {"path": "/var/log/samba/"}
}
```

---

### 🖥️ **ПК: Сетевая активность**

**Syslog**:  
`<144>1 2025-10-08T21:44:46Z PC-1 python3 1316 -- OUT src=192.168.10.3 dst=173.194.222.108 dport=9230`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "PC-1"},
  "process": {"name": "python3", "pid": 1316},
  "event": {
    "action": "network_connection",
    "category": "network",
    "severity": 6
  },
  "source": {"ip": "192.168.10.3"},
  "destination": {"ip": "173.194.222.108", "port": 9230},
  "network": {"protocol": "tcp"}
}
```

---

### 📡 **Коммутатор: Изменение состояния порта**

**Syslog**:  
`<180>1 2025-10-08T21:44:46Z SW-1 LINK-UPDOWN -- Interface Fa1/6 changed state to up`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "SW-1"},
  "event": {
    "action": "interface_state_change",
    "category": "network",
    "severity": 6
  },
  "interface": {"name": "Fa1/6", "state": "up"}
}
```

---

### 📡 **Коммутатор: Нарушение безопасности**

**Syslog**:  
`<181>1 2025-10-08T21:44:46Z SW-1 PORTSEC-VIOLATION -- Security violation on Fa1/7`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "SW-1"},
  "event": {
    "action": "port_security_violation",
    "category": "intrusion_detection",
    "severity": 4
  },
  "interface": {"name": "Fa1/7"}
}
```

---

### 🌐 **Маршрутизатор: ACL-блокировка**

**Syslog**:  
`<180>1 2025-10-08T21:44:46Z RT-1 ACL-DENIED -- Denied tcp from 13.107.246.10 to 192.168.10.27`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "RT-1"},
  "event": {
    "action": "denied",
    "category": "network",
    "outcome": "failure",
    "severity": 4
  },
  "source": {"ip": "13.107.246.10"},
  "destination": {"ip": "192.168.10.27"},
  "network": {"protocol": "tcp"}
}
```

---

### 🛡️ **Firewall: Разрешение трафика**

**Syslog**:  
`<181>1 2025-10-08T21:44:46Z FW-1 ASA-302013 -- Built TCP connection for outside: 91.189.91.83 to inside: 192.168.10.10`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "FW-1"},
  "event": {
    "action": "connection_established",
    "category": "network",
    "outcome": "success",
    "severity": 6
  },
  "source": {"ip": "91.189.91.83", "zone": "outside"},
  "destination": {"ip": "192.168.10.10", "zone": "inside"},
  "network": {"protocol": "tcp"}
}
```

---

### 🛡️ **Firewall: Блокировка угрозы**

**Syslog**:  
`<184>1 2025-10-08T21:44:46Z FW-1 PAN-THREAT -- Critical threat: Exploit attempt blocked`

**JSON**:
```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "FW-1"},
  "event": {
    "action": "blocked",
    "category": "intrusion_detection",
    "severity": 1
  },
  "threat": {"name": "Exploit attempt"}
}
```

---

## 📌 Общая структура JSON (ECS)

```json
{
  "@timestamp": "2025-10-08T21:44:46Z",
  "host": {"hostname": "..."},
  "process": {"name": "...", "pid": 1234},
  "event": {
    "action": "...",
    "category": "...",
    "severity": N,
    "outcome": "success|failure" (если применимо)
  },
  // Дополнительные поля в зависимости от категории:
  "user": {"name": "..."},
  "source": {"ip": "...", "port": N},
  "destination": {"ip": "...", "port": N},
  "file": {"path": "..."},
  "interface": {"name": "..."},
  "threat": {"name": "..."}
}