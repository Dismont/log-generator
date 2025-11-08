from tkinter import Tk, Label, Entry, Button, font, Frame, messagebox
from PIL import Image, ImageTk
import random
import network
import generator


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.segment_subnetwork_number = None
        self.random_link_image = None
        self.app_font = font.Font(family="Courier New", size=14, weight="bold")
        self['bg'] = "darkgray"
        self.title("Электронный тренажер")
        self.geometry("1200x650")
        self.resizable(False, False)
        self.option_add("*Font", self.app_font)
        self.is_get_task = False
        self.link_images = [
            "images/top-3A.jpg", "images/top-3AV.jpg", "images/top-3B.jpg", "images/top-3BV.jpg",
            "images/top-4A.jpg", "images/top-4AV.jpg", "images/top-4B.jpg", "images/top-4BV.jpg",
            "images/top-5A.jpg", "images/top-5AV.jpg", "images/top-5B.jpg", "images/top-5BV.jpg",
        ]
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

        # --- LABEL`s <STATUS> ---
        self.label_status_logo_create_index = Label(self, bg="darkgray", text="Статус:", anchor="e")
        self.label_status_logo_create_index.place(x=10, y=320, width=100, height=25)
        self.label_status_create_index = Label(self, bg="darkgray", text="*", anchor="e")
        self.label_status_create_index.place(x=110, y=320, width=230, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- BUTTON <CREATE INDEX> ---
        self.button_create_index = Button(self, text="Создать индекс", state="disabled", command=self.create_index_ui)
        self.button_create_index.place(x=10, y=355, width=300, height=25)
        # --- --- --- --- --- --- --- --- --- ---

        # --- SEPARATOR <create index> ---
        self.separator_auth = Frame(self, height=2, bg="black")
        self.separator_auth.place(x=0, y=400, width=350)
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
        self.button_generation = Button(self, text="Генерация", state="disabled", command=self.generation_ui)
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

        second_name = self.entry_second_name.get().lower()
        id_student = self.entry_id.get()
        word = ""

        translit_map = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
            'э': 'e', 'ю': 'yu', 'я': 'ya'
        }

        for i in range(len(second_name.lower())):
            for key, value in translit_map.items():
                if second_name[i] == key:
                    word += value
                else:
                    continue

        index_name = word + '_' + str(id_student)
        self.label_status_create_index.config(text="Создание индекса")
        code = network.create_index_opensearch(
            client=self.client,
            index_name=index_name,
            index_mapping=self.index_mapping)
        if code == 200:
            self.label_status_create_index.config(text="Индекс создан")
            messagebox.showinfo(f"Индекс {index_name}", f"Индекс {index_name} создан!")
            self.button_get_task.config(state="normal")
        if code == 201:
            answer = messagebox.askquestion(f"Индекс {index_name}",
                                            f"Индекс {index_name} уже существует!\n Удалить индекс?")
            if answer == "yes":
                network.delete_index_opensearch(client=self.client,
                                                index_name=index_name)
                self.label_status_create_index.config(text="Индекс удален")
                messagebox.showinfo(f"Индекс {index_name}", f"Индекс {index_name} успешно удалён!")
                self.button_get_task.config(state="disabled")
            else:
                self.label_status_create_index.config(text="Индекс без изменений")
                messagebox.showinfo(f"Индекс {index_name}", f"Состояние индекса {index_name} не изменилось!")
                self.button_get_task.config(state="normal")

    def get_task_ui(self):
        self.random_link_image = random.choice(self.link_images)
        image = Image.open(self.random_link_image)
        topology = ImageTk.PhotoImage(image)
        self.label_photo.config(image=topology)
        self.label_photo.image = topology
        self.label_photo.config(state="normal")

        self.segment_subnetwork_number = []
        if "3" in self.random_link_image:
            print("3 сегмента")
            for i in range(3):
                self.segment_subnetwork_number.append(random.randint(1, 50))

        elif "4" in self.random_link_image:
            print("4 сегмента!")
            for i in range(4):
                self.segment_subnetwork_number.append(random.randint(1, 50))
        else:
            print("5 сегментов!")
            for i in range(5):
                self.segment_subnetwork_number.append(random.randint(1, 50))

        text_seg = ""
        for i in range(len(self.segment_subnetwork_number)):
            text_seg += f"Seg.{i + 1} | 192.168.{self.segment_subnetwork_number[i]}.0/24\n"

        self.label_task.config(text=text_seg)

        self.is_get_task = True
        self.button_get_task.config(state="disabled")
        self.button_generation.config(state="normal")

    def generation_ui(self):

        generator.generation_topology(self.random_link_image, self.segment_subnetwork_number)


def main():
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    main()
