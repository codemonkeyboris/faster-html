from fasthtml.common import *
from label import CustomLabel
from button import CustomButton


class Card:
    def __init__(
        self,
        *args,
        cls="card",
        margin="10px",
        padding="20px",
        border="1px solid #ccc",
        background_color="#f9f9f9",
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
        width="300px",
        height=None,
        border_radius="8px",
        hover_box_shadow="0 6px 12px rgba(0, 0, 0, 0.2)",
        **kwargs,
    ):
        """
        Initialize a Card with optional children components and customizable styles.
        """
        self.children = list(args)  # Store initial children components
        self.attrs = kwargs  # Store additional attributes
        self.styles = {
            "margin": margin,
            "padding": padding,
            "border": border,
            "background-color": background_color,
            "box-shadow": box_shadow,
            "width": width,
            "height": height if height else "auto",
            "border-radius": border_radius,
        }
        # Hover effect style
        self.hover_box_shadow = hover_box_shadow
        self.cls = cls

    def add(self, component):
        """Add a new component to the Card."""
        self.children.append(component)

    def render(self):
        """Render the Card as a Div with inline styles, including hover effect."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
        hover_style = f"hover: {{ box-shadow: {self.hover_box_shadow}; }}"

        # Return a Div with inline styles and add hover effect as inline style
        return Div(
            *self.children,
            **self.attrs,
            cls=self.cls,
            style=style + f"; {hover_style}",  # Combine the hover effect and styles
        )


def example_card():
    """Create a Card with multiple components inside it."""

    label1 = CustomLabel("This is a Label inside the Card")
    label2 = CustomLabel(
        "Another Label inside", margin="10px", background_color="#f0f0f0"
    )
    button1 = CustomButton("Click Me")

    # Create a Card instance and add components
    card = Card(label1.render(), label2.render(), button1.render())

    return card.render()


# FastHTML app example
app, rt = fast_app()


@rt("/")
async def index():
    card_content = example_card()

    return Div(
        H1("Card Component Example"),
        card_content,
        cls="container",
    )


if __name__ == "__main__":
    serve()
