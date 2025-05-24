# ────────────────────────────────────────────────────────────────
# # Bardak/logger_configs/collector_logs.py
# ────────────────────────────────────────────────────────────────

from Bardak.configs import config_raw
from Bardak.configs.logger_configs.log_parser import smart_parse_log
from Bardak.configs.logger_configs.write_db import write_log_to_db
import os


LOG_FILES = {
    os.path.join(config_raw.LOG_DIR,'info.log'),
    os.path.join(config_raw.LOG_DIR,'error.log')
}

def collect_log() -> None:
    """Читает строки из лог-файла и пишет их в БД"""
    try:
        for path in LOG_FILES:
            with open(path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    log = smart_parse_log(line)
                    if log:
                        write_log_to_db(log)
                    else:
                        print(f"⚠️  Строка {line_num} не распознана: {line.strip()}")
    except FileNotFoundError:
        print(f"❌ Лог-файл не найден по пути: {path}")

collect_log()