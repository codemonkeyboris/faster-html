from fasthtml.common import *

class DropdownMenu:
    def __init__(
        self,
        options,
        on_change=None,  # Dictionary of onchange events for specific options
        cls="dropdown",
        width="200px",
        background_color="#fff",
        border="1px solid #ccc",
        padding="10px",
        color="black",
        font_size="14px",
    ):
        """
        Initialize a DropdownMenu with options and customizable styles.

        :param options: List of options to display in the dropdown.
        :param on_change: Optional dictionary mapping options to JavaScript actions.
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
        self.on_change = on_change or {}

    def render(self):
        """Render the dropdown as a select element with options."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())

        # Generate a JavaScript onchange handler that maps values to actions
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
# Example usage of DropdownMenu with Events

def example_dropdown_menu():
    """Create a DropdownMenu example with options."""
    dropdown = DropdownMenu(
        options=["Option 1", "Option 2", "Option 3"],
        on_change={
            "Option 1": "alert('You selected Option 1!')",
            "Option 2": "alert('You selected Option 2!')",
            "Option 3": "console.log('Option 3 was selected')",
        },
        width="250px",
        background_color="#f9f9f9",
        padding="8px 10px",
    )

    return dropdown.render()

# FastHTML app example
app, rt = fast_app()

@rt("/")
async def index():
    dropdown_content = example_dropdown_menu()

    return Div(
        H1("DropdownMenu Example with Dynamic Events"),
        dropdown_content,
        cls="container",
    )

if __name__ == "__main__":
    serve()
