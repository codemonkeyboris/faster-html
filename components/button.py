from fasthtml.common import *

class CustomButton:
    def __init__(self, text, cls="button"):
        """Initialize a button with text and optional CSS class."""
        self.text = text
        self.cls = cls

    def render(self):
        """Render the button as a Button."""
        return Button(self.text, cls=self.cls)

    @staticmethod
    def css():
        """Return CSS styles for the Button."""
        return """
        <style>
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