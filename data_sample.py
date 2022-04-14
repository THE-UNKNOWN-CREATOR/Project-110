import pandas as pd
import plotly.figure_factory as pf
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

def random_set_of_means(counter):    
    data_set = []
    
    for i in range(0, counter):
        rand_index = random.randint(0, len(data)-1)
        value = data[rand_index]
        data_set.append(value)
    
    sample_mean = statistics.mean(data_set)
    return sample_mean 

def plot_data(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    pic = pf.create_distplot([df], ["Claps"], show_hist=False)
    pic.add_trace( go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="mean"))
    pic.show()

def setup():
    mean_list = []
    
    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)

    plot_data(mean_list)

    mean = statistics.mean(mean_list)
    print("sampling mean:- ",mean)

setup()

population_mean = statistics.mean(data)
print("population mean:- ", population_mean)

def standard_def():
    mean_list = []
    
    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)

    std_dev = statistics.stdev(mean_list)
    print(std_dev)

standard_def()