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
highLightedTextMedium["fontSize"] = ["0.5em", "0.5em", "0.5em", "2xl", "2xl"]


def customField(field: str, value: str) -> rx.Component:
    textStyle = copy.deepcopy(highLightedTextMedium)
    textStyle.pop("style")
    textStyle.pop("bgGradient")
    textStyle["color"] = "#FF0080"

    return rx.hstack(
        rx.text(f"{field}: ", **textStyle),
        rx.text(f"{value}", font_size=["0.5em", "0.5em", "0.5em", "1em", "1em"]),
        align="left",
        width="100%",
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
        buttonIcon("3d.png"),
        buttonIcon("btc.png"),
        buttonIcon("dog.png"),
        buttonIcon("music.png"),
        buttonIcon("paint.png"),
        buttonIcon("plane.png"),
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
            # width="100%",
            # height="auto",
            # height=["450px", "750px", "1125px", "1125px", "1125px"],
            height="auto",
            max_width=["100px", "250px", "400px", "400px", "450px"],
            # max_width="450px",
            style={
                "box-shadow": "60px -16px #FF0080",
            },
        ),
        rx.spacer(min_height="16px"),
        rx.button(
            "Download Resume", min_width=["100px", "150px", "250px", "350px", "450px"]
        ),
        direction="column",
        align="center",
    )


def aboutDescriptionSection() -> rx.Component:
    return rx.flex(
        rx.text("ABOUT ME", **highLightedText),
        rx.text(DESCRIPTION_TEST, font_size=["8px", "8px", "8px", "1em", "1.5em"]),
        customField("NAME", "Miguel Molledo"),
        customField("DATE OF BIRTH", "26 September 1993"),
        customField("NATIONALITY", "Spain"),
        customField("ADDRESS", "Madrid, Spain, 28016 Maestro lassalle 22"),
        customField("PHONE", "+34 606 11 76 80"),
        customField("E-MAIL", "info@miguelmolledo.com"),
        direction="column",
        align="left",
        gap=["2", "2", "2", "8", "8"],
    )


def aboutSection() -> rx.Component:
    return rx.flex(
        rx.spacer(min_height="100px"),
        rx.flex(
            rx.spacer(),
            imageSection(),
            aboutDescriptionSection(),
            rx.spacer(),
            align="center",
            gap="120",
            direction="row",
            style={"align-items": "stretch"},
        ),
        rx.spacer(min_height="100px"),
        direction="column",
    )


def section() -> rx.Component:
    # button nav bar

    return rx.flex(
        rx.spacer(min_height=["20px", "20px", "20px", "50px", "100px"]),
        aboutSection(),
        rx.spacer(min_height=["20px", "20px", "20px", "50px", "100px"]),
        rx.flex(
            rx.spacer(max_width="10%"), rx.heading("MY INTERESTS", **highLightedText)
        ),
        activitiesSection(),
        rx.spacer(min_height=["20px", "20px", "20px", "50px", "100px"]),
        direction="column",
        gap="4",
        min_height=["40vh", "40vh", "60vh", "80vh", "100vh"],
    )
