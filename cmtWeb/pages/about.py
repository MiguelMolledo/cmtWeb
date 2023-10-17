import reflex as rx


def aboutSection() -> rx.Component:
    # button nav bar

    return rx.box(
        "About",
        bg=color,
        border_radius="0.5em",
        width=percentage,
    )
