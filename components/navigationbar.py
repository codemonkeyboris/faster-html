from fasthtml.common import *

class NavigationBar:
    def __init__(self, logo, *menu_items, **kwargs):
        """
        Initialize the navigation bar with a logo and menu items.
        
        :param logo: The logo element.
        :param menu_items: Menu items, which are link buttons.
        :param kwargs: Additional attributes for the navigation bar.
        """
        self.logo = logo
        self.menu_items = menu_items
        self.attrs = kwargs

    def add(self, item):
        """Add a new menu item to the navigation bar."""
        self.menu_items.append(item)

    def render(self):
        """Render the navigation bar as a Div containing logo and menu items."""
        # Logo is placed at the left, menu items to the right
        navbar_style = "display: flex; justify-content: space-between; align-items: center; background-color: green; padding: 10px 20px;"
        return Div(
            self.logo,
            Div(*self.menu_items, style="display: flex; gap: 20px;"),
            **self.attrs,
            style=navbar_style,
            cls="navbar"
        )


def example_navbar():
    """Create a navigation bar with logo and link buttons."""
    # Create a logo (can be an image or text)
    logo = Span("MyLogo", style="color: white; font-size: 24px; font-weight: bold;")

    # Create link buttons using FastHTML's Button and style them as links
    home_button = A("Home", href="/", style="color: white; text-decoration: none;")
    about_button = A("About", href="/about", style="color: white; text-decoration: none;")
    contact_button = A("Contact", href="/contact", style="color: white; text-decoration: none;")

    # Create the navigation bar with the buttons
    navbar = NavigationBar(logo, home_button, about_button, contact_button)
    
    return navbar

app, rt = fast_app()

@rt("/")
async def index():
    navbar = example_navbar()

    return Div(
        navbar.render(),  # This renders the navigation bar
        Div(
            H1("Website with Navigation Bar"),
            style="margin-top: 60px;",  # Add margin to avoid overlap with navbar
        ),
        cls="container"
    )

if __name__ == "__main__":
    serve()
