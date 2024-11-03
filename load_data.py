import re
import networkx as nx
import matplotlib
import pandas as pd

matplotlib.use('TkAgg')

attributes_path = './data/attributes/'
lexicon_path = './data/lexicon.txt'
link_path = './data/links.txt'


def build_graph():
    G = nx.Graph()
    for i in range(1, 16008):
        with open(attributes_path + str(i) + '.txt', 'r', encoding='utf-8') as f:
            description = f.read().replace('\n', ',')
            G.add_node(i, description=set(description.split(',')))
    with open(link_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            numbers = [int(num) for num in re.findall(r'\d+', line)]
            G.add_edge(numbers[0], numbers[1])
    # nx.draw_networkx(G, with_labels=False)
    return G


def load_lexicon():
    with open(lexicon_path, 'r', encoding='utf-8') as f:
        return f.read().split('\n')


def linkstxt2csv():
    data = []
    with open(link_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            numbers = [int(num) for num in re.findall(r'\d+', line)]
            data.append([numbers[0], numbers[1]])
    df = pd.DataFrame(data, columns=['a', 'b'])
    df.to_csv('links.csv', index=False, header=False)
