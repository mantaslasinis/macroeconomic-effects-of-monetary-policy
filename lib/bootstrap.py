import numpy as np
from joblib import Parallel, delayed
from lib.var_regression import var_regression
from lib.impulse_response_function import impulse_response_function

def bootstrap(data, coeffs, params, irf):
    nobs, nvar = data.shape

    trend = np.arange(nobs)

    low68 = np.zeros((params['irfhorizon'], nvar))
    upp68 = np.zeros((params['irfhorizon'], nvar))
    low95 = np.zeros((params['irfhorizon'], nvar))
    upp95 = np.zeros((params['irfhorizon'], nvar))

    wildBootstrap = 0
    wild = np.zeros(10000)
    if wildBootstrap == 1:
        wildThreshold = int(10000 * ((5**(1 / 5) + 1) / (2 * 5**(1 / 5))))
        wild[:wildThreshold] = -(5**(1 / 5) - 1) / 2
        wild[wildThreshold:] = (5**(1 / 5) + 1) / 2
    elif wildBootstrap == 2:
        wild[:5000] = -1
        wild[5000:] = 1
    wild = wild[np.random.permutation(len(wild))]

    def single_bootstrap_iteration(r):
        rootmax = 100
        while rootmax >= 1:
            draw = np.random.randint(0, nobs - params['P'], size=nobs - params['P'])

            simulation_data = np.zeros((nobs, nvar))
            simulation_data[:params['P'], :] = data[:params['P'], :]

            usim = coeffs['u']

            for p in range(params['P'], nobs):
                if wildBootstrap != 0:
                    resid = wild[np.random.randint(0, 10000)] * usim[draw[p - params['P']], :].T
                else:
                    resid = usim[draw[p - params['P']], :].T

                endogbs_lags = np.hstack([simulation_data[p - j, :] for j in range(1, params['P'] + 1)])

                intercept_and_trend = np.array([1, trend[p]])
                predicted = (
                    intercept_and_trend @ coeffs['beta'][:2, :] +
                    endogbs_lags @ coeffs['beta'][2:, :] +
                    resid.T
                )
                simulation_data[p, :] = predicted

            sim_estimates = var_regression(simulation_data, params)
            pi = np.zeros((nvar * params['P'], nvar * params['P']))
            pi[nvar:, :nvar * (params['P'] - 1)] = np.eye(nvar * (params['P'] - 1))
            pi[:nvar, :] = sim_estimates['beta'][2:, :].T
            rootmax = max(abs(np.linalg.eigvals(pi)))

        irfsim = impulse_response_function(sim_estimates, params)
        return irfsim['point'].T

    boots = Parallel(n_jobs=-1)(delayed(single_bootstrap_iteration)(r) for r in range(params['nreps']))
    boots = np.array(boots)

    for zz in range(nvar):
        for qq in range(params['irfhorizon']):
            dist = boots[:, qq, zz]
            dist_sorted = np.sort(dist)
            low68_idx = int(0.16 * params['nreps']) 
            high68_idx = int(0.84 * params['nreps'])
            low95_idx = int(0.025 * params['nreps'])
            high95_idx = int(0.975 * params['nreps'])

            low68[qq, zz] = dist_sorted[low68_idx]
            upp68[qq, zz] = dist_sorted[high68_idx]
            low95[qq, zz] = dist_sorted[low95_idx]
            upp95[qq, zz] = dist_sorted[high95_idx]

    irf['lower68'] = low68.T
    irf['upper68'] = upp68.T
    irf['lower95'] = low95.T
    irf['upper95'] = upp95.T

    return irf