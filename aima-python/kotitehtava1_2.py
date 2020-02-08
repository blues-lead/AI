#%%
from csp import *
import time
import pickle

info_backtrack_noopts = {} # for gathering information of all the options
levels = {'easy1':easy1, 'vaikee':vaikee, 'harder1':harder1, 'keskivaikee':keski_vaikee, 'erittain_vaikee':erittain_vaikee}
#%% Backtracking algorithm with options
pi_backtrack_noopts = open("btwopts.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    backtracking_search(h, mrv, lcv, forward_checking) 
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
    print("Solved", level, "in ", end_time - start_time, "seconds")
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()
#%% AC3 with no options
pi_backtrack_noopts = open("AC3nopts.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    #backtracking_search(h, mrv, lcv, forward_checking)
    AC3(h, arc_heuristic=no_arc_heuristic)
    #backtracking_search(h)
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    if len(h.infer_assignment()) == 81:
        info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
        print("Solved", level, "in ", end_time - start_time, "seconds")
    else:
        print('Not Solved')
        info_backtrack_noopts[level] = 'Not Solved'
    
    
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()
#%% AC3b with options
pi_backtrack_noopts = open("AC3bwopts.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    #backtracking_search(h, mrv, lcv, forward_checking)
    AC3b(h)
    #backtracking_search(h)
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    if len(h.infer_assignment()) == 81:
        info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
        print("Solved", level, "in ", end_time - start_time, "seconds")
    else:
        print('Not Solved')
        info_backtrack_noopts[level] = 'Not Solved'
    
    
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()
#%% AC4 with options
pi_backtrack_noopts = open("AC4wopts.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    #backtracking_search(h, mrv, lcv, forward_checking)
    AC4(h)
    #backtracking_search(h)
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    if len(h.infer_assignment()) == 81:
        info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
        print("Solved", level, "in ", end_time - start_time, "seconds")
    else:
        print('Not Solved')
        info_backtrack_noopts[level] = 'Not Solved'
    
    
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()
#%% AC3 noopts + backtracking
pi_backtrack_noopts = open("AC3nopts_bt.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    #backtracking_search(h, mrv, lcv, forward_checking)
    AC3(h, arc_heuristic=no_arc_heuristic)
    backtracking_search(h)
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    if len(h.infer_assignment()) == 81:
        info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
        print("Solved", level, "in ", end_time - start_time, "seconds")
    else:
        print('Not Solved')
        info_backtrack_noopts[level] = 'Not Solved'
    
    
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()
#%% AC3b + backtracking
pi_backtrack_noopts = open("AC3b_bt.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    #backtracking_search(h, mrv, lcv, forward_checking)
    AC3b(h)
    backtracking_search(h)
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    if len(h.infer_assignment()) == 81:
        info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
        print("Solved", level, "in ", end_time - start_time, "seconds")
    else:
        print('Not Solved')
        info_backtrack_noopts[level] = 'Not Solved'
    
    
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()
#%% AC4 + backtracking
pi_backtrack_noopts = open("AC4_bt.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    AC4(h)
    backtracking_search(h)
    #backtracking_search(h, mrv, lcv, forward_checking)
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    if len(h.infer_assignment()) == 81:
        info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
        print("Solved", level, "in ", end_time - start_time, "seconds")
    else:
        print('Not Solved')
        info_backtrack_noopts[level] = 'Not Solved'
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()
#%% Backtracking with no options
pi_backtrack_noopts = open("btnopts.pickle", "wb")
for level in levels: # with options of backtracking search
    h  = Sudoku(levels[level])
    print("Solving", level, "level of Sudoku...")
    start_time = time.perf_counter()
    backtracking_search(h)
    end_time = time.perf_counter()
    h.display(h.infer_assignment())
    info_backtrack_noopts[level] = '{:.3f}'.format(end_time - start_time)
    print("Solved", level, "in ", end_time - start_time, "seconds")
pickle.dump(info_backtrack_noopts, pi_backtrack_noopts)
pi_backtrack_noopts.close()

# %%
