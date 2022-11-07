import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2


def plot_correlation_vectors( objective_function, plotter="default", plot_options="default" ):
  if plotter      == "default":  plotter = plt
  if plot_options == "default":  plot_options = "b."
  
  for vector in list(zip(*(objective_function.correlation_vector_matrix))):
    plotter.plot(objective_function.radii, vector, plot_options)
  return plotter


def plot_mean_vector( objective_function, plotter="default", plot_options="default" ):
  if plotter      == "default":  plotter = plt
  if plot_options == "default":  plot_options = "g."
  
  plotter.plot(objective_function.radii, objective_function.mean_vector, plot_options)
  return plotter


def plot_chi2_test( objective_function, plotter="default", n_bins=[], plot_options="default" ):
  if plotter      == "default":  plotter = plt
  if plot_options == "default":  plot_options = "r-"

  n_logl    = [ objective_function.eval_f(vector) \
                for vector in np.transpose(objective_function.correlation_vector_matrix) ]
  if n_bins == []:
    khi, bins = np.histogram( n_logl )
  else:
    khi, bins = np.histogram( n_logl, n_bins )
  khi_n     = [ x / sum(khi) / (bins[1] - bins[0]) for x in khi ]
  plotter.hist(bins[:-1], bins, weights=khi_n)
  df = len( objective_function.correlation_vector_matrix )
  x  = np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99,df), 100)
  plotter.plot(x, chi2.pdf(x, df),plot_options, lw=5, alpha=0.6, label='chi2 pdf')
  return plotter
