from utils import *

data = get_data('data/EXP_3.csv')
t_data, data = t_array(data, 30, 150)
events = get_events(data)
en, ex, fc = count(events)

print(f'{en}, {ex}, {fc}')
plot(t_data, data)