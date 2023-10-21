"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from cmtWeb.styles import styles
from cmtWeb.pages.mainTab import tabSection
from cmtWeb.pages.about import aboutSection
from cmtWeb.pages.home import homeSection
from cmtWeb.pages.works import worksSection
from cmtWeb.pages.services import servicesSection
from cmtWeb.pages.contact import contactSection


def exampleBox(color: str, width: str) -> rx.Component:
    return rx.box("About", border_radius="0.5em", width=width, bg="white")


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            tabSection(),
            rx.spacer(
                minHeight="59px",
            ),
            homeSection(),
            aboutSection(),
            servicesSection(),
            worksSection(),
            contactSection(),
        ),
        minHeight="100vh",
    )


# Add state and page to the app.
app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)
app.compile()
