from color import Color 


if __name__ == "__main__":
    Color.print("<r>Red <g>Green")
    Color.print("<r>Red", "<g>Green", sep=":")
    Color.print("<bld><r>Red and bold <g>Green and bold")
    Color.print("<bld><r>Red and bold <clr><g>Green")

    decolored = Color.print2("<r>Print red and print decolored")
    print(decolored[0])
