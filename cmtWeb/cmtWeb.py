"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from cmtWeb.pages.about import aboutSection
from cmtWeb.pages.mainTab import tabSection

# def link_button():
#     return rx.link(
#         rx.button("Portfolio"),
#         href="https://miguelmolledoalvar.wixsite.com/portfoliomiguelma/3d",
#         is_external=True,
#         button=True,
#     )


class State(rx.State):
    """The app state."""

    pass


# def navbar() -> rx.Component:
#     return rx.box(
#         rx.hstack(
#             rx.image(src="favicon.ico"),
#             rx.heading("My App"),
#         ),
#         rx.spacer(),
#         rx.menu(
#             # rx.menu_button("Home"),
#             rx.menu_button("Home"),
#             rx.menu_button("About"),
#             rx.menu_button("About"),
#             link_button(),
#         ),
#         position="fixed",
#         width="100%",
#         top="0px",
#         z_index="5",
#     )


# def home() -> rx.Component:
#     return rx.fragment(
#         rx.color_mode_button(rx.color_mode_icon(), float="right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", font_size="2em"),
#             rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
#             rx.link(
#                 "Check out our docs!",
#                 href=docs_url,
#                 border="0.1em solid",
#                 padding="0.5em",
#                 border_radius="0.5em",
#                 _hover={
#                     "color": rx.color_mode_cond(
#                         light="rgb(107,99,246)",
#                         dark="rgb(179, 175, 255)",
#                     )
#                 },
#             ),
#             spacing="1.5em",
#             font_size="2em",
#             padding_top="10%",
#         ),
#     )


def exampleBox(color: str, percentage: str) -> rx.Component:
    return rx.box(
        "About",
        bg=color,
        border_radius="0.5em",
        width=percentage,
    )


def index() -> rx.Component:
    return rx.vstack(
        tabSection(),
        exampleBox("red", "100%"),
        exampleBox("blue", "100%"),
        exampleBox("green", "100%"),
        exampleBox("yellow", "100%"),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()


# https://fla.my/
