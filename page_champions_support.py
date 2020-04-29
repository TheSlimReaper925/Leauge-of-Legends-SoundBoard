
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def toChampionsPage():
    destroy_window()


def toGamePage():
    pass


def toSupportLink():
    pass

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None





