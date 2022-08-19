from rich.console import RenderableType
from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Header, Placeholder
from textual_inputs import TextInput

from palindromepal import __version__ as version
from palindromepal.output_text_widget import OutputTextWidget


class SimpleApp(App):
    palindrome: Reactive[RenderableType] = Reactive("A man, a plan, a canal – Panama!")

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("escape", "quit", "Quit")

    async def on_mount(self) -> None:
        await self.view.dock(Header(), edge="top", size=1)
        await self.view.dock(Footer(), edge="bottom", size=1)
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(
            TextInput(
                name="input",
                placeholder="wite a palindrome here...",
                content=self.palindrome,
                title="Palindrome",
            ),
            OutputTextWidget(text="Hello"),
            edge="top",
        )


SimpleApp.run(title=f"Palindrome Pal v{version}")
