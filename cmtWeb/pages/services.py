import reflex as rx
from cmtWeb.styles import styles


def servicesSection() -> rx.Component:
    return rx.flex(
        rx.responsive_grid(
            rx.card(
                # rx.text("Bla bla bla development bla bla bla "),
                rx.image(src="favicon.ico", height="auto", width="100%"),
                header=rx.heading("3D Pipeline", size="lg"),
                # footer=rx.heading("", size="sm"),
                bg="white",
                width="200px",
            ),
            rx.card(
                rx.text(""),
                header=rx.heading("BlockChain", size="lg"),
                footer=rx.heading("Footer", size="sm"),
                bg="lightblue",
                width="200px",
            ),
            rx.card(
                rx.text(""),
                header=rx.heading("Front-End", size="lg"),
                footer=rx.heading("Footer", size="sm"),
                bg="tomato",
                width="200px",
            ),
            rx.card(
                rx.text(""),
                header=rx.heading("Back-End", size="lg"),
                footer=rx.heading("Footer", size="sm"),
                bg="tomato",
                width="200px",
            ),
            rx.card(
                rx.text(""),
                header=rx.heading("Consulting", size="lg"),
                footer=rx.heading("Footer", size="sm"),
                bg="tomato",
                width="200px",
            ),
            columns=[3],
            spacing="4",
        ),
        bg="black",
        width="100%",
        paddingTop="100px",
        paddingBottom="100px",
        justify="center",
        align="center",
    )
