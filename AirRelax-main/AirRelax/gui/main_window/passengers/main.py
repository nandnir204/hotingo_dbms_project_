from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller

from .add_passengers.gui import AddPassengers
from .view_passengers.main import ViewPassengers
from .update_passengers.main import UpdatePassengers

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def passengers():
    Passengers()


class Passengers(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.guest_data = db_controller.get_passengers()

        self.configure(bg="#FFFFFF")

        # Loop through windows and place them
        self.windows = {
            "add": AddPassengers(self),
            "view": ViewPassengers(self),
            "edit": UpdatePassengers(self),
        }

        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=1013.0, height=506.0)

        self.current_window.tkraise()

    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1013.0, height=506.0)
