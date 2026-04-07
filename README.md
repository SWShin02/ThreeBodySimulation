# Three body simulation

JanusEpimetheus.py code is the simulation code. It makes an csv file consist of cartesian coordinates of Saturn, Janus, and Epimetheus in innertial frame. The csv file also contain an angle between innertial frame and rotating frame, which is rotating by mean angular velocity.

JanusEpimetheus2Dplot.py visualize the orbit of Janus & Epimetheus in rotating frame.
JanusEpimetheusRadiiPlot.py visualize the change of orbital radii. You can find that the period of orbit-exchange is dependent on orbital radius difference between Janus & Epimetheus.

LibrationAmplitude.py & RadiusAmplitude.py literally compute the libration amplitude & radius amplitude of the simulation. But, you need to change some parameters carefully. You need to watch the radii graph to decide the parameters. Then, you can find that the libration amplitude ratio & radius amplitude ratio are inverse of mass ratio.

## References

This repository is built upon and inspired by the following academic works:

### Primary References

1. **O'Neill, S., Hay, K., & deMattos, J. (2023).** *Theoretical and computational models for Saturn’s co-orbiting moons, Janus and Epimetheus.* arXiv preprint [arXiv:2312.13442](https://arxiv.org/abs/2312.13442).

---

### BibTeX Citation

If you wish to cite the specific models or data used in this project, please use the following BibTeX entries:

```bibtex
@misc{oneill2023janus,
      title={Theoretical and computational models for Saturn's co-orbiting moons, Janus and Epimetheus}, 
      author={Sean O'Neill and Katrina Hay and Justin deMattos},
      year={2023},
      eprint={2308.06404},
      archivePrefix={arXiv},
      primaryClass={astro-ph.EP},
      url={[https://arxiv.org/abs/2308.06404](https://arxiv.org/abs/2308.06404)}
}
