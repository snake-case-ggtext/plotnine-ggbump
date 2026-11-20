# ggbump

A Python port of the R package [ggbump](https://github.com/davidsjoberg/ggbump) for
[plotnine](https://plotnine.org).

```python
from plotnine import ggplot, aes
import ggbump
```

## Development

Everything runs in one [pixi](https://pixi.sh) environment with Python, R and the tools:

```bash
pixi install
pixi run install-r-upstream   # the R package, from its local clone (skip if conda-forge has it)
pixi run prek install         # git hooks
pixi run test                 # pytest
pixi run lint                 # ruff + pyrefly
pixi run parity run           # compare with R through plotparity
pixi run gallery              # regenerate docs/images and docs/gallery.md
```

See [docs/differences.md](docs/differences.md) for where this port deliberately differs from R.
