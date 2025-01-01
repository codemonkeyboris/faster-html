from abc import ABC, abstractmethod
from fasthtml.common import *


class DropdownMenu(ABC):
    def __init__(
        self,
        options,
        cls="dropdown",
        width="200px",
        background_color="#fff",
        border="1px solid #ccc",
        padding="10px",
        color="black",
        font_size="14px",
    ):
        """
        Abstract DropdownMenu class requiring subclasses to implement `on_change`.

        :param options: List of options to display in the dropdown.
        :param cls: CSS class name.
        :param width: Width of the dropdown.
        :param background_color: Background color for the dropdown.
        :param border: Border for the dropdown.
        :param padding: Padding for the dropdown.
        :param color: Text color for the options.
        :param font_size: Font size for the options.
        """
        self.options = options
        self.cls = cls
        self.styles = {
            "width": width,
            "background-color": background_color,
            "border": border,
            "padding": padding,
            "color": color,
            "font-size": font_size,
        }

    @property
    @abstractmethod
    def on_change(self):
        """Abstract property to define option-to-JavaScript mappings."""
        pass

    def render(self):
        """Render the dropdown as a select element with options."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())

        # Generate JavaScript for onchange event
        onchange_js = """
        const actions = {
            %s
        };
        const selectedValue = this.value;
        if (actions[selectedValue]) {
            actions[selectedValue]();
        }
        """ % ", ".join(
            f"'{key}': () => {{ {action} }}" for key, action in self.on_change.items()
        )

        # Create <Option> elements for each option in the dropdown menu
        options_html = [Option(option, value=option) for option in self.options]

        # Generate the <select> element with dynamic onchange handling
        select_element = Select(
            *options_html,
            cls=self.cls,
            style=style,
            onchange=onchange_js,
        )
        return select_element


##################################################
# Subclass Example


class CustomDropdownMenu(DropdownMenu):
    def __init__(self, options):
        super().__init__(options)

    @property
    def on_change(self):
        """Define individual event handler functions for each option."""
        return {
            "Option 1": "alert('Custom handler for Option 1!')",
            "Option 2": "alert('Custom handler for Option 2!')",
            "Option 3": "console.log('Custom handler for Option 3!')",
        }


##################################################
# Example Usage


def example_dropdown_menu():
    """Create an instance of CustomDropdownMenu."""
    dropdown = CustomDropdownMenu(
        options=["Option 1", "Option 2", "Option 3"],
    )
    return dropdown.render()


# FastHTML app example
app, rt = fast_app()


@rt("/")
async def index():
    dropdown_content = example_dropdown_menu()

    return Div(
        H1("DropdownMenu with Abstract Event Handlers"),
        dropdown_content,
        cls="container",
    )


if __name__ == "__main__":
    serve()
