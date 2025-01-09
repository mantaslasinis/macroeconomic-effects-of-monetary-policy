import numpy as np

def newey_west(e, X=None):
    valid_rows = ~np.isnan(X).any(axis=1)
    X = X[valid_rows, :]
    e = e[valid_rows]

    N, k = X.shape

    L = int(np.floor(4 * ((N / 100) ** (2 / 9))))

    Q_matrix = np.zeros((k, k))
    for l in range(L):
        w_l = 1 - l / (L)
        for t in range(l, N):
            if l == 0:
                Q_matrix += e[t] ** 2 * np.outer(X[t, :], X[t, :])  # Use X[t, :] to select the row
            else:
                Q_matrix += w_l * e[t] * e[t - l] * (
                    np.outer(X[t, :], X[t - l, :]) + np.outer(X[t - l, :], X[t, :])
                )
    Q_matrix = Q_matrix / (N - k)
    XTX_inverse = np.linalg.pinv(X.T @ X)
    nwse = np.sqrt(np.diag(N * (XTX_inverse @ Q_matrix @ XTX_inverse)))

    return nwse