import pickle
files = {'AC3b with back-tracking': 'AC3b_bt.pickle',
        'AC3b with heuristic': 'AC3bwopts.pickle',
        'AC3 no-heuristics with back-tracking': 'AC3nopts_bt.pickle',
        'Pure AC3 algorithm with basic heuristic':'AC3nopts.pickle',
        'AC4 with back-tracking':'AC4_bt.pickle',
        'AC4 without back-tracking':'AC4wopts.pickle',
        'Back-tracking with all options':'btwopts.pickle'}
for fl in files:
    #print(files[fl])
    #breakpoint()
    unpick = open(files[fl],'rb')
    data = pickle.load(unpick)
    unpick.close()
    print("Results of", fl, "algorithm")
    for value in data:
        print("{:20} \t {:>10}".format(value,data[value]))
    print()