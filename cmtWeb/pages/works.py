import reflex as rx


def createCard(header: str, description: str, footer: str):
    return rx.card(
        rx.text(description),
        header=rx.heading("Header", size="lg"),
        footer=rx.heading("Footer", size="sm"),
    )


def workGridItem() -> rx.Component:
    return rx.responsive_grid(
        rx.card(
            rx.text("Body of the Card Component"),
            header=rx.heading("Header", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            bg="lightgreen",
        ),
        rx.card(
            rx.text("Body of the Card Component"),
            header=rx.heading("Header", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            bg="lightblue",
        ),
        rx.card(
            rx.text("Body of the Card Component"),
            header=rx.heading("Header", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            bg="purple",
        ),
        rx.card(
            rx.text("Body of the Card Component"),
            header=rx.heading("Header", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            bg="tomato",
        ),
        rx.card(
            rx.text("Body of the Card Component"),
            header=rx.heading("Header", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            bg="orange",
        ),
        rx.card(
            rx.text("Body of the Card Component"),
            header=rx.heading("Header", size="lg"),
            footer=rx.heading("Footer", size="sm"),
            bg="white",
        ),
        columns=[3],
        spacing="4",
    )


def worksSection() -> rx.Component:
    return rx.flex(workGridItem())
