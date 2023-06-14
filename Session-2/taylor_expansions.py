#! /usr/bin/env python
##
## taylor_expansions.py - An example Python script with Taylor expansion functions
##
## INPUTS:
##    1 = integer describing the highest order term in the polynomial expansion
##
## 2023.06.24 - liac@umich.edu
##--------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

import sys # Python package we will use to grab the in-line inputs to the script

## GOOD PRACTICE: Put any special numbers or hard-coded choices at the top,
## so you can easily remember what choices you made and change as necessary
## without having to search or run find-replace on your code
XGRID = np.linspace(0, 10, 100)

def plot_taylor_expand_exponential(ax, n, x=XGRID, plot_truth=True, **kwargs):
    """
    Compute the Taylor expansion approximation to an exponential function, y = exp(-x),
    and plot the approximation against the true function.
    
    Inputs
    ------
    ax : matplotlib axes object on which to plot
    
    n : int : highest order term to compute in the Taylor expansion
    
    x : numpy array : grid of x values for the function input
    
    plot_truth : bool : If True, plots the true function (exp^-x) in solid black.
    
    **kwargs is passed to plt.plot, which will plot the curve 
        that results from the Taylor expansion
    
    Returns
    -------    
    Plots a Taylor expansion on `ax`, following the approximation:
    y_approx = 1 - x + x^2/2! - x^3/3! + ...

    The true function, y = exp(-x), is plotted with a solid black curve if plot_truth=True
    """
    y = np.exp(-x)
    
    y_approx = 0.0
    for i in range(n+1): # i takes on values 0, 1, 2, ..., n
        y_approx += (-1.0)**(i) * x**i / np.math.factorial(i)

    # This time, call the plot commands from the matplotlib axes object
    if plot_truth:
        ax.plot(x, y, color='k', label='Truth (y = e$^{-x}$)')
    ax.plot(x, y_approx, label='n={} Taylor expansion'.format(n), **kwargs)

    # Some of the plot commands need to be modified from previous use
    ax.set_yscale('log')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    return

## ---------------------------------------------------
## The code below will only run if this Python file is executed from the terminal command line

if __name__ == "__main__":
    # the second thing written on the command line after the command to execute the script
    # read in as a string, cast to an integer
    n = int(sys.argv[1])
    print("Executing Taylor expansion up to order {}".format(n))

    # Set up the axes on which I will draw the plot
    ax = plt.subplot(111)

    # Run the function above
    plot_taylor_expand_exponential(ax, n)
    plt.show() # required when you run matplotlib from the terminal
