import numpy as np

def var_regression(data, params):
    T = data.shape[0]
    lags = params['P']
    matrix_of_lagged_mats = []
    for lag in range(1, lags + 1):
        matrix_of_lagged_mats.append(data[lags - lag: T - lag, :])
    matrix_of_lagged_mats = np.hstack(matrix_of_lagged_mats)

    trend = np.arange(matrix_of_lagged_mats.shape[0]).reshape(-1, 1)
    matrix_of_lagged_mats = np.hstack([np.ones((matrix_of_lagged_mats.shape[0], 1)), trend, matrix_of_lagged_mats])

    y_matrix = data[lags:, :]

    beta = np.linalg.lstsq(matrix_of_lagged_mats, y_matrix, rcond=None)[0]

    u = y_matrix - matrix_of_lagged_mats @ beta

    varcov_matrix = (u.T @ u) / (T - lags)
    
    p_matrix = np.linalg.cholesky(varcov_matrix)
    d_matrix = np.diag(np.diag(p_matrix))
    a_matrix = p_matrix @ np.linalg.inv(d_matrix)
    a0 = np.linalg.inv(a_matrix)

    coeffs = {
        'u': u,
        'beta': beta,
        'A0': a0 
    }
    
    return coeffs