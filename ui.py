import base64
from tkinter import Tk, Label, Entry, Button, font, Frame, messagebox
from PIL import Image, ImageTk
import random, network, generator, datetime, json


import threading

class MainWindow(Tk):

    def __init__(self):
        super().__init__()

        # --- GENERATOR & NETWORK FIELDS ---

        self.is_generating = None
        self.generator_thread = None
        self.stop_event = None
        self.attacker_code = None
        self.segment_subnetwork_number = None
        self.random_link_image = None
        self.second_name = None
        self.id_student = None
        self.code_attack = None
        self.now = None
        self.buffer = ""

        self.is_get_task = False
        self.link_images = [
            "images/top-3A.jpg", "images/top-3AV.jpg", "images/top-3B.jpg", "images/top-3BV.jpg",
            "images/top-4A.jpg", "images/top-4AV.jpg", "images/top-4B.jpg", "images/top-4BV.jpg",
            "images/top-5A.jpg", "images/top-5AV.jpg", "images/top-5B.jpg", "images/top-5BV.jpg",
        ]
        self.users = []
        self.ip_address_list = []
        self.mac_address_list = []
        self.index_name = None

        # --- UI FIELDS ---

        self.app_font = font.Font(family="Courier New", size=14, weight="bold")
        self['bg'] = "darkgray"
        self.title("Электронный тренажер")
        self.geometry("1200x650")
        self.resizable(False, False)
        self.option_add("*Font", self.app_font)
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

        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        # --- SEPARATOR <Vertical> ---
        self.separator_auth = Frame(self, width=2, bg="black")
        self.separator_auth.place(x=350, y=0, height=900)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL <IP-ADDRESS> ---
        self.label_ip = Label(self, bg="darkgray", text="IP-адрес", anchor="e")
        self.label_ip.place(x=10, y=10, width=100, height=25)
        # --- ENTRY <IP-ADDRESS> ---
        self.entry_ip = Entry(self)
        self.entry_ip.place(x=110, y=10, width=200, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL <PORT> ---
        self.label_port = Label(self, bg="darkgray", text="Порт", anchor="e")
        self.label_port.place(x=10, y=45, width=100, height=25)
        # --- ENTRY <PORT> ---
        self.entry_port = Entry(self)
        self.entry_port.place(x=110, y=45, width=200, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL <LOGIN> ---
        self.label_login = Label(self, bg="darkgray", text="Логин", anchor="e")
        self.label_login.place(x=10, y=80, width=100, height=25)
        # --- ENTRY <LOGIN> ---
        self.entry_login = Entry(self)
        self.entry_login.place(x=110, y=80, width=200, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL <PASSWORD> ---
        self.label_password = Label(self, bg="darkgray", text="Пароль", anchor="e")
        self.label_password.place(x=10, y=115, width=100, height=25)
        # --- ENTRY <PASSWORD> ---
        self.entry_password = Entry(self, show="*")
        self.entry_password.place(x=110, y=115, width=200, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL`s <STATUS> ---
        self.label_status_logo_auth = Label(self, bg="darkgray", text="Статус:", anchor="e")
        self.label_status_logo_auth.place(x=10, y=150, width=100, height=25)
        self.label_status_auth = Label(self, bg="darkgray", text="*", anchor="e")
        self.label_status_auth.place(x=110, y=150, width=230, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- BUTTON <AUTH> ---
        self.button_auth = Button(self, text="Авторизация", command=self.auth_ui)
        self.button_auth.place(x=10, y=185, width=300, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- SEPARATOR <auth> ---
        self.separator_auth = Frame(self, height=2, bg="black")
        self.separator_auth.place(x=0, y=230, width=350)
        # --- --- --- --- --- --- --- --- --- ---

        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

        # --- LABEL <SECOND NAME> ---
        self.label_second_name = Label(self, bg="darkgray", text="Фамилия", anchor="e")
        self.label_second_name.place(x=10, y=250, width=100, height=25)
        # --- ENTRY <SECOND NAME> ---
        self.entry_second_name = Entry(self, state="disabled")
        self.entry_second_name.place(x=110, y=250, width=200, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL <ID> ---
        self.label_id = Label(self, bg="darkgray", text="ID", anchor="e")
        self.label_id.place(x=10, y=285, width=100, height=25)
        # --- ENTRY <ID> ---
        self.entry_id = Entry(self, state="disabled")
        self.entry_id.place(x=110, y=285, width=200, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL <ATTACK> ---
        self.label_attack = Label(self, bg="darkgray", text="Атака №", anchor="e")
        self.label_attack.place(x=10, y=320, width=100, height=25)
        # --- ENTRY <ATTACK> ---
        self.entry_attack = Entry(self, state="disabled")
        self.entry_attack.place(x=110, y=320, width=200, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- LABEL`s <STATUS> ---
        self.label_status_logo_create_index = Label(self, bg="darkgray", text="Статус:", anchor="e")
        self.label_status_logo_create_index.place(x=10, y=390, width=100, height=25)
        self.label_status_create_index = Label(self, bg="darkgray", text="*", anchor="e")
        self.label_status_create_index.place(x=110, y=390, width=230, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- BUTTON <CREATE INDEX> ---
        self.button_create_index = Button(self, text="Создать индекс", state="disabled", command=self.create_index_ui)
        self.button_create_index.place(x=10, y=355, width=300, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- SEPARATOR <create index> ---
        self.separator_auth = Frame(self, height=2, bg="black")
        self.separator_auth.place(x=0, y=420, width=350)
        # --- --- --- --- --- --- --- --- --- ---

        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

        # --- LABEL`s <TASK> ---
        self.label_task_logo = Label(self, bg="darkgray", text="Задание:", anchor="e")
        self.label_task_logo.place(x=55, y=425, width=100, height=25)
        self.label_task = Label(self, bg="darkgray",
                                text="1. Seg.1 | *.*.*.*/24\n2. Seg.2 | *.*.*.*/24\n3. Seg.3 | *.*.*.*/24\n4. Seg.4 | *.*.*.*/24\n5. Seg.5 | *.*.*.*/24",
                                anchor="w")
        self.label_task.place(x=10, y=450, width=280, height=25 * 5)
        # --- --- --- --- --- --- --- --- --- ---

        # --- BUTTON <GET TASK> ---
        self.button_get_task = Button(self, text="Получить задание", state="disabled", command=self.get_task_ui)
        self.button_get_task.place(x=10, y=575, width=300, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- BUTTON <GENERATION> ---
        self.button_generation = Button(self, text="Запустить генерацию", state="disabled", command=self.toggle_generation_protocols)
        self.button_generation.place(x=10, y=610, width=300, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

        # --- LABEL`s <PHOTO> ---
        self.label_photo = Label(self, anchor="n", state="disabled", text="Топология не задана!")
        self.label_photo.place(x=370, y=10, height=600, width=830)
        # --- --- --- --- --- --- --- --- --- ---

    def auth_ui(self):

        print(
            f"\t--- Auth ---\n"
            f"IP:{self.entry_ip.get().strip()}\n"
            f"Port:{self.entry_port.get().strip()}\n"
            f"Login:{self.entry_login.get().strip()}\n"
            f"Password:{self.entry_password.get().strip()}\n"
        )

        if self.entry_ip.get() == "" or self.entry_port.get() == "" or self.entry_login.get() == "" or self.entry_password.get() == "":
            self.label_status_auth.config(text="Поля пусты!")
            messagebox.showwarning("Проверка данных", "Поля данных пусты!")
        else:
            code, client = network.initialization_opensearch(self.entry_ip.get(), self.entry_port.get(),
                                                             self.entry_login.get(), self.entry_password.get())
            if code == 200:
                self.label_status_auth.config(text="Авторизация успешна!")
                self.label_second_name.config(state="normal")
                self.entry_second_name.config(state="normal")
                self.label_id.config(state="normal")
                self.entry_id.config(state="normal")
                self.label_attack.config(state="normal")
                self.entry_attack.config(state="normal")
                self.button_create_index.config(state="normal")
                self.client = client
            elif code == 401:
                self.label_status_auth.config(text="Проверьте IP-адрес!")
                messagebox.showwarning("Ошибка авторизации", "Проверьте указанный IP-адрес!")
            elif code == 404:
                self.label_status_auth.config(text="Ошибка авторизации!")
                messagebox.showwarning("Ошибка авторизации", "Поля данных неверны!")
            else:
                self.label_status_auth.config(text="Ошибка авторизации!")
                messagebox.showwarning("Ошибка авторизации", f"{code[1]}")

    def create_index_ui(self):

        self.second_name = self.entry_second_name.get().lower()
        self.id_student = self.entry_id.get()
        self.code_attack = self.entry_attack.get().strip()
        word = ""

        translit_map = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
            'э': 'e', 'ю': 'yu', 'я': 'ya'
        }

        for i in range(len(self.second_name.lower())):
            for key, value in translit_map.items():
                if self.second_name[i] == key:
                    word += value
                else:
                    continue

        self.index_name = word + '_' + str(self.id_student)
        self.label_status_create_index.config(text="Создание индекса")
        code = network.create_index_opensearch(
            client=self.client,
            index_name=self.index_name,
            index_mapping=self.index_mapping)
        if code == 200:
            self.label_status_create_index.config(text="Индекс создан   ")
            messagebox.showinfo(f"Индекс {self.index_name}", f"Индекс {self.index_name} создан!")
            self.button_get_task.config(state="normal")
        if code == 201:
            answer = messagebox.askquestion(f"Индекс {self.index_name}",
                                            f"Индекс {self.index_name} уже существует!\n Удалить индекс?")
            if answer == "yes":
                network.delete_index_opensearch(client=self.client,
                                                index_name=self.index_name)
                self.label_status_create_index.config(text="Индекс удален")
                messagebox.showinfo(f"Индекс {self.index_name}", f"Индекс {self.index_name} успешно удалён!")
                self.title("Электронный тренажер")
                self.button_get_task.config(state="disabled")
                self.button_generation.config(state="disabled")
            else:
                self.label_status_create_index.config(text="Индекс без изменений")
                messagebox.showinfo(f"Индекс {self.index_name}", f"Состояние индекса {self.index_name} не изменилось!")
                self.title("Электронный тренажер")
                self.button_get_task.config(state="normal")
                self.button_generation.config(state="disabled")

    def get_task_ui(self):

        change_window = ChangeWindow(self.app_font, self.client, self.index_name, self.index_mapping, self.users,
                                     self.ip_address_list, self.mac_address_list, self.attacker_code)
        change_window.mainloop()
        if change_window.type_of_job == "demo":
            print("DEMO!")
            self.title("Электронный тренажер - Демо версия")
            self.random_link_image = "images/top-3A.jpg"
            image = Image.open(self.random_link_image)
            topology = ImageTk.PhotoImage(image)
            self.label_photo.config(image=topology)
            self.label_photo.image = topology
            self.label_photo.config(state="normal")
            self.segment_subnetwork_number = []


            text_seg = ""
            for i in range(3):
                self.segment_subnetwork_number.append(random.randint(1, 50))
                text_seg += f"Seg.{i + 1} | 192.168.{self.segment_subnetwork_number[i]}.0/24\n"

            self.users, self.ip_address_list, self.mac_address_list, self.attacker_code = generator.generation_topology(
                "default/ssh_brute_force", self.segment_subnetwork_number, 1,1)
            self.label_task.config(text=text_seg)
            self.is_get_task = True
            self.button_get_task.config(state="disabled")
            self.button_generation.config(state="normal")

        else:
            print("PRACTISE!")
            self.title("Электронный тренажер - Практическая версия")
            self.random_link_image = random.choice(self.link_images)
            image = Image.open(self.random_link_image)
            topology = ImageTk.PhotoImage(image)
            self.label_photo.config(image=topology)
            self.label_photo.image = topology
            self.label_photo.config(state="normal")

            self.segment_subnetwork_number = []
            if "3" in self.random_link_image:
                print(f"3 Seg. {self.random_link_image}")
                for i in range(3):
                    self.segment_subnetwork_number.append(random.randint(1, 50))

            elif "4" in self.random_link_image:
                print(f"4 Seg. {self.random_link_image}")
                for i in range(4):
                    self.segment_subnetwork_number.append(random.randint(1, 50))
            else:
                print(f"5 Seg. {self.random_link_image}")
                for i in range(5):
                    self.segment_subnetwork_number.append(random.randint(1, 50))

            text_seg = ""
            for i in range(len(self.segment_subnetwork_number)):
                text_seg += f"Seg.{i + 1} | 192.168.{self.segment_subnetwork_number[i]}.0/24\n"

            self.users, self.ip_address_list, self.mac_address_list, self.attacker_code = generator.generation_topology(self.random_link_image, self.segment_subnetwork_number, self.code_attack, self.id_student)
            self.label_task.config(text=text_seg)
            self.is_get_task = True
            self.button_get_task.config(state="disabled")
            self.button_generation.config(state="normal")


    def toggle_generation_protocols(self):
        if self.is_generating:
            # Остановка
            self.stop_event.set()
            self.generator_thread.join(timeout=1.0)  # Ждём завершения (макс. 1 сек)
            self.is_generating = False
            self.button_generation.config(text="Запустить генерацию")
            self.writer_log()
            self.buffer = None
            print("! ОСТАНОВКА ГЕНЕРАЦИИ !")

        else:
            # Запуск
            self.stop_event = threading.Event()
            self.generator_thread = threading.Thread(
                target=generator.generator_protocols,
                args=(
                    self.client,
                    self.index_name,
                    self.users,
                    self.ip_address_list,
                    self.mac_address_list,
                    self.stop_event,
                    self.attacker_code,
                    self
                ),
                daemon=True  # Поток завершится при закрытии окна
            )
            self.generator_thread.start()
            self.is_generating = True
            self.button_generation.config(text="Остановить генерацию")
            self.write_header_log()
            print("! ЗАПУСК ГЕНЕРАЦИИ !")

    def writer_log(self):
            with open(f"{self.index_name}_{self.now.strftime('%d_%m_%Y')}_attacks.txt", mode="ab") as file:
                text = base64.b64encode(self.buffer.encode("utf-8"))
                file.write(text)
                file.close()

    def buffer_log(self, data = None, index = 0):
        self.buffer += f"\n[{index}][{datetime.datetime.now().strftime("%H:%M:%S")}]:{data}\n"


    def write_header_log(self):
        self.now = datetime.datetime.now()
        with open(f"{self.index_name}_{self.now.strftime('%d_%m_%Y')}.txt", mode="a", encoding="utf-8") as file:
            text = f"Индекс: {self.index_name}\nФамилия: {self.second_name}\nНомер ID: {self.id_student}\nВремя: {datetime.datetime.now().strftime("%H:%M:%S")}"
            file.write(text)
            file.close()

# --- FOR 2nd WINDOW ---

class ChangeWindow(Tk):

    def __init__(self,app_font, client, index_name, index_mapping, users, ip_address_list, mac_address_list, attacker_code):
        super().__init__()

        self.client = client
        self.index_name = index_name
        self.index_mapping = index_mapping
        self.users = users
        self.ip_address_list = ip_address_list
        self.mac_address_list = mac_address_list
        self.attacker_code = attacker_code
        self.type_of_job = None

        # --- UI FIELDS ---

        self.app_font = app_font
        self.title("Выбор режима подготовки")
        self.geometry("400x200")
        self['bg'] = "darkgray"
        self.option_add("*Font", self.app_font)
        self.resizable(False, False)

        # --- BUTTON <EASY GENERATION> ---

        self.button_easy_generation = Button(self, text="ДЕМО Версия", state="normal", command=self.demo_ui)
        self.button_easy_generation.place(x=25, y=50, width=150, height=50)

        # --- BUTTON <HARD GENERATION> ---
        self.button_hard_generation = Button(self, text="Практика", state="normal", command=self.practise_ui)
        self.button_hard_generation.place(x=225, y=50, width=150, height=50)


    def demo_ui(self):
        self.type_of_job = "demo"
        print(f"SET > Type of job: {self.type_of_job}")
        self.destroy()
        self.quit()


    def practise_ui(self):
        self.type_of_job = "practise"
        print(f"SET > Type of job: {self.type_of_job}")
        self.destroy()
        self.quit()


def main():
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    main()
