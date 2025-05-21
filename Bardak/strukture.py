# ────────────────────────────────────────────────────────────────
# Вспомогательные функции и структуры данных проекта (если есть)
# ────────────────────────────────────────────────────────────────
import os

EXCLUDE_DIRS = {'venv', '__pycache__', '.git', '.idea', '.mypy_cache', '.pytest_cache', 'logs', '.vscode', '.DS_Store'}
EXCLUDE_FILES = {'.DS_Store'}

def print_tree(start_path='.', prefix=''):
    entries = sorted(os.listdir(start_path))
    entries = [e for e in entries if e not in EXCLUDE_FILES]

    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        if os.path.isdir(path) and entry not in EXCLUDE_DIRS:
            is_last = index == len(entries) - 1
            print(f"{prefix}{'└── ' if is_last else '├── '}{entry}/")
            new_prefix = prefix + ('    ' if is_last else '│   ')
            print_tree(path, new_prefix)
        elif os.path.isfile(path):
            print(f"{prefix}{'└── ' if index == len(entries) - 1 else '├── '}{entry}")

if __name__ == '__main__':
    print("📂 Структура проекта:\n")
    print_tree()
