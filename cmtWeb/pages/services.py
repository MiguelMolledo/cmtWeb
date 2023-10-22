import reflex as rx
from cmtWeb.styles import styles

cardStyle = {
    "bg": "linear-gradient(360deg, rgba(255,0,128,0.7203256302521008) 2%, rgba(27,26,33,0.4066001400560224) 5%, rgba(27,26,33,0.3841911764705882) 95%, rgba(255,0,128,0.7203256302521008) 100%)",
    "width": "200px",
}
highLightedText = {
    "bgClip": "text",
    "fontSize": ["2xl", "2xl", "2xl", "5xl", "5xl"],
    "fontWeight": "extrabold",
    "bgGradient": "linear(to-l, #7928CA, #FF0080)",
    "style": {"color": "transparent"},
}


def serviceCards() -> rx.Component:
    return rx.responsive_grid(
        rx.card(
            # rx.text("Bla bla bla development bla bla bla "),
            rx.image(src="PipeSoftwares.png", height="auto", width="100%"),
            header=rx.heading("3D Pipeline", size="lg"),
            footer=rx.text("Provide 3D/VFX/Tracking Tools"),
            # footer=rx.heading("", size="sm"),
            **cardStyle,
        ),
        rx.card(
            rx.card_body(rx.image(src="blockchain.png", height="auto", width="100%")),
            header=rx.heading("BlockChain", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            **cardStyle,
        ),
        rx.card(
            rx.card_body(rx.image(src="front-end.png", height="auto", width="100%")),
            header=rx.heading("Front-End", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            **cardStyle,
        ),
        rx.card(
            rx.card_body(rx.image(src="backend.png", height="auto", width="100%")),
            header=rx.heading("Back-End", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            **cardStyle,
        ),
        rx.card(
            rx.card_body(rx.image(src="consulting.png", height="auto", width="100%")),
            header=rx.heading("Consulting", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            **cardStyle,
        ),
        columns=[3],
        spacing="4",
        color="white",
    )


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
