import tkinter as tk
from tkinter import font
from tkinter import messagebox
import network

class AuthWindow:

    def __init__(self,root, app_font):

        self.root = root
        self.app_font = app_font
        self.root.geometry("400x500")
        self.root.title("Генератор")
        self.root['bg'] = "grey"
        self.root.option_add("*Font", self.app_font)
        # --- IP-ADDRESS ---

        self.label_ip = tk.Label(self.root,text="IP-адрес")
        self.label_ip.place(x=30,y=50,height=25,width=90)
        self.label_ip['bg'] = "grey"

        self.edit_ip = tk.Entry(self.root)
        self.edit_ip.place(x=150,y=50,height=25,width=200)

        # --- PORT ---

        self.label_port = tk.Label(self.root,text="Порт")
        self.label_port.place(x=30,y=100,height=25,width=90)
        self.label_port['bg'] = "grey"

        self.edit_port = tk.Entry(self.root)
        self.edit_port.place(x=150,y=100,height=25,width=200)

        # --- LOGIN ---

        self.label_login = tk.Label(self.root,text="Логин")
        self.label_login.place(x=30,y=150,height=25,width=90)
        self.label_login['bg'] = "grey"

        self.edit_login = tk.Entry(self.root)
        self.edit_login.place(x=150,y=150,height=25,width=200)

        # --- PASSWORD ---

        self.label_password = tk.Label(self.root,text="Пароль")
        self.label_password.place(x=30,y=200,height=25,width=90)
        self.label_password['bg'] = "grey"

        self.edit_password = tk.Entry(self.root,show="*")
        self.edit_password.place(x=150,y=200,height=25,width=200)

        # --- LOGIN <BUTTON> ---

        self.button_auth = tk.Button(self.root, text="Авторизация", command=self.auth_ui)
        self.button_auth.place(x=70, y=250,  height=30, width=270)

        # --- CHECK_SERVER <BUTTON> ---

        self.button_check = tk.Button(self.root, text="Проверка сервера", command=self.check_server_ui)
        self.button_check.place(x=70, y=300, height=30, width=270)

        # --- STATUS ---

        self.label_status_text = tk.Label(self.root, text="Статус: ")
        self.label_status_text.place(x=30, y=350, height=25, width=100)
        self.label_status_text['bg'] = "grey"

        self.label_status = tk.Label(self.root, text=" * ", anchor="w")
        self.label_status.place(x=130, y=350, height=25, width=250)
        self.label_status['bg'] = "grey"


    def auth_ui(self):
        if self.edit_ip.get() == "" or  self.edit_port.get() == "" or self.edit_login.get() == "" or self.edit_password.get() == "":
            messagebox.showwarning("Проверка данных", "Поля данных пусты!")
        else:
            self.label_status.config(text="Авторизация")
            print(
                f"\t--- Auth ---\n"
                f"IP:{self.edit_ip.get().strip()}\n"
                f"Port:{self.edit_port.get().strip()}\n"
                f"Login:{self.edit_login.get().strip()}\n"
                f"Password:{self.edit_password.get().strip()}\n"
            )
            code, client = network.initialization_opensearch(
                host=self.edit_ip.get().strip(),
                login=self.edit_login.get().strip(),
                password=self.edit_password.get().strip())

            if code == 200:
                self.label_status.config(text="Авторизация успешна!")
                new_root = tk.Toplevel(self.root)
                create_index = CreateIndex(new_root,client,self.app_font)

            elif code == 401:
                messagebox.showwarning("Ошибка авторизации", "Проверьте указанный IP-адрес!")
            elif code == 404:
                messagebox.showwarning("Ошибка авторизации", "Поля данных неверны!")
            else:
                messagebox.showwarning("Ошибка авторизации", f"{code[1]}")

    def check_server_ui(self):
        if self.edit_ip.get() == "" or  self.edit_port.get() == "" or self.edit_login.get() == "" or self.edit_password.get() == "":
            messagebox.showwarning("Проверка данных", "Поля данных пусты!")
        else:
            self.label_status.config(text="Проверка сервера")
            print(
                f"\t--- Check Server ---\n"
                f"\t___ Data ___\n"
                f"> IP:{self.edit_ip.get().strip()}\n"
                f"> Port:{self.edit_port.get().strip()}\n"
                f"> Login:{self.edit_login.get().strip()}\n"
                f"> Password:{self.edit_password.get().strip()}\n")



class CreateIndex:

    def __init__(self, root, client, app_font):

        self.client = client
        self.index_mapping = {
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
        self.root = root
        self.app_font = app_font
        self.root['bg'] = "grey"
        self.root.geometry("400x500")
        self.root.title("Создание индекса")
        self.root.option_add("*Font", self.app_font)

        # --- SECOND NAME ---

        self.label_second_name = tk.Label(self.root, text="Фамилия")
        self.label_second_name.place(x=30, y=50, height=25, width=90)
        self.label_second_name['bg'] = "grey"

        self.edit_second_name = tk.Entry(self.root)
        self.edit_second_name.place(x=150, y=50, height=25, width=200)

        # --- ID ---

        self.label_ID = tk.Label(self.root, text="ID")
        self.label_ID.place(x=30, y=100, height=25, width=90)
        self.label_ID['bg'] = "grey"

        self.edit_ID = tk.Entry(self.root)
        self.edit_ID.place(x=150, y=100, height=25, width=200)

        # --- CREATE <BUTTON> ---

        self.button_check = tk.Button(self.root, text="Создать индекс", command=self.create_index_ui)
        self.button_check.place(x=70, y=300, height=30, width=270)

        # --- STATUS ---

        self.label_status_text = tk.Label(self.root, text="Статус: ")
        self.label_status_text.place(x=30, y=350, height=25, width=100)
        self.label_status_text['bg'] = "grey"

        self.label_status = tk.Label(self.root, text=" * ", anchor="w")
        self.label_status.place(x=130, y=350, height=25, width=250)
        self.label_status['bg'] = "grey"

    def create_index_ui(self):

        second_name = self.edit_second_name.get().lower()
        id_student = self.edit_ID.get()
        word = ""

        translit_map = {
                'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
                'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
                'э': 'e', 'ю': 'yu', 'я': 'ya'
        }

        for i in range(len(second_name.lower())):
            for key,value in translit_map.items():
                if second_name[i] == key:
                    word += value
                else: continue

        index_name = word + '_' + str(id_student)
        self.label_status.config(text="Создание индекса")
        code = network.create_index_opensearch(client=self.client,
                                        index_name=index_name,
                                        index_mapping=self.index_mapping)
        if code == 200:
            self.label_status.config(text="Индекс создан")
            messagebox.showinfo(f"Индекс {index_name}", f"✅ Индекс {index_name} создан!")
        if code == 201:
            answer = messagebox.askquestion(f"Индекс {index_name}", f"Индекс {index_name} уже существует!\n Удалить индекс?")
            if answer == "yes":
                network.delete_index_opensearch(client=self.client,
                                                index_name=index_name)
                self.label_status.config(text="Индекс удален")
                messagebox.showinfo(f"Индекс {index_name}", f"✅ Индекс {index_name} успешно удалён!")
            else:
                self.label_status.config(text="Индекс без изменений")
                messagebox.showinfo(f"Индекс {index_name}", f"Состояние индекса {index_name} не изменилось!")



def main():
    root = tk.Tk()
    app_font = font.Font(family="Courier New", size=14, weight="bold")
    app = AuthWindow(root, app_font)
    root.mainloop()

if __name__ == "__main__":
    main()


