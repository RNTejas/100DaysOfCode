import pandas as pd

red = []
black = []
gray = []

data = pd.read_csv('squirrel_data.csv')
fur_column = data['Primary Fur Color']
for squirrel in fur_column:
    if squirrel == 'Gray':
        gray.append(squirrel)
    elif squirrel == 'Black':
        black.append(squirrel)
    elif squirrel == 'Cinnamon':
        red.append(squirrel)

df = pd.DataFrame(
    {
        'squirrels': ['red', 'black', 'gray'],
        'numbers': [len(red), len(black), len(gray)]
    }
)
df.to_csv('squirrel_data_analyzed.csv')