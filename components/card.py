from fasthtml.common import *
from label import CustomLabel
from button import CustomButton
from flowpanel import FlowPanel


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

        return Div(
            *self.children,
            **self.attrs,
            cls=self.cls,
            style=style + f"; {hover_style}",
        )


def example_flow_panel_with_cards():
    """Create a FlowPanel with 3 Cards in a row."""

    label1 = CustomLabel("Label inside Card 1")
    label2 = CustomLabel("Label inside Card 2")
    label3 = CustomLabel("Label inside Card 3")

    # Create Card instances
    card1 = Card(label1.render(), CustomButton("Button 1").render())
    card2 = Card(label2.render(), CustomButton("Button 2").render())
    card3 = Card(label3.render(), CustomButton("Button 3").render())

    # Create a FlowPanel and add the Cards
    flow_panel = FlowPanel(card1.render(), card2.render(), card3.render())

    return flow_panel.render()


app, rt = fast_app()


@rt("/")
async def index():
    flow_panel_content = example_flow_panel_with_cards()

    return Div(
        H1("FlowPanel with 3 Cards in a Row"),
        flow_panel_content,
        cls="container",
    )


if __name__ == "__main__":
    serve()
