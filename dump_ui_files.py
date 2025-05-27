"""
Скрипт собирает все .py и .kv файлы из папки Bardak/ui и
выгружает их в один файл со структурой: путь, имя файла и содержимое.
"""

import os

OUTPUT_FILE = "ui_dump.txt"
TARGET_EXTENSIONS = (".py", ".kv")
ROOT_DIR = "Bardak/ui"

def dump_ui_files():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for root, dirs, files in os.walk(ROOT_DIR):
            for file in files:
                if file.endswith(TARGET_EXTENSIONS):
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, ROOT_DIR)

                    out.write("─" * 80 + "\n")
                    out.write(f"ФАЙЛ: {relative_path}\n")
                    out.write("─" * 80 + "\n\n")

                    with open(full_path, "r", encoding="utf-8") as f:
                        out.write(f.read())
                        out.write("\n\n")

    print(f"Готово! Все файлы собраны в: {OUTPUT_FILE}")

if __name__ == "__main__":
    dump_ui_files()
