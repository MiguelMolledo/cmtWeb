import reflex as rx
from cmtWeb.pages.ConfigText import DESCRIPTION_TEST
from ..styles import styles
import copy


highLightedText = {
    "bgClip": "text",
    "fontSize": ["2xl", "2xl", "2xl", "5xl", "5xl"],
    "fontWeight": "extrabold",
    "bgGradient": "linear(to-l, #7928CA, #FF0080)",
    "style": {"color": "transparent"},
}

highLightedTextMedium = copy.deepcopy(highLightedText)
highLightedTextMedium["fontSize"] = ["1x1", "1x1", "1xl.5", "1xl.5", "2xl"]


def customField(field: str, value: str) -> rx.Component:
    textStyle = copy.deepcopy(highLightedTextMedium)
    textStyle.pop("style")
    textStyle.pop("bgGradient")
    textStyle["color"] = "#FF0080"

    return rx.flex(
        rx.text(f"{field}: ", **textStyle),
        rx.text(f"{value}", font_size=["1em", "1em", "1em", "1em", "1em"]),
        rx.spacer(),
        # align="center",
        width=["100%", "100%", "100%", "100%", "100%"],
        align="stretch",
        gap="2",
    )


def buttonIcon(icon: str) -> rx.Component:
    return rx.button(
        rx.image(src=icon, height="auto", maxWidth="auto"),
        style={"border-radius": "30%"},
        variant="solid",
        width=["32px", "32px", "64px", "64px", "124px"],
        height=["32px", "32px", "64px", "64px", "124px"],
    )


def activitiesSection() -> rx.Component:
    return rx.flex(
        # rx.spacer(min_height="32px"),
        # rx.divider(),
        rx.spacer(rx.divider(border_color=styles.highLight)),
        rx.tooltip(buttonIcon("3d.png"), label="3D Animation!"),
        rx.tooltip(buttonIcon("btc.png"), label="BlockChain!"),
        rx.tooltip(buttonIcon("dog.png"), label="Animals!"),
        rx.tooltip(buttonIcon("music.png"), label="Play Guitar!"),
        rx.tooltip(buttonIcon("paint.png"), label="Paint Miniatures!"),
        rx.tooltip(buttonIcon("plane.png"), label="Travel along the world!"),
        rx.spacer(rx.divider(border_color=styles.highLight)),
        # rx.divider(),
        # rx.spacer(min_height="32px"),
        alignItems="center",
        direction="row",
        gap="4",
    )


def imageSection() -> rx.Component:
    return rx.flex(
        rx.image(
            src="profile.jpg",
            size="md",
            height="auto",
            max_width=["250px", "250px", "400px", "400px", "450px"],
            # max_width="450px",
            style={
                "box-shadow": "60px -16px #FF0080",
            },
        ),
        rx.spacer(min_height="16px"),
        rx.button(
            rx.icon(tag="download"),
            "Download Resume",
            min_width=["100px", "150px", "250px", "350px", "450px"],
            on_click=rx.download(
                url="/Cv.png",
                filename="CvMiguelMolledo.png",
            ),
        ),
        rx.spacer(min_height="16px"),
        direction="column",
        align="center",
    )


def aboutDescriptionSection() -> rx.Component:
    return rx.flex(
        rx.text("ABOUT ME", **highLightedText),
        rx.flex(
            rx.spacer(),
            rx.text(
                DESCRIPTION_TEST,
                font_size=["1em", "1em", "1em", "1em", "1.5em"],
                max_width="500px",
                width="100%",
            ),
            rx.spacer(),
            width="100%",
        ),
        rx.flex(
            rx.spacer(max_width=["0px", "0px", "0px", "0px", "0px"]),
            rx.vstack(
                customField("NAME", "Miguel Molledo"),
                customField("DATE OF BIRTH", "26 September 1993"),
                customField("NATIONALITY", "Spain"),
                customField("ADDRESS", "Madrid, Spain, 28016 Maestro lassalle 22"),
                customField("PHONE", "+34 606 11 76 80"),
                customField("E-MAIL", "info@miguelmolledo.com"),
                width="100%",
            ),
            rx.spacer(max_width=["0px", "0px", "0px", "0px", "0px"]),
        ),
        direction="column",
        align="center",
        gap=["2", "2", "2", "8", "8"],
    )


def aboutSection() -> rx.Component:
    return rx.flex(
        # rx.spacer(min_height="100px"),
        rx.flex(
            rx.spacer(
                max_width=["0", "0", "0", "10%", "10%"],
                max_height=["0", "0", "0", "10%", "10%"],
            ),
            imageSection(),
            aboutDescriptionSection(),
            rx.spacer(
                max_width=["0", "0", "0", "10%", "10%"],
                max_height=["0", "0", "0", "10%", "10%"],
            ),
            align="center",
            gap="20",
            direction=["column", "column", "row", "row", "row"],
            style={"align-items": "stretch"},
            min_width=["1%", "1%", "5%", "10%", "10%"],
        ),
        # rx.spacer(
        #     min_height="100px",
        #     min_width=["1%", "1%", "5%", "10%", "10%"],
        # ),
        direction="column",
    )


def section() -> rx.Component:
    # button nav bar

    return rx.flex(
        # rx.spacer(
        #     min_height=["20px", "20px", "20px", "50px", "100px"],
        #     min_width=["1%", "1%", "5%", "10%", "10%"],
        # ),
        rx.spacer(min_height=["20px", "20px", "20px", "20px", "20px"]),
        aboutSection(),
        # rx.spacer(min_height=["20px", "20px", "20px", "50px", "100px"]),
        rx.flex(
            rx.spacer(max_width="10%"), rx.heading("MY INTERESTS", **highLightedText)
        ),
        activitiesSection(),
        # rx.spacer(min_height=["20px", "20px", "20px", "50px", "100px"]),
        min_width=["1%", "1%", "5%", "10%" "10%"],
        direction="column",
        width="100%",
        gap=["20px", "20px", "20px", "50px", "100px"],
        minHeight=["40vh", "60vh", "80vh", "100vh", "100vh"],
        bg="#1b1a21",
    )
