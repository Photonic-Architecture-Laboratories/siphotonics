import numpy as np
from jax import jit
from jax.scipy import ndimage
from trax import fastmath

from siphotonics.util import _read_effective_index

neff_data, width_data, wav_data = _read_effective_index(
    "neff_fitted_Si_fitted_SiO2_width_240_5_700_wav_1200_0p1_1700.csv"
)

wav_size = wav_data.shape[0]
wav_min = np.min(wav_data)
wav_max = np.max(wav_data)

width_size = width_data.shape[0]
width_min = np.min(width_data)
width_max = np.max(width_data)


effective_index_te0, width_data_te0, wav_data_te0 = _read_effective_index(
    "neff_te0_fitted_Si_fitted_SiO2_width_240_5_700_wav_1200_0p1_1700.csv"
)

effective_index_tm0, _, _ = _read_effective_index(
    "neff_tm0_fitted_Si_fitted_SiO2_width_240_5_700_wav_1200_0p1_1700.csv"
)

effective_index_te1, _, _ = _read_effective_index(
    "neff_te1_fitted_Si_fitted_SiO2_width_240_5_700_wav_1200_0p1_1700.csv"
)

effective_index_tm1, _, _ = _read_effective_index(
    "neff_tm1_fitted_Si_fitted_SiO2_width_240_5_700_wav_1200_0p1_1700.csv"
)

effective_index_te2, _, _ = _read_effective_index(
    "neff_te2_fitted_Si_fitted_SiO2_width_240_5_700_wav_1200_0p1_1700.csv"
)

width_size_te0 = width_data_te0.shape[0]
width_min_te0 = np.min(width_data_te0)
width_max_te0 = np.max(width_data_te0)

wav_size_te0 = wav_data_te0.shape[0]
wav_min_te0 = np.min(wav_data_te0)
wav_max_te0 = np.max(wav_data_te0)


@jit
def neff(width, wavelength):
    """
    Gets Effective Index value by using corresponding parameters. This is
    a JAX compatible function. JIT is enabled.
    :param width: Waveguide width in microns. (0.25 - 0.7) Scalar or list
    :param wavelength:
    :return: Effective Index value(s).
    """
    return ndimage.map_coordinates(
        neff_data,
        [
            (wavelength - wav_min) * ((wav_size - 1) / (wav_max - wav_min)),
            (width - width_min) * ((width_size - 1) / (width_max - width_min)),
        ],
        order=1,
    )


@jit
def neff_te0(width, wavelength):
    """
    Gets Effective Index value  of TE0 by using corresponding parameters. This is
    a JAX compatible function. JIT is enabled.
    :param width: Waveguide width in microns. (0.24 - 0.7) Scalar or list
    :param wavelength:
    :return: Effective Index value(s).
    """
    return ndimage.map_coordinates(
        effective_index_te0,
        [
            (width - width_min_te0) * ((width_size_te0 - 1) / (width_max_te0 - width_min_te0)),
            (wavelength - wav_min_te0) * ((wav_size_te0 - 1) / (wav_max_te0 - wav_min_te0)),
        ],
        order=1,
    )


@jit
def neff_tm0(width, wavelength):
    """
    Gets Effective Index value  of TM0 by using corresponding parameters. This is
    a JAX compatible function. JIT is enabled.
    :param width: Waveguide width in microns. (0.24 - 0.7) Scalar or list
    :param wavelength:
    :return: Effective Index value(s).
    """
    return ndimage.map_coordinates(
        effective_index_tm0,
        [
            (width - width_min_te0) * ((width_size_te0 - 1) / (width_max_te0 - width_min_te0)),
            (wavelength - wav_min_te0) * ((wav_size_te0 - 1) / (wav_max_te0 - wav_min_te0)),
        ],
        order=1,
    )


@jit
def neff_te1(width, wavelength):
    """
    Gets Effective Index value  of TE1 by using corresponding parameters. This is
    a JAX compatible function. JIT is enabled.
    :param width: Waveguide width in microns. (0.24 - 0.7) Scalar or list
    :param wavelength:
    :return: Effective Index value(s).
    """
    return ndimage.map_coordinates(
        effective_index_te1,
        [
            (width - width_min_te0) * ((width_size_te0 - 1) / (width_max_te0 - width_min_te0)),
            (wavelength - wav_min_te0) * ((wav_size_te0 - 1) / (wav_max_te0 - wav_min_te0)),
        ],
        order=1,
    )


@jit
def neff_tm1(width, wavelength):
    """
    Gets Effective Index value  of TM1 by using corresponding parameters. This is
    a JAX compatible function. JIT is enabled.
    :param width: Waveguide width in microns. (0.24 - 0.7) Scalar or list
    :param wavelength:
    :return: Effective Index value(s).
    """
    return ndimage.map_coordinates(
        effective_index_tm1,
        [
            (width - width_min_te0) * ((width_size_te0 - 1) / (width_max_te0 - width_min_te0)),
            (wavelength - wav_min_te0) * ((wav_size_te0 - 1) / (wav_max_te0 - wav_min_te0)),
        ],
        order=1,
    )


@jit
def neff_te2(width, wavelength):
    """
    Gets Effective Index value  of TE2 by using corresponding parameters. This is
    a JAX compatible function. JIT is enabled.
    :param width: Waveguide width in microns. (0.24 - 0.7) Scalar or list
    :param wavelength:
    :return: Effective Index value(s).
    """
    return ndimage.map_coordinates(
        effective_index_te2,
        [
            (width - width_min_te0) * ((width_size_te0 - 1) / (width_max_te0 - width_min_te0)),
            (wavelength - wav_min_te0) * ((wav_size_te0 - 1) / (wav_max_te0 - wav_min_te0)),
        ],
        order=1,
    )


@jit
def grad_neff(width, wavelength, mode=1):
    """
    Gets derivatives of Effective Index with respect to waveguide width and
    wavelength.
    :param width: Waveguide width in microns. (0.25 - 0.7)
    :param wavelength: Wavelength in microns. (1.2 - 1.7)
    :param mode: Mode number. (1 - 5)
    :return: A tuple of DeviceArrays. First element corresponds to derivative
    with respect to width. Last element is the derivative with respect to
    wavelength
    """
    return fastmath.grad(neff, (0, 1))(width, wavelength)
