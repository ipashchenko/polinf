# polinf
Estimating mean intrinsic fractional polarization (FPOL) and intrinsic variability (modulation index) using sequence of the observed FPOL values and their errors. Implementation of the approach described in Appendix A of Blinov et al. 2016j (doi:10.1093/mnras/stw158) 

## Installation
First, install ``boost``, ``dlib`` and ``pybind11`` C++ libraries. 
Clone repo:
```
$ git clone https://github.com/ipashchenko/polinf.git
$ cd polinf
```
Compile:
```
$ c++ -O3 -Wall -shared -std=c++17 -fPIC -ldlib -march=native -DNDEBUG -O3 -fext-numeric-literals `python3 -m pybind11 --includes` -o pypolinf`python3-config --extension-suffix` pypolinf.cpp
```
This creates ``*.so`` shared library file (e.g. ``pypolinf.cpython-38-x86_64-linux-gnu.so``) that can be used to import ``fit`` function from Python:
```
$ python -c "from pypolinf import fit"
```

## Usage
Imported function ``fit`` takes two positional arguments - iterables of FPOL values and their uncertainties, and returns tuple of mean intrinsic FPOL and intrinsic modulation index.
```
>>> FPOL_mean, mod_indx = fit(FPOL, sigma_FPOL)
```

## Examples
Example usage shown in ``example.py`` (first, compile shared library).