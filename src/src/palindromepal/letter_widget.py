from rich.align import Align
from rich.console import RenderableType
from rich.padding import Padding
from rich.text import Text
from textual.reactive import Reactive
from textual.widget import Widget


class LetterWidget(Widget):

    label = Reactive("")

    def render(self) -> RenderableType:
        return Padding(
            Align.center(Text(text=self.label), vertical="middle"),
            (0, 1),
            style="white on rgb(51,51,51)",
        )
