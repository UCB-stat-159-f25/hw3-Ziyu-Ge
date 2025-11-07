import numpy as np
from pathlib import Path
from ligotools.readligo import loaddata

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
H1 = str(DATA / "H-H1_LOSC_4_V2-1126259446-32.hdf5")

def test_loaddata_shapes_and_dt():
    """strain/time align and have positive dt"""
    strain, time, chan = loaddata(H1)
    assert len(strain) == len(time) > 0
    assert (time[1] - time[0]) > 0
    # finite numbers
    assert np.isfinite(strain).all()
    assert np.isfinite(time).all()

def test_loaddata_channel_is_dict():
    """metadata object is a non-empty dict (as returned by loaddata)"""
    _, _, chan = loaddata(H1)
    assert isinstance(chan, dict)
    assert len(chan) > 0