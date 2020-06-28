import numpy as np
from scipy.stats import beta as beta_dist
from scipy.stats import rice as rice_dist
from pypolinf import fit


def alpha(m_0, mod_m):
    return ((1 - m_0) / (m_0 * mod_m ** 2) - 1) * m_0


def beta(m_0, mod_m):
    return ((1 - m_0) / (m_0 * mod_m ** 2) - 1) * (1 - m_0)


# Number of measurements of FPOL
n = 10
# True mean intrinsic FPOL
m_0_true = 0.2
# True modulation index
mod_m_true = 0.4
print("True mean FPOL: ", m_0_true)
print("True modulation index: ", mod_m_true)
# True variable FPOL values
ms_i_true = beta_dist(alpha(m_0_true, mod_m_true), beta(m_0_true, mod_m_true)).rvs(n)
# Some errors
sigmas = 0.03*np.ones(n)
# Observed variable FPOL values
ms_obs = rice_dist(ms_i_true / sigmas, scale=sigmas).rvs(n)

print("Observed FPOL: ", ms_obs)
print("Errors of FPOL: ", sigmas)

res = fit(ms_obs, sigmas)
print("Estimated mean FPOL: ", res[0])
print("Estimated modulation index: ", res[1])