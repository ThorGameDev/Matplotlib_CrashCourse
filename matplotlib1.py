import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import random

style.use("dark_background")

def random_dots():
    X_data = np.random.random(1000) * 100
    Y_data = np.random.random(1000) * 100

    plt.scatter(X_data, Y_data, c='#00001f', s=150, marker='*', alpha=0.3)
    plt.show()

def obesity_tracker():
    years = [2006 + x for x in range(16)]
    weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
               82, 82, 83, 81, 80, 79]

    plt.plot(years, weights, c='red', lw=4, linestyle="--")
    plt.show()

def lnaguage_poll():
    x = ["C++", "C#", "Python", "Java", "Go"]
    y = [20, 50, 140, 1, 45]

    plt.bar(x,y,color='r', width=0.5, edgecolor='green', lw=6)
    plt.show()

def histogram():
    ages = np.random.normal(20, 1.5, 1000)

    plt.hist(ages,
             #bins=[ages.min(),18,21,ages.max()],
             bins=20,
             cumulative=True)

    plt.show()

def language_pie_chart():
    langs = ["C++", "C#", "Python", "Java", "Go"]
    votes = [20, 50, 140, 10, 45]
    explodes = [0, 0, 0, 0.2, 0]

    plt.pie(votes, labels=langs, explode=explodes, autopct="%.2f%%", pctdistance=1.3, startangle=90)
    plt.show()

def box_plot():
    heights = np.random.normal(172, 8, 300)
    plt.boxplot(heights)
    plt.show()

def income_tracker():
    years = [2014, 2015, 2016, 2017,
             2018, 2019, 2020, 2021]

    income = [55, 56, 62, 61,
              72, 72, 73, 75]

    income_ticks = list(range(50,81,2))

    plt.plot(years, income)
    plt.title("Income of John (in USD)", fontsize=30)

    plt.xlabel("Year")
    plt.ylabel("Yearly Income in USD")

    plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])

    plt.show()

def stock_tracker():
    stock_a = [100, 102, 99, 101, 101, 100, 102]
    stock_b = [90, 95, 102, 104, 105, 103, 109]
    stock_c = [110, 115, 100, 105, 100, 98, 95]

    plt.plot(stock_a, label="Company1")
    plt.plot(stock_b, label="Company2")
    plt.plot(stock_c, label="Company3")

    plt.legend(loc="lower center")

    plt.show()

def multi():
    x1, y1 = np.random.random(100), np.random.random(100)
    x2, y2 = np.arange(100), np.random.random(100)

    plt.figure(1)
    plt.scatter(x1, y1)

    plt.figure(2)
    plt.plot(x2, y2)

    plt.show()

def subplots():
    x = np.arange(100)
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(x, np.sin(x))
    axs[0, 0].set_title("Sine Wave")
    axs[0, 0].set_xlabel("TEST")

    axs[0, 1].plot(x, np.cos(x))
    axs[0, 1].set_title("Cosine Wave")

    axs[1, 0].plot(x, np.random.random(100))
    axs[1, 0].set_title("Random Function")

    axs[1, 1].plot(x, np.log(x))
    axs[1, 1].set_title("Log")


    fig.suptitle("Four Plots")

    plt.tight_layout()

    plt.savefig("fourplots.png", dpi=300,
                transparent=False, bbox_inches="tight")

def three_dimensional_scatter():
    ax = plt.axes(projection="3d")

    x = np.random.random(100)
    y = np.random.random(100)
    z = np.random.random(100)

    ax.scatter(x, y, z)
    ax.set_title("3D Plot")
    ax.set_xlabel("x")

    plt.show()

def trig_spiral():
    ax = plt.axes(projection="3d")

    x = np.arange(0,50,0.1)
    y = np.sin(x)
    z = np.cos(x)

    ax.plot(x, y, z)
    ax.set_title("3D Spiral")
    plt.show()

def surface_plot():
    ax = plt.axes(projection="3d")

    x = np.arange(-5, 5, 0.1) 
    y = np.arange(-5, 5, 0.1) 

    X, Y = np.meshgrid(x, y)

    Z = np.sin(X) * np.cos(Y)

    ax.plot_surface(X, Y, Z, cmap="Spectral")
    ax.set_title("3D meshgrid")
    plt.show()

def coin_flips():
    heads_tails = [0, 0]
    
    for _ in range(100000):
        heads_tails[random.randint(0,1)] += 1
        plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
        plt.pause(0.0001)

    plt.show
coin_flips()
