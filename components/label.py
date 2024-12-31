from fasthtml.common import *


class CustomLabel:
    def __init__(
        self,
        text,
        cls="label",
        margin="10px",
        padding="10px",
        border="1px solid #ccc",
        background_color="#f9f9f9",
        color=None,
        font_size=None,
    ):
        """
        Initialize a label with text, optional CSS class, and customizable styles.

        :param text: Text content of the label.
        :param cls: CSS class name.
        :param margin: Margin for the label.
        :param padding: Padding for the label.
        :param border: Border for the label.
        :param background_color: Background color for the label.
        :param color: Text color for the label (optional).
        :param font_size: Font size for the label (optional).
        """
        self.text = text
        self.cls = cls
        self.styles = {
            "margin": margin,
            "padding": padding,
            "border": border,
            "background-color": background_color,
        }

        # Optional styles are added only if provided
        if color:
            self.styles["color"] = color
        if font_size:
            self.styles["font-size"] = font_size

    def render(self):
        """Render the label as a Div with inline styles."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
        return Div(self.text, cls=self.cls, style=style)


##################################################
def test_labels():
    """Simple test application to display CustomLabel instances."""
    label1 = CustomLabel("Label 1")
    label2 = CustomLabel("Label 2", margin="20px", background_color="#e0e0e0")
    label3 = CustomLabel("Label 3", color="blue", font_size="50px")

    # Aggregate rendered labels
    return Div(
        label1.render(),
        label2.render(),
        label3.render(),
        cls="test-container",
    )


# Create a FastHTML application
app, rt = fast_app()


@rt("/")
async def index():
    label_content = test_labels()

    return Div(
        H1("Testing CustomLabel"),
        label_content,
        cls="container",
    )


if __name__ == "__main__":
    serve()
