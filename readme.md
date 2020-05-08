# Circadian Clock Modulators

Analyzing circadian clock modulators.

## References

Figshare datasets by Tamai et al are stored in the [`data/tamai-screen`](data/tamai-screen) directory.
They were downloaded from figshare at the locations listed below, where they are available under a [CC0 License](https://creativecommons.org/publicdomain/zero/1.0/).

<!-- generated using:
manubot cite --format=markdown --render \
  doi:10.15252/emmm.201708724 \
  doi:10.6084/m9.figshare.11608485.v2 \
  doi:10.6084/m9.figshare.11626014.v2
-->

1. **Identification of circadian clock modulators from existing drugs**  
T Katherine Tamai, Yusuke Nakane, Wataru Ota, Akane Kobayashi, Masateru Ishiguro, Naoya Kadofusa, Keisuke Ikegami, Kazuhiro Yagita, Yasufumi Shigeyoshi, Masaki Sudo, … Takashi Yoshimura  
*EMBO Molecular Medicine* (2018-04-17) <https://doi.org/ggq6hh>  
DOI: [10.15252/emmm.201708724](https://doi.org/10.15252/emmm.201708724) · PMID: [29666146](https://www.ncbi.nlm.nih.gov/pubmed/29666146) · PMCID: [PMC5938619](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5938619)

2. **FDA\_Tamai et al\_Identification of circadian clock modulators from existing drugs**  
Kathy Tamai, Yusuke Nakane, Takashi Yoshimura  
*figshare* (2020) <https://doi.org/ggq6hp>  
DOI: [10.6084/m9.figshare.11608485.v2](https://doi.org/10.6084/m9.figshare.11608485.v2)

3. **IDC\_Tamai et al\_Identification of circadian clock modulators from existing drugs**  
Kathy Tamai, Takashi Yoshimura, Yusuke Nakane  
*figshare* (2020) <https://doi.org/ggq6hq>  
DOI: [10.6084/m9.figshare.11626014.v2](https://doi.org/10.6084/m9.figshare.11626014.v2)

## Environment

This repository uses Pipenv to manage its environment.
See [this post](https://towardsdatascience.com/how-to-use-pipenv-with-jupyter-and-vscode-ae0e970df486) for information on using Pipenv with notebooks and vscode.

Here are some useful commands to run from the repository's root directory:

```shell
# if conda is installed, it might help to deactivate a conda env first
conda deactivate

# install the virtual environment
pipenv install

# activate a terminal shell with this environment
pipenv shell

# start the jupyter notebook
pipenv run jupyter notebook

# add the "pandas" package to the environment (already done)
pipenv install pandas
```

## License

All original work in this repository is released under a [CC0 License](https://creativecommons.org/publicdomain/zero/1.0/).
All code in this repository is also released under a BSD-2-Clause Plus Patent License as provided in [`license-bsd.md`](license-bsd.md).
