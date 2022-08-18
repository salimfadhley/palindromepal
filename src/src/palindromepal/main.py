

from textual.app import App
from textual import events
from textual.widgets import Placeholder, Header, Footer

from palindromepal.input_text_widget import InputTextWidget


class SimpleApp(App):

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("ctrl-q", "quit", "Quit")

    async def on_mount(self) -> None:
        await self.view.dock(Header(), edge="top", size=1)
        await self.view.dock(Footer(), edge="bottom", size=1)
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(InputTextWidget(), Placeholder(), edge="top")


SimpleApp.run(log="textual.log")