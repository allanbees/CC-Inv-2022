import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_data(filename):
    df = pd.read_csv(filename)
    data = np.array(df, dtype=float).flatten()
    return data

def t_array(x, t, th, remove_outliers=True):
    iters = x.shape[0] // t
    DATA = np.array([])
    T_DATA = np.array([])
    outliers = 0
    total = 0
    for i in range(iters):
        start = i * t
        end = start + t
        data = x[start:end]
        if remove_outliers:
            quartiles = np.quantile(data, [0.25, 0.75])
            q1 = quartiles[0]
            q3 = quartiles[1]
            iqr = q3 - q1
            bottom_limit = q1 - 1.5 * iqr
            upper_limit = q1 + 1.5 * iqr
            mask = (bottom_limit <= data) & (data <= upper_limit) & (data < th)
            data = data[mask]
            outliers += t - data.shape[0]
            total += t
        mean = np.mean(data)
        DATA = np.append(DATA, mean)
        T_DATA = np.append(T_DATA, end)
    return T_DATA, DATA

def plot(x, y, title=''):
    plt.plot(x, y)
    plt.title(title)
    plt.show()

def scatter(x, y, title=''):
    plt.scatter(x, y)
    plt.title(title)
    plt.show()

def plot_title(t, th):
    return f't={t} th={th}'

def get_events(data):
    n = data.shape[0]
    i = 0
    events = []
    while i < n:
        value = data[i]
        if np.isnan(value):
            i += 1
            continue
        event = np.array([])
        while not np.isnan(value):
            event = np.append(event, value)
            i += 1
            if i >= n:
                break
            value = data[i] 
        events.append(event)
    return events

def event_slope(event):
    n = event.shape[0]
    slope = 0
    for i in range(1, n):
        slope += event[i] - event[i - 1]
    return slope

def count(events):
    entries = 0
    exits = 0
    for event in events:
        slope = event_slope(event)
        if slope < 0:
            entries += 1
        elif slope > 0:
            exits += 1
    final_count = entries - exits
    return entries, exits, final_count

# results: [en, ex]
# expected: [en, ex]
def get_accuracy(results, expected):
    def accuracy(r, e):
        if r <= 0:
            diff = 1 - r
            e += diff
            r += diff
        if r <= e:
            acc = r / float(e)
        elif r > e:
            acc = e / float(r)
        return acc

    # Entries Accuracy
    en_r = results[0] # Entries Result
    exp_en = expected[0] # Expected Entries
    en_acc = accuracy(en_r, exp_en)

    # Exits Accuracy
    ex_r = results[1] # Exits Result
    exp_ex = expected[1] # Expected Exits
    ex_acc = accuracy(ex_r, exp_ex)

    return round(en_acc * ex_acc, 4)