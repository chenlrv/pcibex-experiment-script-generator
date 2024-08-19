import pandas as pd

with open('demo_items.csv') as demo_items:
    demo_items = pd.read_csv(demo_items)

with open('demo_practice.csv') as demo_practice:
    demo_practice = pd.read_csv(demo_practice)

