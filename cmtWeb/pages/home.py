## In this page we are going to have a home section

## Main Presentaation
## offer service button
## about us
## motivational image + text
## Select most impact clients
## FAQ
from cmtWeb.styles import styles

import reflex as rx


def homeSection() -> rx.Component:
    return rx.flex(
        rx.image(
            src="home2.jpg",
            size="md",
            width="100%",
            height="auto",
            style={"filter": "blur(3px)"},
            top="0px",
        ),
        width="100%",
        maxHeight="0vh",
        minHeight="100vh",
        bg="linear-gradient(90deg, rgba(27,26,33,1) 31%, rgba(51,11,75,1) 68%)",
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src="favicon.ico"),
            rx.heading("My App"),
        ),
        rx.spacer(),
        rx.text("DO you want to work with the best developer in the world?"),
        width="40%",
        z_index="5",
        bg="linear-gradient(11deg, rgba(27,26,33,0.3) 0%, rgba(143,59,118,0.5) 95%);",
    )
