# task A
import pandas as pd
import re


def length_stats(text):
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    clean_text = re.sub(r'\d+', '', clean_text)

    words = clean_text.split()

    unique_words = sorted(set(words))

    lengths = pd.Series({word: len(word) for word in unique_words})

    return lengths

# task B
import pandas as pd
import re


def length_stats(text):
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    clean_text = re.sub(r'\d+', '', clean_text)

    words = clean_text.split()

    unique_words = sorted(set(words))

    lengths = pd.Series({word: len(word) for word in unique_words})

    odd = lengths[lengths % 2 != 0]
    even = lengths[lengths % 2 == 0]

    return odd, even

# task C
import pandas as pd


def cheque(price_list, **kwargs):
    data = []

    for product, number in kwargs.items():
        if product in price_list:
            price = price_list[product]
            cost = price * number
            data.append([product, price, number, cost])

    df = pd.DataFrame(data, columns=['product', 'price', 'number', 'cost'])

    df = df.sort_values(by='product').reset_index(drop=True)

    return df

# task D
import pandas as pd


def cheque(price_list, **kwargs):
     data = []

    for product, number in kwargs.items():
        if product in price_list:
            price = price_list[product]
            cost = price * number
            data.append([product, price, number, cost])

    df = pd.DataFrame(data, columns=['product', 'price', 'number', 'cost'])

    df = df.sort_values(by='product').reset_index(drop=True)

    return df


def discount(df):
    discounted_df = df.copy()

    discounted_df.loc[discounted_df['number'] > 2, 'cost'] *= 0.5

    return discounted_df
import pandas as pd


def cheque(price_list, **kwargs):
     data = []

    for product, number in kwargs.items():
        if product in price_list:
            price = price_list[product]
            cost = price * number
            data.append([product, price, number, cost])

    df = pd.DataFrame(data, columns=['product', 'price', 'number', 'cost'])

    df = df.sort_values(by='product').reset_index(drop=True)

    return df


def discount(df):
    discounted_df = df.copy()

    discounted_df.loc[discounted_df['number'] > 2, 'cost'] *= 0.5

    return discounted_df

# task E
import pandas as pd


def cheque(price_list, **kwargs):
    data = []

    for product, number in kwargs.items():
        if product in price_list:
            price = price_list[product]
            cost = price * number
            data.append([product, price, number, cost])

    df = pd.DataFrame(data, columns=['product', 'price', 'number', 'cost'])

    df = df.sort_values(by='product').reset_index(drop=True)

    return df


def discount(df):
    discounted_df = df.copy()

    discounted_df.loc[discounted_df['number'] > 2, 'cost'] *= 0.5

    return discounted_df


def get_long(series, min_length=5):
    filtered_series = series[series.index.str.len() >= min_length]
    return filtered_series

# task F

# task G
import pandas as pd


def need_to_work_better(df):
    filtered_df = df[df.iloc[:, 1:].eq(2).any(axis=1)]
    return filtered_df

# task H

# task I
import pandas as pd

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

xmin, xmax = min(x1, x2), max(x1, x2)
ymin, ymax = min(y1, y2), max(y1, y2)

data = pd.read_csv('data.csv')

filtered_data = data[(data['x'] >= xmin) & (data['x'] <= xmax) & (data['y'] >= ymin) & (data['y'] <= ymax)]

print(filtered_data)

# task J

