from scipy import special

# Another source for more specialized and obscure ufuncs is the submodule scipy.special

# Gamma functions
x = [1, 5, 10]
print("gamma(x)     =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2)   =", special.beta(x, 2))
