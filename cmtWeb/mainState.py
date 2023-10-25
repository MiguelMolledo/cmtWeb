import reflex as rx


class State(rx.State):
    testCards: list[dict] = [
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
        {"header": "header1", "footer": "footer1", "description": "body1"},
    ]

    serviceInfo: list[dict] = [
        {
            "header": "3D Pipeline",
            "footer": "Provide 3D/VFX/Tracking Tools",
            "description": "",
            "image": "PipeSoftwares.png",
        },
        {
            "header": "BlockChain",
            "footer": "SmartContracts, NFTs, DEFI, AUDIT",
            "description": "",
            "image": "blockchain.png",
        },
        {
            "header": "Front-End",
            "footer": "Provide 3D/VFX/Tracking Tools",
            "description": "",
            "image": "front-end.png",
        },
        {
            "header": "Back-End",
            "footer": "Provide 3D/VFX/Tracking Tools",
            "description": "",
            "image": "backend.png",
        },
        {
            "header": "Consulting",
            "footer": "Provide 3D/VFX/Tracking Tools",
            "description": "",
            "image": "consulting.png",
        },
    ]

    filterWorks: str = "Filter by name"

    @rx.var
    def testFilterWorks(test):
        # print(test)
        # print("------")
        return True

    def filterWorkCards():
        pass
