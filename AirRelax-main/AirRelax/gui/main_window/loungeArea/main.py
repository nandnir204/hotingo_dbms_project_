from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller


from .add_lounges.gui import AddLounges
from .view_lounges.main import ViewLounges
from .update_lounges.main import UpdateLounges

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def lounges():
    Lounges()


class Lounges(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.room_data = db_controller.get_lounges()

        self.configure(bg="#FFFFFF")

        # Loop through windows and place them
        self.windows = {
            "add": AddLounges(self),
            "view": ViewLounges(self),
            "edit": UpdateLounges(self),
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
