## In this page we are going to have a home section

## Main Presentaation
## offer service button
## about us
## motivational image + text
## Select most impact clients
## FAQ
from cmtWeb.styles import styles
from cmtWeb.pages.mainTab import tabSection
from cmtWeb.mainState import State

import reflex as rx

titleStyle = {
    "fontWeight": "extrabold",
    "bgGradient": "linear-gradient(360deg, rgba(157,0,167,1) 0%, rgba(0,249,255,1) 100%)",
    "bgClip": "text",
}
highLightedText = {
    "bgClip": "text",
    "fontSize": ["2xl", "2xl", "2xl", "5xl", "5xl"],
    "fontWeight": "extrabold",
    "bgGradient": "linear(to-l, #7928CA, #FF0080)",
    "style": {"color": "transparent", "font_family": styles.SANS},
}

imageLinkDict = {
    "width": "auto",
    "max_height": ["32px", "32px", "32px", "64px", "64px"],
}


def presentationSection() -> rx.Component:
    return rx.flex(
        rx.flex(
            # rx.spacer(width="20%"),
            rx.text(
                "Hello!",
                fontSize="45px",
                stye={"font_family": styles.SANS},
            ),
            rx.heading(
                "I'm Miguel Molledo!",
                **highLightedText,
            ),
            rx.text(
                "3D Pipeline & Blockchain & Full Stack developer",
                stye={
                    "font_family": styles.SANS,
                },
            ),
            # rx.spacer(),
            direction="column",
        ),
        rx.spacer(),
        rx.flex(
            rx.flex(
                rx.spacer(min_height="100px"),
                rx.link(
                    rx.image(
                        src="github.png",
                        **imageLinkDict,
                    ),
                    href="https://github.com/MiguelMolledo",
                    is_external=True,
                ),
                rx.link(
                    rx.image(
                        src="twitter.png",
                        **imageLinkDict,
                    ),
                    href="https://twitter.com/MolledoMiguel",
                    is_external=True,
                ),
                rx.link(
                    rx.image(src="linkedin.png", **imageLinkDict),
                    href="https://www.linkedin.com/in/miguelmolledoalvarez",
                    is_external=True,
                ),
                direction="row",
                gap="10",
            ),
            rx.flex(
                rx.spacer(),
                rx.button("Hire me!", on_click=State.goToContact),
                rx.spacer(),
            ),
            direction="column",
        ),
        rx.spacer(),
        bg="rgb(255, 51, 255, 0.1)",
        padding="20px",
        # padding="20",
        gap="10px",
        direction=["column", "column", "column", "row", "row"],
        wdith="100%",
    )


def homeSection() -> rx.Component:
    return rx.flex(
        tabSection(),
        rx.spacer(),
        presentationSection(),
        rx.spacer(),
        width="100%",
        # maxHeight="0vh",
        minHeight=["40vh", "60vh", "80vh", "100vh", "100vh"],
        backgroundImage="home2Blur.png",
        backgroundRepeat="no-repeat",
        bgSize="cover",
        direction="column",
    )
