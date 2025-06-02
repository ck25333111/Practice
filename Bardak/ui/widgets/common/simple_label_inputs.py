# ────────────────────────────────────────────────────────────────
# Файл: ui/widgets/common/simple_label_inputs.py
# Назначение: Заглушка для SimpleLabelInputs, чтобы kv мог его распознать
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "simple_label_inputs.kv"))


class SimpleLabelInputs(BoxLayout):
    """Пустой класс-заглушка для kv, без логики."""
    pass