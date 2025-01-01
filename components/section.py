from fasthtml.common import *

class CustomSection:
    def __init__(self, content, bg_color="white", extra_classes="", flex=True):
        """
        CustomSection for wrapping content with a predefined layout.

        :param content: The content to include in the section.
        :param bg_color: Background color in any valid CSS color format.
        :param extra_classes: Additional CSS classes to append.
        :param flex: Whether to include a flex layout.
        """
        self.content = content
        self.bg_color = bg_color
        self.extra_classes = extra_classes
        self.flex = flex

    def render(self):
        """
        Render the section with the specified styles.

        :return: A Section element with the desired layout and styling.
        """
        base_classes = (
            "section-base1 col" if self.flex else "section-base1"
        )
        classes = (
            f"{base_classes} -mt-8 lg:-mt-16 items-center "
            "rounded-t-3xl lg:rounded-t-[2.5rem] relative "
            f"{self.extra_classes}"
        )
        style = f"background-color: {self.bg_color};"
        return Section(self.content, cls=classes, style=style)

##################################################
# Example Usage

def example_sections():
    """
    Create two example sections with different content and background colors.
    """
    # First section content
    content1 = Div(
        H1("Welcome to the First Section!"),
        P("This section has a blue background and white text."),
        Button("Learn More", cls="btn-primary"),
        cls="content-wrapper"
    )
    section1 = CustomSection(
        content=content1,
        bg_color="#007bff",  # Background color as a hex code
        extra_classes="text-white",  # Additional styling
        flex=True,  # Enable flex layout
    )

    # Second section content
    content2 = Div(
        H1("Welcome to the Second Section!"),
        P("This section has a gray background and dark text."),
        Button("Get Started", cls="btn-secondary"),
        cls="content-wrapper"
    )
    section2 = CustomSection(
        content=content2,
        bg_color="#f8f9fa",  # Background color as a hex code
        extra_classes="text-gray-800",  # Additional styling
        flex=False,  # Disable flex layout
    )

    return Div(
        section1.render(),
        section2.render(),
        cls="sections-container",
    )

# FastHTML app example
app, rt = fast_app()

@rt("/")
async def index():
    sections = example_sections()

    return Div(
        H1("CustomSection Example with Two Sections"),
        sections,
        cls="container mx-auto",
    )

if __name__ == "__main__":
    serve()
