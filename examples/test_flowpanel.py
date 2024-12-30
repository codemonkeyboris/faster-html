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

# class CustomLabel:
#     def __init__(self, text, cls="label"):
#         """Initialize a label with text and optional CSS class."""
#         self.text = text
#         self.cls = cls

#     def render(self):
#         """Render the label as a Div."""
#         return Div(self.text, cls=self.cls)

#     @staticmethod
#     def css():
#         """Return CSS styles for the Label."""
#         return """
#         <style>
#             .label {
#                 margin: 10px;
#                 padding: 10px;
#                 border: 1px solid #ccc;
#                 background-color: #f9f9f9;
#             }
#         </style>
#         """

def example_flow_panel():
    # Create a FlowPanel instance
    flow_panel = FlowPanel()
    
    # Add labels and buttons as child components
    flow_panel.add(CustomLabel("Label 1").render())
    flow_panel.add(CustomButton("Button 1").render())
    flow_panel.add(CustomLabel("Label 2").render())
    flow_panel.add(CustomButton("Button 2").render())
    flow_panel.add(CustomLabel("Label 3").render())
    flow_panel.add(CustomButton("Button 3").render())

    # Render the FlowPanel
    return flow_panel.render()

# Create a FastHTML application
app, rt = fast_app()

@rt("/")
async def index():
    flow_panel_content = example_flow_panel()
    
    # Aggregate all CSS styles
    all_css = FlowPanel.css() + CustomLabel.css() + CustomButton.css()
    
    return Div(
        H1("FlowPanel Example with Labels and Buttons"),
        flow_panel_content,
        cls="container",
        style=all_css  # Include aggregated CSS styles
    )

if __name__ == "__main__":
    serve() 