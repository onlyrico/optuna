"""

plot_timeline
=============

.. autofunction:: optuna.visualization.plot_timeline

The following code snippet shows how to plot the timeline of a study.
Timeline plot can visualize trials with overlapping execution time
(e.g., in distributed environments).

"""

import time

import optuna
from plotly.io import show


def objective(trial):
    x = trial.suggest_float("x", 0, 1)
    time.sleep(x * 0.1)
    if x > 0.8:
        raise ValueError()
    if x > 0.4:
        raise optuna.TrialPruned()
    return x ** 2


study = optuna.create_study(direction="minimize")
study.optimize(
    objective, n_trials=50, n_jobs=2, catch=(ValueError,)
)

fig = optuna.visualization.plot_timeline(study)
show(fig)

