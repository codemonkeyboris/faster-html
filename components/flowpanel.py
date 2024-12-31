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



def example_flow_panels():
    """Create two FlowPanel instances: one horizontal and one vertical."""
    # Horizontal FlowPanel (as before)
    label1 = CustomLabel("Label 1")
    label2 = CustomLabel("Label 2", margin="20px", background_color="#e0e0e0")
    label3 = CustomLabel("Label 3", color="blue", font_size="50px")

    button1 = CustomButton("Button 1", on_click="alert('Button 1 clicked!')")
    button2 = CustomButton("Button 2", background_color="#28a745", hover_background_color="#218838",
                           on_click="alert('Button 2 clicked!')")
    button3 = CustomButton("Button 3", background_color="#ffc107", hover_background_color="#e0a800",
                           on_click="console.log('Button 3 was clicked')")

    horizontal_panel = FlowPanel()
    horizontal_panel.add(label1.render())
    horizontal_panel.add(button1.render())
    horizontal_panel.add(label2.render())
    horizontal_panel.add(button2.render())
    horizontal_panel.add(label3.render())
    horizontal_panel.add(button3.render())

    # Vertical FlowPanel with a different set of labels and buttons
    vertical_panel = FlowPanel(border="1px solid #333", padding="15px")
    vertical_panel.styles["flex-direction"] = "column"
    
    # Adding labels and buttons in vertical stack
    label4 = CustomLabel("Vertical Label 1", background_color="#ffcccc")
    button4 = CustomButton("Vertical Button 1", background_color="#0066cc",
                           on_click="alert('Vertical Button 1 clicked!')")
    label5 = CustomLabel("Vertical Label 2", background_color="#ccffcc")
    button5 = CustomButton("Vertical Button 2", background_color="#cc6600",
                           on_click="console.log('Vertical Button 2 was clicked')")
    label6 = CustomLabel("Vertical Label 3", background_color="#ffe6cc")
    button6 = CustomButton("Vertical Button 3", background_color="#e60000",
                           on_click="alert('Vertical Button 3 clicked!')")

    vertical_panel.add(label4.render())
    vertical_panel.add(button4.render())
    vertical_panel.add(label5.render())
    vertical_panel.add(button5.render())
    vertical_panel.add(label6.render())
    vertical_panel.add(button6.render())

    return horizontal_panel, vertical_panel


# Create a FastHTML application
app, rt = fast_app()


@rt("/")
async def index():
    horizontal_panel, vertical_panel = example_flow_panels()

    return Div(
        H1("FlowPanel Example with Horizontal and Vertical Groups"),
        Div(
            horizontal_panel.render(),
            vertical_panel.render(),
            style="display: flex; gap: 20px;",  # To separate the two panels
        ),
        cls="container"
    )


if __name__ == "__main__":
    serve()
