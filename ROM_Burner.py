import sys

if len(sys.argv) == 1:
    # No arguments: open gui
    import gui
    rbgui = gui.ROMBurnerGUI()
    rbgui.begin()

else:
    # File and port should be passed by the command line
    if len(sys.argv) != 3:
        raise SystemError('ROM_Burner.py: expected two arguments')
    else:
        import files
        import serialinterface

        fname = sys.argv[1]
        pname = sys.argv[2]
        try:
            file = open(fname, 'r')
        except OSError:
            print("File {} could not be found".format(fname))
            exit(-1)

        data = files.parse(file)
        status = serialinterface.send(data, pname)
        if status is False:
            print('Data could not be sent')
