import opensearchpy
from opensearchpy import AuthenticationException

# --- Libraries ---

def initialization_opensearch(host , login , password):

    port = 9200
    auth = (login, password)
    try:
        client = opensearchpy.OpenSearch(
            hosts=[{'host': host, 'port': port}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=False,
            ssl_show_warn=False
        )

        info = client.info()
        print(f"OpenSearch Info: {info}")
        return 200, client

    except AuthenticationException:
        return 401, None
    except ConnectionError:
        return 400, None
    except Exception as e:
        print(f"Error:{e}")
        return [404, e],None


def create_index_opensearch(client, index_name, index_mapping):
    if not client.indices.exists(index=index_name):
        response = client.indices.create(index=index_name, body=index_mapping)
        print(f"Индекс {index_name} создан")
        return 200
    else:
        print(f"Индекс {index_name} уже существует!")
        return 201


def insert_index_opensearch(client, index_name, index_data):
    client.index(index=index_name, body=index_data)
    print("Документ добавлен")


def delete_index_opensearch(client, index_name):
    client.indices.delete(index=index_name)
    print(f"Индекс {index_name} удалён")
