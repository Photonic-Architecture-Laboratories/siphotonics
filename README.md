[![build](https://github.com/Photonic-Architecture-Laboratories/si-photonics-toolkit/actions/workflows/makefile.yml/badge.svg)](https://github.com/Photonic-Architecture-Laboratories/si-photonics-toolkit/actions/workflows/makefile.yml)
[![Documentation Status](https://readthedocs.org/projects/sipkit/badge/?version=latest)](https://sipkit.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/sipkit.svg)](https://badge.fury.io/py/sipkit)

# Silicon Photonics Toolkit

Numerical simulations are essential for modeling and predicting the behavior of complex systems in many fields of research and development including applications in physics and material science, medical and biological sciences, environmental sciences, and many engineering disciplines [1-15]. The accuracy of simulation results in many of these examples depends on externally specified or separately simulated sets of parameters, which have critical implications for the outcome of the simulations. For example, many physical properties of materials play critical roles in shaping the performance of electro-optical and micro-electromechanical devices that underpin today’s modern computing and communications infrastructure [1-6]. Thermodynamic behavior and properties of chemical mixtures are instrumental in understanding and designing more efficient and cost-effective chemical processes [7-11]. The biomechanical properties of tissues, including their tensile and elastic properties, can have a direct impact on the design choices of numerous medical devices including implants [12-15]. As more devices and systems in virtually all areas of science and engineering are being designed and optimized by machine learning-based techniques today, efficient and rapid access to such application-specific parameters remains an important requirement in the future landscape of scientific design and modeling.

In integrated optics, accessing optical parameters of waveguides is one of the most important yet recurring tasks in the process of designing photonic devices. Silicon Photonics Toolkit (sipkit) is a python package that provides computationally efficient access to waveguide parameters as functions of key optical and physical variables, to aid the design of silicon photonic systems and scientific discovery through integrated optics. In addition to its state-of-the-art data mapping for rapid parameter access, sipkit also allows for full automatic-differentiation capability through its compatibility with JAX. With efficient gradient computation for optimization algorithms, sipkit can therefore be used in the design of photonic systems using modern machine learning methods. With this combination of streamlined data access and support for automatic differentiation, sipkit enables researchers and engineers to design complex photonic systems with greater efficiency and flexibility.




## Getting Started

**Silicon Photonics Toolkit** is a toolkit providing fundamental waveguide and material properties to aid in the design of silicon photonic components on silicon-on-insulator platforms with high accuracy and extremely fast runtime. All the waveguide parameters returned by sipkit are calculated for 220-nm-thick strip waveguides on a SOI. See the [documentation](https://sipkit.readthedocs.io/en/latest/) for tutorials and API reference.

## Installation

### Pip

The package can be installed via pip:

    pip install sipkit

You can install siphotonics with additional packages for developers:

    pip install sipkit[dev]

### Build from source

Alternatively, the package can be built from source by cloning the repository and running the setup script:

    git clone https://github.com/Photonic-Architecture-Laboratories/si-photonics-toolkit.git
    cd si-photonics-toolkit
    pip install -e .

## Dependencies

The package requires the following packages to be installed:

-   [NumPy](https://numpy.org/)
-   [Jax](https://jax.readthedocs.io/en/latest/index.html)

## Citing SiPhotonics Toolkit

    @article{silicon-photonics-toolkit2023opticaopen,
        author = {Aycan Deniz Vit and Kazim Gorgulu and Ali Najjar Amiri and Emir Salih Magden},
        title = {Silicon Photonics Toolkit},
        journal = {Optica Open},
        year = {2023},
        note = {Preprint},
        doi = {10.1364/opticaopen.23098334.v1},
        url = {https://doi.org/10.1364/opticaopen.23098334.v1},
        description = {A toolkit to rapidly lookup parameters for the design of silicon photonic components with automatic differentiation capability.}
    }


## References

1- Dunn, A., Wang, Q., Ganose, A., Dopp, D., & Jain, A. (2020). Benchmarking materials property prediction methods: the Matbench test set and Automatminer reference algorithm. npj Computational Materials, 6(1), 138. 

2- Magden, E. S., Li, N., Raval, M., Poulton, C. V., Ruocco, A., Singh, N., ... & Watts, M. R. (2018). Transmissive silicon photonic dichroic filters with spectrally selective waveguides. Nature communications, 9(1), 3009. 

3- Ong, S. P., Richards, W. D., Jain, A., Hautier, G., Kocher, M., Cholia, S., ... & Ceder, G. (2013). Python Materials Genomics (pymatgen): A robust, open-source python library for materials analysis. Computational Materials Science, 68, 314-319. 

4- Tambasco, J., Gabrielli, L. H., Matres, J., & Frick, S. (2018). Opticalmaterialspy: The optical properties of materials. https://github.com/jtambasco/opticalmaterialspy. 

5- Gorgulu, K., & Magden, E. S. (2023). Ultra-broadband integrated optical filters based on adiabatic optimization of coupled waveguides. Journal of Lightwave Technology. 

6- Lu, L., Dao, M., Kumar, P., Ramamurty, U., Karniadakis, G. E., & Suresh, S. (2020). Extraction of mechanical properties of materials through deep learning from instrumented indentation. Proceedings of the National Academy of Sciences, 117(13), 7052-7062.  

7- Rosen, A. S., Iyer, S. M., Ray, D., Yao, Z., Aspuru-Guzik, A., Gagliardi, L., ... & Snurr, R. Q. (2021). Machine learning the quantum-chemical properties of metal–organic frameworks for accelerated materials discovery. Matter, 4(5), 1578-1597. 

8- Bell, C., & Contributors (2016-2021). Thermo: Chemical properties component of Chemical Engineering Design Library (ChEDL). https://github.com/CalebBell/thermo.

9- Bell, C. (2016-2023). Fluids: Fluid dynamics component of Chemical Engineering Design Library (ChEDL). https://github.com/CalebBell/fluids.

10- Rosen, A. S., Fung, V., Huck, P., O’Donnell, C. T., Horton, M. K., Truhlar, D. G., ... & Snurr, R. Q. (2022). High-throughput predictions of metal–organic framework electronic properties: theoretical challenges, graph neural networks, and data exploration. npj Computational Materials, 8(1), 112. 

11- Wiggins, G. (2020). Chemics: A collection of Python functions for performing calculations in the field of chemical engineering. https://github.com/wigging/chemics.

12- Hofemeier, A. D., Limon, T., Muenker, T. M., Wallmeyer, B., Jurado, A., Afshar, M. E., ... & Betz, T. (2021). Global and local tension measurements in biomimetic skeletal muscle tissues reveals early mechanical homeostasis. Elife, 10, e60145. 

13- Singh, S., Valencia-Jaime, I., Pavlic, O., & Romero, A. H. (2018). Elastic, mechanical, and thermodynamic properties of Bi-Sb binaries: Effect of spin-orbit coupling. Physical Review B, 97(5), 054108. 

14- Singh, S., Lang, L., Dovale-Farelo, V., Herath, U., Tavadze, P., Coudert, F. X., & Romero, A. H. (2021). MechElastic: A Python library for analysis of mechanical and elastic properties of bulk and 2D materials. Computer Physics Communications, 267, 108068. 

15- Bernaerts, Y., & Berens, P. (2020). EphysExtraction: Extracting electrophysiological parameters of neurons. https://github.com/berenslab/EphysExtraction.


