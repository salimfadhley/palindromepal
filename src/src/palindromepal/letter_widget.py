from rich.align import Align
from rich.console import RenderableType
from rich.padding import Padding
from rich.panel import Panel
from rich.text import Text
from textual.reactive import Reactive
from textual.widget import Widget


class LetterWidget(Widget):
    label = Reactive("")
    content = Reactive("")

    def render(self) -> RenderableType:
        return Panel(Padding(
            Align.center(Text(text=self.content), vertical="middle"),
            (0, 1),
            style="white on rgb(51,51,51)",
        ))
