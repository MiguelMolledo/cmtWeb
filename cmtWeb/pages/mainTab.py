import reflex as rx
from cmtWeb.styles import styles
from reflex import Component, Text


class PropExampleStateTest(rx.State):
    borderColorOver: str = "black"

    def on_mouse_over(self):
        print("mouse over")
        self.borderColorOver = styles.light

    def on_mouse_out(self):
        self.borderColorOver = "black"


def tabSection() -> rx.Component:
    iconButton = rx.image(
        src="logoMMA.png",
        width="188px",
        height="80px",
        colorScheme="teal",
        size="lg"
        # 2,32 x
    )

    buttonAttr = {
        "width": "10%",
        "minWidth": "60px",
        "color": "white",
        "fontWeight": "extrabold",
        "style": {
            "borderTop": "4px",
            "borderColor": "black",
            "_hover": {"borderColor": "#FF0080"},
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
        iconButton,
        rx.menu_button(
            "Works",
            **buttonAttr,
        ),
        rx.menu_button(
            "Contact",
            **buttonAttr,
        ),
    )
    # PropExampleState.reference = menu

    return rx.flex(
        rx.spacer(),
        menu,
        rx.spacer(),
        # bg="linear-gradient(90deg, rgba(20,13,56,1) 0%, rgba(40,42,47,1) 50%, rgba(20,13,56,1) 100%)",
        bg="rgb(27, 26, 33)",
        width="100%",
        minHeight="59px",
        top="0px",
        position="fixed",
        z_index="10",
    )


# def sidebar() -> rx.Component:
#     return rx.box(
#         rx.vstack(
#             rx.image(src="/favicon.ico", margin="0 auto"),
#             rx.heading(
#                 "Sidebar",
#                 text_align="center",
#                 margin_bottom="1em",
#             ),
#             rx.menu(
#                 rx.menu_button("About", width="10%", minWidth="60px", color="white"),
#                 rx.menu_button("Services", width="10%", minWidth="60px", color="white"),
#                 rx.menu_button("Home", width="10%", minWidth="60px", color="white"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Works", width="10%", minWidth="60px", color="black"),
#                 rx.menu_button("Contact", width="10%", minWidth="60px", color="white"),
#             ),
#             width="250px",
#             padding_x="2em",
#             padding_y="1em",
#         ),
#         position="fixed",
#         height="100%",
#         left="0px",
#         top="0px",
#         z_index="500",
#     )
