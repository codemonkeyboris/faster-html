from fasthtml.common import *

class CustomButton:
    def __init__(self, text, cls="button", 
                 margin="10px", padding="10px 20px", 
                 border="none", 
                 background_color="#007bff", 
                 color="white", 
                 cursor="pointer", 
                 border_radius="5px", 
                 hover_background_color="#0056b3", 
                 on_click=None):
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
        :param hover_background_color: Background color on hover.
        :param on_click: JavaScript function for the click event (optional).
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
        self.hover_background_color = hover_background_color
        self.on_click = on_click

    def render(self):
        """Render the button as a Button with inline styles and event handlers."""
        style = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
        hover_js = f"""
        this.style.backgroundColor = '{self.hover_background_color}';
        """
        reset_hover_js = f"""
        this.style.backgroundColor = '{self.styles["background-color"]}';
        """
        click_js = self.on_click if self.on_click else ""

        return Button(
            self.text,
            cls=self.cls,
            style=style,
            onmouseover=hover_js,
            onmouseout=reset_hover_js,
            onclick=click_js
        )

def test_buttons():
    """Simple test application to display CustomButton instances with events."""
    button1 = CustomButton(
        "Hover Me",
        hover_background_color="#0056b3",
        on_click="alert('Button 1 clicked!')"
    )
    button2 = CustomButton(
        "Click Me",
        margin="20px",
        background_color="#28a745",
        hover_background_color="#218838",
        on_click="alert('Button 2 clicked!')"
    )
    button3 = CustomButton(
        "Event Test",
        padding="15px 30px",
        background_color="#ffc107",
        hover_background_color="#e0a800",
        on_click="console.log('Button 3 was clicked')"
    )

    # Aggregate rendered buttons
    return Div(
        button1.render(),
        button2.render(),
        button3.render(),
        cls="test-container",
    )


app, rt = fast_app()

@rt("/")
async def index():
    button_content = test_buttons()

    return Div(
        H1("Testing CustomButton with Events"),
        button_content,
        cls="container",
    )

if __name__ == "__main__":
    serve()
