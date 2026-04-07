# Three body simulation

JanusEpimetheus.py code is the simulation code. It makes an csv file consist of cartesian coordinates of Saturn, Janus, and Epimetheus in innertial frame. The csv file also contain an angle between innertial frame and rotating frame, which is rotating by mean angular velocity.

JanusEpimetheus2Dplot.py visualize the orbit of Janus & Epimetheus in rotating frame.
JanusEpimetheusRadiiPlot.py visualize the change of orbital radii. You can find that the period of orbit-exchange is dependent on orbital radius difference between Janus & Epimetheus.

LibrationAmplitude.py & RadiusAmplitude.py literally compute the libration amplitude & radius amplitude of the simulation. But, you need to change some parameters carefully. You need to watch the radii graph to decide the parameters. Then, you can find that the libration amplitude ratio & radius amplitude ratio are inverse of mass ratio.

## References

This repository is built upon and inspired by the following academic works:

### Primary Publication
* **O'Neill, S., Hay, K., & deMattos, J. (2024).** *Theoretical and computational models for Saturn’s co-orbiting moons, Janus and Epimetheus.* Celestial Mechanics and Dynamical Astronomy, 136(27).  
  [DOI: 10.1007/s10569-024-10200-8](https://doi.org/10.1007/s10569-024-10200-8)

### BibTeX Citation
```bibtex
@article{ONeill2024,
  author = {O'Neill, Sean and Hay, Katrina and deMattos, Justin},
  title = {Theoretical and computational models for Saturn’s co-orbiting moons, Janus and Epimetheus},
  journal = {Celestial Mechanics and Dynamical Astronomy},
  year = {2024},
  volume = {136},
  number = {27},
  doi = {10.1007/s10569-024-10200-8},
  url = {[https://doi.org/10.1007/s10569-024-10200-8](https://doi.org/10.1007/s10569-024-10200-8)}
}
