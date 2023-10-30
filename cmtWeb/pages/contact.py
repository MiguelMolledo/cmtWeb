import reflex as rx
from cmtWeb.pages.mainTab import tabSection
from cmtWeb.styles import styles

highLightedText = {
    "bgClip": "text",
    "fontSize": ["2xl", "2xl", "2xl", "5xl", "5xl"],
    "fontWeight": "extrabold",
    "bgGradient": "linear(to-l, #7928CA, #FF0080)",
    "style": {"color": "transparent", "font_family": styles.SANS},
}


def contactForm() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.spacer(border_color=styles.highLight),
                rx.text("Contact Info", **highLightedText),
                rx.spacer(border_color=styles.highLight),
                width="100%",
            ),
            rx.input(
                placeholder="First Name",
                id="first_name",
                border="2px solid white",
                borderRadius="5px",
                bg="rgb(27, 26, 33)",
            ),
            rx.input(
                placeholder="email",
                id="email",
                border="2px solid white",
                borderRadius="5px",
                bg="rgb(27, 26, 33)",
            ),
            rx.select(
                ["Web2", "Web3", "Pipeline", "Consultancy", "Other"],
                placeholder="Type of Service",
                id="type_of_service",
                border="2px solid white",
                borderRadius="5px",
                bg="rgb(27, 26, 33)",
                color="white",
            ),
            # rx.input(
            #     placeholder="Web2/Web3/Pipeline/Consultancy/Other",
            #     id="type_of_service",
            #     border="2px solid white",
            #     borderRadius="5px",
            #     bg="rgb(27, 26, 33)",
            # ),
            rx.editable(
                rx.editable_preview(),
                rx.editable_textarea(),
                placeholder="Describe your Needs here!",
                min_height="30vh",
                # on_submit=EditableState.set_example_textarea,
                width="100%",
                id="description_of_service",
                border="2px solid white",
                borderRadius="5px",
                color="white",
                bg="rgb(27, 26, 33)",
            ),
            width="40%",
        ),
        width="100%",
        align="center",
        justify="center",
    )


def contactSection() -> rx.Component:
    return rx.box(
        tabSection(),
        rx.spacer(min_height="200px"),
        contactForm(),
        direction="column",
        minHeight="100vh",
    )
