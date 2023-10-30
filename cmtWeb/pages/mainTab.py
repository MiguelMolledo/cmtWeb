import reflex as rx
from cmtWeb.styles import styles
from reflex import Component, Text


def tabSection() -> rx.Component:
    iconButton = rx.image(
        src="logoMMA.png",
        width="auto",
        height=["40px", "40px", "80px", "80px", "80px"],
        colorScheme="teal",
        size="lg"
        # 2,32 x
    )

    buttonAttr = {
        "width": "10%",
        "minWidth": "60px",
        "color": "white",
        "fontSize": ["10px", "13px", "16px", "2xl", "2xl"],
        "fontWeight": "extrabold",
        "style": {
            "borderTop": "4px",
            "borderColor": "transparent",
            "_hover": {"borderColor": styles.highLight},
        },
    }

    menu = rx.menu(
        rx.menu_button("About", **buttonAttr),
        rx.menu_button(
            "Services",
            **buttonAttr,
            # on_click=lambda x: PropExampleState.focus_me("test"),
        ),
        # rx.menu_button("Home", width="10%", minWidth="60px", color="white"),
        rx.flex(rx.spacer(), iconButton, rx.spacer(), direction="column"),
        rx.menu_button(
            "Works",
            **buttonAttr,
        ),
        rx.menu_button(
            rx.link(
                "Contact",
                href="/contact",
            ),
            **buttonAttr,
        ),
    )
    # PropExampleState.reference = menu

    return rx.flex(
        rx.spacer(),
        menu,
        rx.spacer(),
        # bg="linear-gradient(90deg, rgba(20,13,56,1) 0%, rgba(40,42,47,1) 50%, rgba(20,13,56,1) 100%)",
        # bg="rgb(27, 26, 33)",
        # bg="#FF0080",
        bg="rgb(27, 26, 33, 0.9)",
        width="100%",
        minHeight="59px",
        top="0px",
        position="fixed",
        z_index="10",
    )
