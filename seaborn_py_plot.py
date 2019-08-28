import seaborn as sns
sns.set()
import numpy as np

# load the tip datase to plot
tips = sns.load_dataset('tips')

tips.head()

sns.distplot(tips['total_bill'],kde=False)

sns.distplot(tips['total_bill'],kde=False, bins =40)

# joint plot
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

# parplot
sns.pairplot(tips, hue='sex', palette = 'coolwarm')

sns.rugplot(tips['total_bill'])

# Don't worry about understanding this code!
# It's just for the diagram below
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min, x_max, 100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4 * dataset.std() ** 5) / (3 * len(dataset))) ** .2

# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    # Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis, kernel, color='grey', alpha=0.5)

plt.ylim(0, 1)

sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)

sns.countplot(x='smoker', data=tips)


sns.boxplot(x='day',y='total_bill', data=tips, hue='smoker')
sns.countplot(x='day',data=tips)

sns.violinplot(x='day',y='total_bill', data=tips, hue='smoker', split=True)

sns.stripplot(x='day', y='total_bill', data=tips, jitter =True)

sns.swarmplot(x='day',y='total_bill', data= tips) # not use at all

# matrix plot

flights = sns.load_dataset('flights')

tc=tips.corr()
sns.heatmap(tc, annot = True)

fc=flights.corr()

flights.pivot_table()





import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')

# Map to upper,lower, and diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")

sns.lmplot()