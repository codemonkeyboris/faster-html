from fasthtml.common import *


class CustomSection:
    def __init__(self, bg_color="white", extra_classes="", flex=True):
        """
        CustomSection for wrapping content with a predefined layout.

        :param bg_color: Background color in any valid CSS color format.
        :param extra_classes: Additional CSS classes to append.
        :param flex: Whether to include a flex layout.
        """
        self.children = []  # Initialize an empty list to hold child elements
        self.bg_color = bg_color
        self.extra_classes = extra_classes
        self.flex = flex

    def add(self, component):
        """Add a new component to the CustomSection."""
        self.children.append(component)

    def render(self):
        """
        Render the section with the specified styles.

        :return: A Section element with the desired layout and styling.
        """
        base_classes = "section-base1 col" if self.flex else "section-base1"
        classes = (
            f"{base_classes} -mt-8 lg:-mt-16 items-center "
            "rounded-t-3xl lg:rounded-t-[2.5rem] relative "
            f"{self.extra_classes}"
        )
        style = f"background-color: {self.bg_color};"
        return Section(*self.children, cls=classes, style=style)


def example_sections():
    """
    Create two example sections with different content and background colors.
    """
    # First section
    section1 = CustomSection(bg_color="#007bff", extra_classes="text-white", flex=True)
    section1.add(H1("Welcome to the First Section!"))
    section1.add(P("This section has a blue background and white text."))
    section1.add(Button("Learn More", cls="btn-primary"))

    # Second section
    section2 = CustomSection(
        bg_color="#f8f9fa", extra_classes="text-gray-800", flex=False
    )
    section2.add(H1("Welcome to the Second Section!", style="color: #e63946;"))
    section2.add(
        P(
            "This section has a gray background and vibrant text.",
            style="color: #457b9d;",
        )
    )
    section2.add(Button("Get Started", cls="btn-secondary", style="color: #2a9d8f;"))

    return section1, section2


# FastHTML app example
app, rt = fast_app()


@rt("/")
async def index():
    section1, section2 = example_sections()

    return Div(
        H1("CustomSection Example with Added Items"),
        Div(
            section1.render(),
            section2.render(),
            style="display: flex; gap: 20px;",  # To separate the two sections
        ),
        cls="container mx-auto",
    )


if __name__ == "__main__":
    serve()
