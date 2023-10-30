import reflex as rx
from typing import Dict, List


class State(rx.State):
    workData: List[Dict[str, str]] = [
        {
            "header": "Tmnt Film tools",
            "footer": "Pipeline 3D",
            "description": "tmnt.png",
            "link": "https://youtu.be/IHvzw4Ibuho?si=rNoGiMSW1eu0onng",
        },
        {
            "header": "SpellBound Film tools",
            "footer": "Pipeline 3D",
            "description": "skydance.png",
            "link": "https://www.skydance.com/",
        },
        {
            "header": "Mummies Film Tools",
            "footer": "Pipeline 3D/Backend",
            "description": "mummies.png",
            "link": "https://www.youtube.com/watch?v=WRB8YIc4U68",
        },
        {
            "header": "Blue & Malone",
            "footer": "Pipeline 3D",
            "description": "bluemalone.png",
            "link": "https://www.youtube.com/watch?v=2PKYobvej8M",
        },
        {
            "header": "WonderPark",
            "footer": "Pipeline 3D",
            "description": "wonderpark.png",
            "link": "https://youtu.be/vYm7mYd0SgE?si=2H2l8ereiXSLwI4l",
        },
        {
            "header": "Illusorium",
            "footer": "Pipeline 3D",
            "description": "wonderpark.png",
            "link": "Illusorium.png",
        },
        {
            "header": "SimpleCloud",
            "footer": "Pipeline 3D/Backend",
            "description": "simpleCloud.png",
            "link": "https://www.simplecloud.io/",
        },
        {
            "header": "Sanity Checks",
            "footer": "Pipeline 3D",
            "description": "checkList.png",
        },
        {
            "header": "Blue & Malone",
            "footer": "Pipeline 3D",
            "description": "bluemalone.png",
            "link": "https://www.youtube.com/watch?v=2PKYobvej8M",
        },
        {"header": "CriticalMinds Business", "footer": "Web", "description": "wip.png"},
        {"header": "Samoytek Solutions", "footer": "Web", "description": "wip.png"},
        {"header": "Podcast Medjugoria", "footer": "web", "description": "wip.png"},
        {
            "header": "NFTs Platform",
            "footer": "Blockhain/Web",
            "description": "Nft.png",
        },
        {
            "header": "Dex Platform",
            "footer": "Blockhain/Web",
            "description": "trading.png",
        },
        {
            "header": "Betting Platform",
            "footer": "Blockhain",
            "description": "betting.png",
        },
    ]

    serviceInfo: List[Dict[str, str]] = [
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
        {
            "header": "3D Pipeline",
            "footer": "Provide 3D/VFX/Tracking Tools",
            "description": "",
            "image": "PipeSoftwares.png",
        },
    ]

    filterWorksExpression: str = ""

    @rx.cached_var
    def filteredWorkData(self) -> List[Dict[str, str]]:
        return [
            row
            for row in self.workData
            if not self.filterWorksExpression.lower()
            or self.filterWorksExpression.lower() in row["header"].lower()
            or self.filterWorksExpression.lower() in row["footer"].lower()
        ]

    def inputWorkFilter(self, value):
        self.filterWorksExpression = value
        yield rx.console_log(f"Filter set to: {self.filterWorksExpression}")

    def goToContact(self):
        rx.redirect("/contact")

    def goToHome(self):
        rx.redirect("/")
