import reflex as rx


def contactSection() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text("Contact Us", fontSize="20px"),
            rx.input(
                placeholder="First Name",
                id="first_name",
                border="2px solid white",
                borderRadius="5px",
            ),
            rx.input(
                placeholder="email",
                id="email",
                border="2px solid white",
                borderRadius="5px",
            ),
            rx.input(
                placeholder="Web2/Web3/Pipeline/Consultancy/Other",
                id="type_of_service",
                border="2px solid white",
                borderRadius="5px",
            ),
            rx.editable(
                rx.editable_preview(),
                rx.editable_textarea(),
                placeholder="Describe your Needs here!",
                # on_submit=EditableState.set_example_textarea,
                width="100%",
                id="description_of_service",
                border="2px solid white",
                borderRadius="5px",
                color="white",
            ),
            width="40%",
        ),
        bg="rgb(27, 26, 33)",
        width="100%",
        align="center",
        justify="center",
    )
