import numpy as np

def impulse_response_function(coeffs, params):
    impulse = np.zeros((params['irfhorizon'] + params['P'], params['nvar']))
    shock = np.zeros((params['irfhorizon'] + params['P'], params['nvar']))
    shock[params['P'], params['shockPosition'] - 1] = 1
    
    B = np.eye(params['nvar']) 

    for m in range(params['P'], params['irfhorizon'] + params['P']):
        endog_lags = []
        for j in range(1, params['P'] + 1):
            endog_lags.extend(impulse[m - j, :])
        
        endog_lags = np.array(endog_lags)

        impulse[m, :] = (
            endog_lags @ coeffs['beta'][2:, :] + np.linalg.inv(coeffs['A0']) @ B @ shock[m, :]
        ).T

    irf = {
        'point': impulse[params['P']:, :].T 
    }

    return irf