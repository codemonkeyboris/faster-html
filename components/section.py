from fasthtml.common import *

class CustomSection:
    def __init__(self, content, bg_color="white", extra_classes="", flex=True):
        """
        CustomSection for wrapping content with a predefined layout.

        :param content: The content to include in the section.
        :param bg_color: Background color class (e.g., "white", "gray-100").
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
            f"bg-{self.bg_color} {base_classes} "
            "-mt-8 lg:-mt-16 items-center "
            "rounded-t-3xl lg:rounded-t-[2.5rem] relative "
            f"{self.extra_classes}"
        )
        return Section(self.content, cls=classes)

##################################################
# Example Usage

def example_section():
    """
    Create an example section with custom content and styles.
    """
    content = Div(
        H1("Welcome to the Custom Section!"),
        P("This is an example of a reusable section wrapper."),
        Button("Click Me!", cls="btn-primary"),
        cls="content-wrapper"
    )
    custom_section = CustomSection(
        content=content,
        bg_color="blue-500",  # Background color
        extra_classes="text-white",  # Additional styling
        flex=True,  # Enable flex layout
    )
    return custom_section.render()

# FastHTML app example
app, rt = fast_app()

@rt("/")
async def index():
    section = example_section()

    return Div(
        H1("CustomSection Example"),
        section,
        cls="container mx-auto",
    )

if __name__ == "__main__":
    serve()
