# OPENSEARCH

## 1. Скачать .deb OpenSearch

``` bash
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=MySecret123@ && dpkg -i opensearch-3.2.0-linux-x64.deb
```
## 2. Установка .deb
``` bash
sudo dpkg -i opensearch-<version>-linux-x64.deb
```

## 3. Редактирование `opensearch.yml`

``` bash
sudo nano /etc/opensearch/opensearch.yml
```

### `/etc/opensearch/opensearch.yml`
``` yaml
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
network.host: 0.0.0.0
discovery.type: single-node
```
## 4. Включить сервис
``` bash
sudo systemctl enable --now opensearch
sudo systemctl status opensearch
```

## 5. ==(Опционально)== Тест работоспособности OpenSearch
``` bash
 curl -X GET https://localhost:9200 -u 'admin:MySecret123@' --insecure
```

---
# OPENSEARCH DASHBOARDS

## 1. Установка .deb
``` bash
sudo dpkg -i opensearch-dashboards-3.2.0-linux-x64.deb
```
## 2. Редактирование `opensearch_dashboards.yml`
``` bash
sudo nano /etc/opensearch-dashboards/opensearch_dashboards.yml
```
### `opensearch_dashboards.yml`
``` yaml
server.host: 0.0.0.0
opensearch.user: admin
opensearch.password: MySecret123@
```
## 3. Перезагрузка daemon и запуск сервиса OpenSearch Dashboards
``` bash
sudo systemctl daemon-reload
sudo systemctl enable --now opensearch-dashboards
sudo systemctl status opensearch-dashboards
```
---
