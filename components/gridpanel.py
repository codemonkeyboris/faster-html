from fasthtml.common import *
from button import CustomButton
from label import CustomLabel


class GridPanel:
    def __init__(self, *children, columns="repeat(3, 1fr)", gap="10px", **kwargs):
        """
        Initialize the GridPanel with optional children and customizable styles.

        :param children: Initial child components for the panel.
        :param columns: Grid column setup (default is 3 columns).
        :param gap: The space between grid items.
        :param kwargs: Additional attributes for the panel (e.g., custom styles).
        """
        self.children = list(children)
        self.attrs = kwargs  # Additional attributes
        self.styles = {
            "display": "grid",
            "grid-template-columns": columns,
            "gap": gap,
        }

    def add(self, component):
        """Add a new component to the GridPanel."""
        self.children.append(component)

    def render(self):
        """Render the GridPanel as a Div containing its children."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
        return Div(*self.children, **self.attrs, cls="grid-panel", style=style)


def example_grid_panels():
    """Create a GridPanel with multiple child elements."""
    # Adding labels and buttons to the grid
    label1 = CustomLabel("Label 1", background_color="#ffcccb")
    button1 = CustomButton("Button 1", on_click="alert('Button 1 clicked!')")

    label2 = CustomLabel("Label 2", background_color="#ffeb3b")
    button2 = CustomButton("Button 2", on_click="alert('Button 2 clicked!')")

    label3 = CustomLabel("Label 3", background_color="#8bc34a")
    button3 = CustomButton("Button 3", on_click="alert('Button 3 clicked!')")

    label4 = CustomLabel("Label 4", background_color="#009688")
    button4 = CustomButton("Button 4", on_click="alert('Button 4 clicked!')")

    label5 = CustomLabel("Label 5", background_color="#3f51b5")
    button5 = CustomButton("Button 5", on_click="alert('Button 5 clicked!')")

    label6 = CustomLabel("Label 6", background_color="#e91e63")
    button6 = CustomButton("Button 6", on_click="alert('Button 6 clicked!')")

    # Creating the grid panel with 3 columns and 10px gap
    grid_panel = GridPanel(columns="repeat(3, 1fr)", gap="20px")
    grid_panel.add(label1.render())
    grid_panel.add(button1.render())
    grid_panel.add(label2.render())
    grid_panel.add(button2.render())
    grid_panel.add(label3.render())
    grid_panel.add(button3.render())
    grid_panel.add(label4.render())
    grid_panel.add(button4.render())
    grid_panel.add(label5.render())
    grid_panel.add(button5.render())
    grid_panel.add(label6.render())
    grid_panel.add(button6.render())

    return grid_panel


app, rt = fast_app()


@rt("/")
async def index():
    grid_panel = example_grid_panels()

    return Div(
        H1("GridPanel Example with Multiple Items"),
        grid_panel.render(),
        cls="container",
    )


if __name__ == "__main__":
    serve()
