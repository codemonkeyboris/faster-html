from fasthtml.common import *
from button import CustomButton
from label import CustomLabel


class FlowPanel:
    def __init__(self, *children, border="1px solid #000", padding="10px", **kwargs):
        """
        Initialize the FlowPanel with optional children and customizable styles.

        :param children: Initial child components for the panel.
        :param border: Border for the panel.
        :param padding: Padding for the panel.
        :param kwargs: Additional attributes for the panel (e.g., custom styles).
        """
        self.children = list(children)
        self.attrs = kwargs  # Additional attributes
        self.styles = {
            "display": "flex",
            "flex-wrap": "wrap",
            "border": border,
            "padding": padding,
        }

    def add(self, component):
        """Add a new component to the FlowPanel."""
        self.children.append(component)

    def render(self):
        """Render the FlowPanel as a Div containing its children."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
        return Div(*self.children, **self.attrs, cls="flow-panel", style=style)


def example_flow_panel():
    """Create an example FlowPanel instance with CustomLabels and CustomButtons."""
    # Create CustomLabel instances
    label1 = CustomLabel("Label 1")
    label2 = CustomLabel("Label 2", margin="20px", background_color="#e0e0e0")
    label3 = CustomLabel("Label 3", color="blue", font_size="50px")

    # Create CustomButton instances
    button1 = CustomButton("Button 1", on_click="alert('Button 1 clicked!')")
    button2 = CustomButton(
        "Button 2",
        background_color="#28a745",
        hover_background_color="#218838",
        on_click="alert('Button 2 clicked!')",
    )
    button3 = CustomButton(
        "Button 3",
        background_color="#ffc107",
        hover_background_color="#e0a800",
        on_click="console.log('Button 3 was clicked')",
    )

    # Create a FlowPanel and add components
    flow_panel = FlowPanel()
    flow_panel.add(label1.render())
    flow_panel.add(button1.render())
    flow_panel.add(label2.render())
    flow_panel.add(button2.render())
    flow_panel.add(label3.render())
    flow_panel.add(button3.render())

    return flow_panel


# Create a FastHTML application
app, rt = fast_app()


@rt("/")
async def index():
    flow_panel = example_flow_panel()

    return Div(
        H1("FlowPanel Example with Labels and Buttons"),
        flow_panel.render(),
        cls="container",
    )


if __name__ == "__main__":
    serve()
