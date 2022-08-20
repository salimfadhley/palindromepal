import logging
import re

from rich.console import RenderableType
from textual.app import App
from textual.keys import Keys
from textual.reactive import Reactive, watch
from textual.widgets import Footer, Header, Placeholder
from textual_inputs import TextInput

from palindromepal import __version__ as version
from palindromepal.letter_widget import LetterWidget
from palindromepal.output_text_widget import OutputTextWidget
from palindromepal.text_widget import TextWidget


log = logging.getLogger(__name__)


class SimpleApp(App):
    live: Reactive[bool] = Reactive(False)

    async def action_toggle_live(self)->None:
        log.info("Toggling live!")
        self.live = not self.live


    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("escape", "quit", "Quit")
        await self.bind(Keys.ControlR, "refresh_palindrome", "Refresh")
        await self.bind(Keys.ControlL, "toggle_live", "Live")

    async def on_mount(self) -> None:

        self.text_output = TextWidget(name="A")
        self.text_output.title = "AAA"
        self.text_output.text = ""

        self.text_input = TextInput(
            name="input",
            placeholder="write a palindrome here...",
            content="",
            title="Palindrome",
        )



        watch(self.text_input, "value", self.watch_palindrome)


        await self.view.dock(Header(), edge="top", size=1)
        await self.view.dock(Footer(), edge="bottom", size=1)
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(
            self.text_input,
            self.text_output,
            edge="top",
        )

    async def watch_palindrome(self, value) -> None:
        self.text_output.text = " ".join(re.split("\s+", value[::-1]))


def main():
    SimpleApp.run(title=f"Palindrome Pal v{version}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
