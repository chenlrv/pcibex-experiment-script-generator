import pandas as pd

with open('demo_items.csv') as f:
    demo_items = pd.read_csv(f)

with open('demo_practice.csv') as f:
    demo_practice = pd.read_csv(f)

with open('RSVP_fixed_point.txt', 'r') as f:
    rsvp_fixed_script = f.read()

with open('SPR_moving_window.txt', 'r') as f:
    SPR_moving_script = f.read()

