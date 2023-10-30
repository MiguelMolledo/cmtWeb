import reflex as rx
from typing import Dict, List
from cmtWeb import data


class State(rx.State):
    serviceInfo: List[Dict[str, str]] = data.SERVICE_DATA

    aboutDescription: str = data.ABOUT_DESCRIPTION

    workData: List[Dict[str, str]] = data.WORK_DATA
    filterWorksExpression: str = "Filter here"

    @rx.cached_var
    def filteredWorkData(self) -> List[Dict[str, str]]:
        if self.filterWorksExpression == "Filter here":
            return self.workData

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
        rx.console_log("Redirecting to contact page...")
        yield rx.console_log("Redirecting to contact page...")

    def goToHome(self):
        rx.redirect("/")
