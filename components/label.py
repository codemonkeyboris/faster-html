from fasthtml.common import *

class CustomLabel:
    def __init__(self, text, cls="label"):
        """Initialize a label with text and optional CSS class."""
        self.text = text
        self.cls = cls

    def render(self):
        """Render the label as a Div."""
        return Div(self.text, cls=self.cls)

    @staticmethod
    def css():
        """Return CSS styles for the Label."""
        return """
        <style>
            .label {
                margin: 10px;
                padding: 10px;
                border: 1px solid #ccc;
                background-color: #f9f9f9;
            }
        </style>
        """
