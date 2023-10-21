import reflex as rx
from cmtWeb.pages.ConfigText import DESCRIPTION_TEST
import copy

highLightedText = {
    "bgClip": "text",
    "fontSize": "5xl",
    "fontWeight": "extrabold",
    # bgGradient="linear(to-l, #ff5acd, #00e1f5)",
    "bgGradient": "linear(to-l, #7928CA, #FF0080)",
    "style": {"color": "transparent"},
}

highLightedTextMedium = copy.deepcopy(highLightedText)
highLightedTextMedium["fontSize"] = "3x1"


def customField(field: str, value: str) -> rx.Component:
    textStyle = copy.deepcopy(highLightedTextMedium)
    textStyle.pop("style")
    textStyle.pop("bgGradient")
    textStyle["color"] = "#FF0080"

    return rx.hstack(
        rx.text(f"{field}: ", **textStyle),
        rx.text(f"{value}", font_size="1em"),
        align="left",
        width="100%",
    )


def aboutSection() -> rx.Component:
    # button nav bar
    imageVsStack = rx.flex(
        rx.image(
            src="profile.jpg",
            size="md",
            width="100%",
            height="auto",
            max_height="1500x",
            max_width="1000px",
            min_height="600x",
            min_width="400px",
            # style={"filter": "blur(3px)"},
            # top="0px",
            style={
                "box-shadow": "60px -16px #FF0080",
                # "outline": "20px solid #FF0080",
                # "outline-offset": "15px",
            },
        ),
        rx.button(
            "Download Resume",
            color_scheme="pink",
            # bg="white",
            # color="white",
            # variant="solid",
            # style={"bg": ""},
            # border_radius="lg",
        ),
        rx.button("TEST"),
        rx.button("TEST"),
        rx.button("TEST"),
        direction="column",
        align="center",
    )

    aboutVsStack = rx.vstack(
        rx.text("ABOUT ME", **highLightedText),
        rx.text(DESCRIPTION_TEST, style={"font-size": "1em"}),
        customField("NAME", "Miguel Molledo"),
        customField("DATE OF BIRTH", "26 September 1993"),
        customField("NATIONALITY", "Spain"),
        customField("ADDRESS", "Madrid, Spain, 28016 Maestro lassalle 22"),
        customField("PHONE", "+34 606 11 76 80"),
        customField("E-MAIL", "info@miguelmolledo.com"),
    )

    return rx.flex(
        rx.flex(
            rx.spacer(),
            imageVsStack,
            aboutVsStack,
            rx.spacer(),
            # minHeight="100vh",
            # display="flex",
            # align_items="stretch",
            align="center",
            gap="120",
            direction="row",
            style={"align-items": "stretch"},
        ),
        rx.flex(),
        direction="column",
    )
