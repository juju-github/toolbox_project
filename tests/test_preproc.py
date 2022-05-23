from toolbox_project.preproc import train_test_split_series
import numpy as np

def test_train_test_split_series():
    assert type(np.arange(100)) == np.ndarray
