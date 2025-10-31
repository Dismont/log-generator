import opensearchpy


# --- Libraries ---

def initialization_opensearch():
    index_name = input("Enter index name: ")
    index_mapping = {
        "settings": {
            "index": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            }
        },
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date",
                    "format": "strict_date_optional_time||epoch_millis"
                },
                "host": {
                    "properties": {
                        "hostname": {"type": "keyword"}
                    }
                },
                "process": {
                    "properties": {
                        "name": {"type": "keyword"},
                        "pid": {"type": "integer"}
                    }
                },
                "event": {
                    "properties": {
                        "action": {"type": "keyword"},
                        "category": {"type": "keyword"},
                        "type": {"type": "keyword"},
                        "outcome": {"type": "keyword"},
                        "severity": {"type": "integer"}
                    }
                },
                "user": {
                    "properties": {
                        "name": {"type": "keyword"}
                    }
                },
                "source": {
                    "properties": {
                        "ip": {"type": "ip"}
                    }
                }
            }
        }
    }

    host = input("Enter IP-address: ")
    port = 9200
    auth = ('admin', 'MySecret123@')

    client = opensearchpy.OpenSearch(
        hosts=[{'host': host, 'port': port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=False,
        ssl_show_warn=False
    )

    # info = client.info()
    # print(f"OpenSearch Info: {info}")

    return client, index_name, index_mapping


def create_index_opensearch(client, index_name, index_mapping) -> None:
    if not client.indices.exists(index=index_name):
        response = client.indices.create(index=index_name, body=index_mapping)
        print("Индекс создан ...")

    else:
        print("Индекс уже существует!")


def insert_index_opensearch(client, index_name, index_data):
    client.index(index=index_name, body=index_data)
    print("Документ добавлен")


def delete_index_opensearch(client, index_name):
    client.indices.delete(index=index_name)
    print(f"Индекс {index_name} удалён")
