import numpy as np
from lib.newey_west import newey_west

def local_projection(data, params):
    Y = data['end'][params['Start']:, :]
    num_vars = Y.shape[1]

    irf = {
        'point': np.zeros((params['irfhorizon'], num_vars)),
        'SE': np.zeros((params['irfhorizon'], num_vars))
    }

    laggedShocks = np.zeros((data['Shocks'].shape[0], params['Q']))
    for j in range(params['Q']):
        laggedShocks[j+1:, j] = data['Shocks'][:-(j+1), 0]

    for v in range(num_vars):
        data_end = data['end']

        if params['allControls'] == 0:
            data_mat = np.zeros_like(data_end)
            data_mat[1:, v] = data_end[1:, v] - data_end[:-1, v]
        else:
            data_mat = np.zeros_like(data_end)
            data_mat[1:, :] = data_end[1:, :] - data_end[:-1, :]

        X = []
        num_rows = data_mat.shape[0] - params['P']
        for k in range(data_mat.shape[1]):
            for j in range(params['P']):
                start_idx = params['P'] - j - 1
                end_idx = -j - 1 if j > 0 else None
                slice_ = data_mat[start_idx:end_idx, k]
                X.append(slice_[:num_rows])

        X = np.column_stack(X)

        xx = X[params['Start']-params['P']:, :]

        max_horizon = params['irfhorizon'] if params['Contemp'] else params['irfhorizon'] - 1

        for h in range(max_horizon):
            YY = Y[h+1:, v] - Y[:len(Y)-h-1, v]
            if params['Contemp'] == 1:
                XX = np.column_stack((
                    data["Shocks"][params["Start"]+1:len(data['Shocks'])-h],
                    data['Shocks'][params['Start']:len(data['Shocks'])-h-1],
                    laggedShocks[params['Start']:len(laggedShocks)-h-1, :],
                    data_mat[params['Start']:len(data_mat)-h-1, :],
                    xx[:len(xx)-h-1, :],
                    np.ones((YY.shape[0], 1))
                ))
            else:
                XX = np.column_stack((
                    data["Shocks"][params["Start"]:len(data['Shocks'])-h-1],
                    laggedShocks[params['Start']:len(data['Shocks'])-h-1, :],
                    data_mat[params['Start']:len(data_mat)-h-1, :],
                    xx[0:len(xx)-h-1, :],
                    np.ones((YY.shape[0], 1))
                ))

            beta = np.linalg.pinv(XX.T @ XX) @ (XX.T @ YY)
            EE = YY - XX @ beta

            newey_west_se = newey_west(EE, XX)

            if params['Contemp']:
                irf['point'][h, v] = beta[0]
                irf['SE'][h, v] = newey_west_se[0]
            else:
                irf['point'][h+1, v] = beta[0]
                irf['SE'][h+1, v] = newey_west_se[0]

    irf['upper95'] = irf['point'] + 1.96 * irf['SE']
    irf['lower95'] = irf['point'] - 1.96 * irf['SE']
    irf['upper68'] = irf['point'] + 1.00 * irf['SE']
    irf['lower68'] = irf['point'] - 1.00 * irf['SE']

    return irf