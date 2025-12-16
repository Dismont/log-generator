import tkinter as tk
from tkinter import filedialog, messagebox
import base64
import os

def decode_base64_file():
    # Открываем диалог выбора файла
    filepath = filedialog.askopenfilename(
        title="Выберите файл для декодирования (Base64)",
        filetypes=[("Base64 файлы", "*.txt *.b64"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return  # Пользователь отменил выбор

    try:
        # Читаем файл как текст (Base64 — это ASCII-совместимая строка)
        with open(filepath, "r", encoding="utf-8") as f:
            b64_data = f.read()

        # Удаляем пробелы и переносы (на случай, если они есть)
        b64_clean = ''.join(b64_data.split())

        # Декодируем из Base64
        decoded_bytes = base64.b64decode(b64_clean, validate=True)

        # Определяем путь для сохранения
        dir_name = os.path.dirname(filepath)
        base_name = os.path.basename(filepath)
        name, ext = os.path.splitext(base_name)
        output_path = os.path.join(dir_name, f"{name}_decoded{ext}")

        # Сохраняем декодированные данные как бинарный файл
        with open(output_path, "wb") as f:
            f.write(decoded_bytes)

        messagebox.showinfo("Успех", f"Файл успешно декодирован!\nСохранён как:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось декодировать файл:\n{str(e)}")

# Создаём главное окно
root = tk.Tk()
root.title("Base64 Декодер")
root.geometry("300x120")
root.resizable(False, False)

# Центрируем окно
root.eval('tk::PlaceWindow . center')

# Кнопка
btn = tk.Button(
    root,
    text="Выбрать и декодировать файл",
    command=decode_base64_file,
    font=("Arial", 10),
    padx=20,
    pady=10
)
btn.pack(expand=True)

# Запуск GUI
root.mainloop()