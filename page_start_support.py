def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def toChampionsPage():
    pass


def toGamePage():
    pass


def toSupportLink():
    pass

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import unknown
    unknown.vp_start_gui()




