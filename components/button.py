from fasthtml.common import *


class CustomButton:
    def __init__(
        self,
        text,
        cls="button",
        margin="10px",
        padding="10px 20px",
        border="none",
        background_color="#007bff",
        color="white",
        cursor="pointer",
        border_radius="5px",
        hover_background_color="#0056b3",
    ):
        """
        Initialize a button with text, optional CSS class, and customizable styles.

        :param text: Text content of the button.
        :param cls: CSS class name.
        :param margin: Margin for the button.
        :param padding: Padding for the button.
        :param border: Border for the button.
        :param background_color: Background color for the button.
        :param color: Text color for the button.
        :param cursor: Cursor style when hovering over the button.
        :param border_radius: Border radius for rounded corners.
        :param hover_background_color: Background color on hover (not applied inline).
        """
        self.text = text
        self.cls = cls
        self.styles = {
            "margin": margin,
            "padding": padding,
            "border": border,
            "background-color": background_color,
            "color": color,
            "cursor": cursor,
            "border-radius": border_radius,
        }

    def render(self):
        """Render the button as a Button with inline styles."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
        return Button(self.text, cls=self.cls, style=style)


def test_buttons():
    """Simple test application to display CustomButton instances."""
    button1 = CustomButton("Button 1")
    button2 = CustomButton(
        "Button 2", margin="20px", background_color="#28a745", color="white"
    )
    button3 = CustomButton(
        "Button 3", padding="15px 30px", background_color="#ffc107", color="black"
    )

    # Aggregate rendered buttons
    return Div(
        button1.render(),
        button2.render(),
        button3.render(),
        cls="test-container",
    )


# Create a FastHTML application
app, rt = fast_app()


@rt("/")
async def index():
    button_content = test_buttons()

    return Div(
        H1("Testing CustomButton"),
        button_content,
        cls="container",
    )


if __name__ == "__main__":
    serve()
