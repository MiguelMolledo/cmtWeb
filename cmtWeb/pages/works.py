import reflex as rx


def worksSection() -> rx.Component:
    # gridItems = []
    # for x in range(0, 8):
    #     gridItems.append(
    #         rx.grid_item(
    #             createCard("Header", "Description", "Footer"),
    #             row_span=1,
    #             col_span=1,
    #             bg="lightgreen",
    #         )
    #     )

    return rx.flex(
        rx.container(
            rx.responsive_grid(
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
            ),
        ),
        width="100%",
    )


def createCard(header: str, description: str, footer: str):
    return rx.card(
        rx.text(description),
        header=rx.heading("Header", size="lg"),
        footer=rx.heading("Footer", size="sm"),
    )
