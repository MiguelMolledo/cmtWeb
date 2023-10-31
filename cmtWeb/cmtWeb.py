"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from cmtWeb.styles import styles
from cmtWeb.pages.mainTab import tabSection
from cmtWeb.pages.about import section as aboutSection
from cmtWeb.pages.home import homeSection
from cmtWeb.pages.works import worksSection
from cmtWeb.pages.services import servicesSection
from cmtWeb.pages.contact import contactSection
from cmtWeb.mainState import State


def exampleBox(color: str, width: str) -> rx.Component:
    return rx.box("About", border_radius="0.5em", width=width, bg="white")


def index() -> rx.Component:
    # return rx.box()
    # return contactSection()
    return rx.box(
        rx.vstack(
            # tabSection(),
            homeSection(),
            aboutSection(),
            servicesSection(),
            worksSection(),
        ),
        minHeight="100vh",
    )


# Add state and page to the app.
app = rx.App(style=styles.BASE_STYLE, state=State)
# app = rx.App()


app.add_page(index)
# app.add_page(contactSection)
app.compile()
