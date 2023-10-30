import reflex as rx
from ..styles import styles
from cmtWeb.pages.about import activitiesSection
from cmtWeb.mainState import State

highLightedText = {
    "bgClip": "text",
    "fontSize": ["2xl", "2xl", "2xl", "5xl", "5xl"],
    "fontWeight": "extrabold",
    "bgGradient": "linear(to-l, #7928CA, #FF0080)",
    "style": {"color": "transparent"},
}
cardStyle = {
    "bg": "linear-gradient(360deg, rgba(255,0,128,0.7203256302521008) 2%, rgba(27,26,33,0.4066001400560224) 5%, rgba(27,26,33,0.3841911764705882) 95%, rgba(255,0,128,0.7203256302521008) 100%)",
    "max_width": ["100px", "150px", "200px", "250px", "250px"],
    # "height": ["100px", "150px", "200px", "250px", "250px"],
    "color": "white",
}


# dataTest = list[
#     (
#         "Header1",
#         "footer1",
#         "music.png",
#         "Body body body body ",
#     )
# ]

rx.stat_arrow
#  img {
#   -webkit-mask-image:-webkit-gradient(linear, left top, left bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)));
#   mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));


def createCardsByDict() -> rx.Component:
    return rx.flex(
        rx.responsive_grid(
            rx.foreach(
                State.filteredWorkData,
                # lambda item: rx.text(item["header"]),
                lambda item: createCard(
                    item["header"], item["description"], item["footer"]
                ),
            ),
            columns=[[2], [2], [3], [3], [3]],
            spacing="4",
            color="white",
        ),
        style={
            "overflow": "auto",
            "::-webkit-scrollbar": {"display": "none"},
            "::-webkit-scrollbar": {"width": "10px"},
            "::-webkit-scrollbar-track": {
                "box-shadow": "inset 0 0 5px grey",
                "border-radius": "5px",
            },
            "::-webkit-scrollbar-thumb": {
                "background": styles.highLight,
                "border-radius": "5px",
            },
            " ::-webkit-scrollbar-thumb:hover": {
                "background": styles.medium,
            },
        },
        id="test1",
    )


def createCard(header: str, description: str, footer: str):
    body = rx.cond(
        description.contains(".png"),
        rx.image(
            src=description,
            width="100%",
            style={
                # "::-webkit-mask-image": "-webkit-gradient(linear, left top, left bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)))",
                # "::mask-image": "linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0))"
                "color": "transparent"
            },
        ),
        rx.text(description),
    )

    return rx.card(
        body,
        header=rx.heading(header, size="lg"),
        footer=rx.heading(footer, size="sm"),
        opacity="0.9",
        **cardStyle,
    )


def workGridItem() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.icon(
                tag="search",
                color="white",
                height="auto",
                width=["16px", "32px", "32px", "32px", "32px"],
            ),
            rx.input(
                value=State.filterWorksExpression,
                border_color=styles.highLight,
                on_change=State.inputWorkFilter,
            ),
            gap="2",
            justify="center",
        ),
        createCardsByDict(),
        direction="column",
        gap="10",
        width="100%",
        max_height=["500px", "500px", "650px", "850px", "1000px"],
    )


def titleSection() -> rx.Component:
    return rx.flex(
        rx.divider(border_color=styles.highLight),
        rx.spacer(rx.divider(border_color=styles.highLight)),
        rx.heading("WORKS", **highLightedText),
        rx.spacer(rx.divider(border_color=styles.highLight)),
        # rx.spacer(min_height="32px"),
        alignItems="center",
        direction="row",
        gap="4",
    )


def worksSection() -> rx.Component:
    return rx.flex(
        # activitiesSection(),
        titleSection(),
        workGridItem(),
        direction="column",
        gap="40",
        min_height=["40vh", "40vh", "60vh", "80vh", "100vh"],
        wdith="100%",
    )
