from csp import *



def main():
    cs = Sudoku(vaikee)
    AC4(cs)
    min_conflicts(cs, max_steps=500000)
    cs.display(cs.infer_assignment())


main()