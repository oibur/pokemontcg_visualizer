import json
import matplotlib. pyplot as plt
import pygal

def make_a_graph(Genx_txt):
    with open(Genx_txt) as f: 
        data = f.read()
        data_dict = json.loads(data)
        names = []
        number = []
        items = data_dict.items()
        for item in items:
            names.append(item[0]), number.append(item[1]) 
        plt.barh(names, number)
        plt.show()

make_a_graph('Gen'+input("what Gen would you like to see? ")+'.txt')