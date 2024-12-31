import sys
import os

# Add the parent directory of 'components' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fasthtml.common import *
from components.button import CustomButton
from components.label import CustomLabel

class FlowPanel:
    def __init__(self, *args, **kwargs):
        """Initialize the FlowPanel with optional children and attributes."""
        self.children = list(args)  # Store initial children
        self.attrs = kwargs  # Store additional attributes

    def add(self, component):
        """Add a new component to the FlowPanel."""
        self.children.append(component)

    def render(self):
        """Render the FlowPanel as a Div containing its children."""
        return Div(*self.children, **self.attrs, cls="flow-panel")

    @staticmethod
    def css():
        """Return CSS styles for the FlowPanel."""
        return """
        <style>
            .flow-panel {
                display: flex;
                flex-wrap: wrap;
                border: 1px solid #000;
                padding: 10px;
            }
        </style>
        """

label1 = CustomLabel("Label 1")
label2 = CustomLabel("Label 2", margin="20px", background_color="#e0e0e0")
label3 = CustomLabel("Label 3", color="blue", font_size="50px")

def example_flow_panel():
    # Create a FlowPanel instance
    flow_panel = FlowPanel()

    # Create CustomLabel and CustomButton instances
    button1 = CustomButton("Button 1")
    button2 = CustomButton("Button 2", cls="custom-button")
    button3 = CustomButton("Button 3", cls="custom-button")

    # Add them to the FlowPanel
    flow_panel.add(label1.render())
    flow_panel.add(button1.render())
    flow_panel.add(label2.render())
    flow_panel.add(button2.render())
    flow_panel.add(label3.render())
    flow_panel.add(button3.render())

    # Render the FlowPanel
    return flow_panel


app, rt = fast_app()

@rt("/")
async def index():
    flow_panel = example_flow_panel()
    
    # Aggregate all CSS styles
    all_css = FlowPanel.css() + label1.css() + label2.css() + label3.css() + CustomButton("Button").css()
    
    return Div(
        H1("FlowPanel Example with Labels and Buttons"),
        flow_panel.render(),
        cls="container",
        style=all_css  # Include aggregated CSS styles
    )

if __name__ == "__main__":
    serve()
