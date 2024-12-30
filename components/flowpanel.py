from fasthtml.common import *

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
        return Div(*self.children, **self.attrs)

def example_flow_panel():
    # Create a FlowPanel instance
    flow_panel = FlowPanel(cls="flow-panel")
    
    # Add labels and buttons as child components
    flow_panel.add(Div("Label 1", cls="label"))
    flow_panel.add(Button("Button 1", cls="button"))
    flow_panel.add(Div("Label 2", cls="label"))
    flow_panel.add(Button("Button 2", cls="button"))
    flow_panel.add(Div("Label 3", cls="label"))
    flow_panel.add(Button("Button 3", cls="button"))

    # Render the FlowPanel
    return flow_panel.render()

# Create a FastHTML application
app, rt = fast_app()

@rt("/")
async def index():
    flow_panel_content = example_flow_panel()
    
    # Include CSS directly in the HTML response
    return Div(
        H1("FlowPanel Example with Labels and Buttons"),
        flow_panel_content,
        cls="container",
        style="""
            <style>
                .flow-panel {
                    display: flex;
                    flex-wrap: wrap;
                    border: 1px solid #000;
                    padding: 10px;
                }
                .label {
                    margin: 10px;
                    padding: 10px;
                    border: 1px solid #ccc;
                    background-color: #f9f9f9;
                }
                .button {
                    margin: 10px;
                    padding: 10px 20px;
                    border: none;
                    background-color: #007bff;
                    color: white;
                    cursor: pointer;
                    border-radius: 5px;
                }
                .button:hover {
                    background-color: #0056b3;
                }
            </style>
        """
    )

if __name__ == "__main__":
    serve() 