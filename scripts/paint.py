# I just want to use this in several files without pasting the same code
# thank you for understanding

def color(text,rgb,back=False):
    # Color code is formatted as \x1b[ (foreground 38, background 48) ; 2 (true color) ; red ; green ; blue m
    position = 4 if back else 3
    end = "\x1b[0m"
    return "\x1b[{}8;2;{};{};{}m{}{}".format(position,rgb[0],rgb[1],rgb[2],text,end)