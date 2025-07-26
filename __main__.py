# __main__.py

from tkinter import Tk
from ui.main_window import StudyTrackerApp

if __name__ == "__main__":
    root = Tk()
    app = StudyTrackerApp(root)
    root.mainloop()