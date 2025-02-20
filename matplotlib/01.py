import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


# Create the plot
plt.figure(figsize=(10*np.pi, 5))
plt.title(
        'Plot of $cos(x) and sin(x)$')
plt.xlabel('x')
plt.ylabel('cos(x) and sin(x)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.xlim(0, 9*np.pi)
plt.ylim(-1.5, 1.5)

# Set x-ticks at multiples of pi
pi_ticks = np.arange(0, 9*np.pi, np.pi)  # Create ticks at multiples of pi
pi_labels = [f'{i}π' for i in range(len(pi_ticks))]  # Create labels

# Set the ticks and labels
plt.xticks(pi_ticks, pi_labels)


def f(x):
    return np.cos(x)


def g(x):
    return np.sin(x)


x = np.linspace(0, 9*np.pi, 1000)

plt.plot(x,
         f(x),
         label=r'$\cos(x)$',
         color='yellow')


plt.plot(x,
         g(x),
         label=r'$\sin(x)$',
         color='green')


plt.legend()
plt.savefig('function_plot.png', format='png', dpi=300)


# README
#
# on your host machine run
#   podman run --volume ~/git-repos/python/matplotlib/:/main --name matplotlib.python --rm -u nobody -it python bash
#
# then in the container run
#   pip install matplotlib
#   cd /main
#   python 01.py
#
# open the file named `function_plot.png` on your host machine
