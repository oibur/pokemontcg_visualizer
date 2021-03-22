import json
import matplotlib.pyplot as plt

#Open each Gen
with open('txt_files/Gen8sort.json') as f: 
    graph_data = json.loads(f.read())

def make_a_graph(x):
    names = []
    number = []
    items = x.items()
    for item in items:
        names.append(item[0]), number.append(item[1]) 
    plt.barh(names, number)
    plt.show()

make_a_graph(graph_data)