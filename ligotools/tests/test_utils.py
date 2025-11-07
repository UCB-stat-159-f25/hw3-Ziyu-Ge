import numpy as np
from pathlib import Path
from scipy.io import wavfile

from ligotools.utils import whiten, reqshift
import ligotools.utils as u  # to set u.AUDIO for write_wavfile


def test_whiten():
    fs = 2048.0
    dt = 1.0 / fs
    x = np.random.randn(4096)
    interp_psd = lambda f: np.ones_like(f)
    y = whiten(x, interp_psd, dt)
    assert len(y) == len(x)
    assert np.isfinite(y).all()
    assert np.std(y) > 0


def test_reqshift_shape_and_change():
    fs = 2048
    t = np.arange(4096) / fs
    x = np.sin(2*np.pi*100*t)
    y = reqshift(x, fshift=50, sample_rate=fs)
    assert y.shape == x.shape
    assert not np.allclose(y, x)


def test_write_wavfile_creates_file(tmp_path):
    fs = 4096
    x = np.sin(2*np.pi*100*np.arange(4096)/fs).astype(float)

    outdir = tmp_path / "audio"
    outdir.mkdir(parents=True, exist_ok=True)

    # make the utils function write into our temp dir
    u.AUDIO = outdir

    fname = "test.wav"
    u.write_wavfile(fname, fs, x)  # no 'outdir' kwarg in your function

    outpath = outdir / fname
    assert outpath.exists()

    rate, data = wavfile.read(outpath)
    assert rate == fs
    assert len(data) == len(x)