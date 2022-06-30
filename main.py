from utils import *

# Experiments: File - Expected [Entries, Exits]
experiments = [
    { 'file': 'data/EXP_1.csv', 'expected': [9, 0], 'result': 'results/RES_1.csv' },
    { 'file': 'data/EXP_2.csv', 'expected': [0, 9], 'result': 'results/RES_2.csv'  },
    { 'file': 'data/EXP_3.csv', 'expected': [6, 6], 'result': 'results/RES_3.csv'},
]

# Parameters
ts = [ 1, 5, 10, 20, 30, 50, 60, 70, 80, 100 ]
ths = [ 10, 25, 50, 75, 100, 110, 125, 150, 175, 200, 210, 225, 250, 275, 400, 1000 ]


for experiment in experiments:
    print(experiment['file'])
    x = get_data(experiment['file'])
    results = None

    for t in ts:
        for th in ths:
            # Remove outliers = True
            t_data, data = t_array(x, t, th)
            events = get_events(data)
            en, ex, fc = count(events)
            result = [en, ex]
            acc = get_accuracy(result, experiment['expected'])

            result = np.array([t, th, 1, acc])
            if results is None:
                results = result
            else:
                results = np.vstack([results, result])

            # Remove outliers = False
            t_data, data = t_array(x, t, th, False)
            events = get_events(data)
            en, ex, fc = count(events)
            result = [en, ex]
            acc = get_accuracy(result, experiment['expected'])

            result = np.array([t, th, 0, acc])
            results = np.vstack([results, result])

    np.savetxt(experiment['result'], results, delimiter=',')
    
