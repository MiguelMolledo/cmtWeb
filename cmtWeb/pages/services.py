import reflex as rx
from cmtWeb.styles import styles
from cmtWeb.mainState import State

cardStyle = {
    "bg": "linear-gradient(360deg, rgba(255,0,128,0.7203256302521008) 2%, rgba(27,26,33,0.4066001400560224) 5%, rgba(27,26,33,0.3841911764705882) 95%, rgba(255,0,128,0.7203256302521008) 100%)",
    "min_width": ["100px", "150px", "200px", "200px", "250px"],
    "color": "white",
}
highLightedText = {
    "bgClip": "text",
    "fontSize": ["2xl", "2xl", "2xl", "5xl", "5xl"],
    "fontWeight": "extrabold",
    "bgGradient": "linear(to-l, #7928CA, #FF0080)",
    "style": {"color": "transparent"},
}


def createServiceCards() -> rx.Component:
    return rx.responsive_grid(
        rx.foreach(
            State.serviceInfo,
            lambda item: createCardButton(
                item["header"], item["footer"], item["image"]
            ),
        ),
        columns=[[2], [2], [3], [3], [3]],
        spacing="10",
        color="white",
    )


def createCardButton(header: str, footer: str, image: str):
    return rx.button(
        rx.card(
            rx.image(
                src=image,
                height="100%",
                # min_weight=["100px", "150px", "200px", "200px", "250px"],
            ),
            header=rx.heading(header, size="auto"),
            footer=rx.text(footer, fontSize=["8px", "xs", "sm", "md", "md"]),
            **cardStyle,
        ),
        height="auto",
        bg="transparent",
        style={
            "background-color": "transparent",
            ":hover": {
                "background-color": "transparent",
                "box-shadow": "0px 20px 40px #black",
                "transform": "scale(1.10)",
            },
        },
    )


def serviceCards() -> rx.Component:
    return rx.flex(createServiceCards(), width="80%")


def servicesSection() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.spacer(border_color=styles.highLight),
            rx.heading("SERVICES", **highLightedText),
            rx.spacer(border_color=styles.highLight),
        ),
        serviceCards(),
        # bg="black",
        width="100%",
        paddingTop="100px",
        paddingBottom="100px",
        justify="center",
        align="center",
        bg="#1a1340",
        minHeight="60vh",
        direction="column",
        gap="50px",
    )
