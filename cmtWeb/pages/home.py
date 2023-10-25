## In this page we are going to have a home section

## Main Presentaation
## offer service button
## about us
## motivational image + text
## Select most impact clients
## FAQ
from cmtWeb.styles import styles
from cmtWeb.pages.mainTab import tabSection

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


def homeSection() -> rx.Component:
    return rx.flex(
        tabSection(),
        rx.spacer(),
        rx.flex(
            rx.flex(
                rx.spacer(width="20%"),
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
                    "3D Pipeline & Blockchain & Web Developer",
                    stye={
                        "font_family": styles.SANS,
                    },
                ),
                rx.spacer(),
                direction="column",
            ),
            bg="rgb(255, 51, 255, 0.1)",
            padding="20",
        ),
        rx.spacer(),
        width="100%",
        maxHeight="0vh",
        minHeight="100vh",
        backgroundImage="home2Blur.png",
        backgroundRepeat="no-repeat",
        bgSize="cover",
        direction="column",
        style={
            # "backdrop-filter": "blur(5px)",
            # "-webkit-backdrop-filter": "blur(5px)",
            # "filter": "blur(8px)",
            # "-webkit-filter": "blur(8px)",
        }
        # style={"filter": "blur(3px)"}
        # bg="linear-gradient(90deg, rgba(27,26,33,1) 31%, rgba(51,11,75,1) 68%)",
        # background-image: url("./images/forest.jpg") !important;
    )


# def navbar() -> rx.Component:
#     return rx.box(
#         rx.hstack(
#             rx.image(src="favicon.ico"),
#             rx.heading("My App"),
#         ),
#         rx.spacer(),
#         rx.text("DO you want to work with the best developer in the world?"),
#         width="40%",
#         z_index="5",
#         bg="linear-gradient(11deg, rgba(27,26,33,0.3) 0%, rgba(143,59,118,0.5) 95%);",
#     )
