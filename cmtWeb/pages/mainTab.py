import reflex as rx


def tabSection() -> rx.Component:
    # button nav bar

    button = rx.button("About", bg="blue", border_radius="0.5em", width="15%")
    button1 = rx.button("About", bg="blue", border_radius="0.5em", width="15%")
    button2 = rx.button("About", bg="blue", border_radius="0.5em", width="15%")
    button3 = rx.button("About", bg="blue", border_radius="0.5em", width="15%")
    button4 = rx.button("About", bg="blue", border_radius="0.5em", width="15%")
    flex = rx.flex(rx.spacer(), button, button1, button2, button3, button4, rx.spacer())

    return flex
