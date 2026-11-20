# Port plan: ggbump → ggbump

## Upstream

| | |
|---|---|
| R package | ggbump 0.1.99999 (development version; CRAN has 0.1.0) |
| Source | https://github.com/davidsjoberg/ggbump @ fe6d5c7a974d4ae421b295cf81974394df481111 |
| License | MIT — decision: the port is MIT and translates the R code; upstream copyright kept in `LICENSE` |
| Depends/Imports | ggplot2, dplyr, purrr, tidyr, magrittr |
| ggplot2 (reference env) | 4.0.4 |
| plotnine | 0.15.9 (sources cache @ v0.15.9) |
| plotparity adapter | `ggbump` on branch `adapter-ggbump` |

## Exports

Status: `todo`, `case` (parity case written), `impl` (implemented), `parity` (passes plotparity),
`skip` (with the reason).

| R export | Kind | plotnine target | Status | Notes |
|---|---|---|---|---|
| `geom_bump()` | layer function (stat `StatBump`, geom `"line"`) | `geom_bump(geom_line)`, default stat `"bump"` | todo | `smooth=8`, `direction="x"` |
| `StatBump` | Stat | `stat_bump(stat)`, default geom `"line"` | todo | lag per non-position group in `setup_data`, so discrete x works |
| `geom_sigmoid()` | layer function (stat `StatSigmoid`, geom `"line"`) | `geom_sigmoid(geom_line)`, default stat `"sigmoid"` | todo | |
| `StatSigmoid` | Stat | `stat_sigmoid(stat)` | todo | R's `setup_data` prints the data; the port doesn't |
| `sigmoid()` | helper | `ggbump.sigmoid()` → `pd.DataFrame` | todo | defaults `smooth=5, n=100` |
| `rank_sigmoid()` | helper | `ggbump.rank_sigmoid()` → `pd.DataFrame` | todo | default `smooth=8` |
| `%>%` | re-export | — | skip | magrittr pipe; no Python counterpart |

## R tests and examples

| R source | Becomes | Status |
|---|---|---|
| `test-numeric_inputs.R` "Basic usage" (3 builds) | `parity/geom_bump/{example_continuous,test_sweden,test_sweden_smooth10}.md` + `tests/test_numeric_inputs.py` | todo |
| `test-numeric_inputs.R` "Basic usage" `expect_warning(aes(smooth = 10))` | `tests/test_numeric_inputs.py` | todo |
| `test-numeric_inputs.R` "Discrete x axis" | `parity/geom_bump/test_discrete_points.md` + pytest | todo |
| `test-numeric_inputs.R` "geom_sigmoid" | `parity/geom_sigmoid/test_df_sig.md` + pytest | todo |
| `?geom_bump` examples 1, 2 | `parity/geom_bump/{example_continuous,example_discrete}.md` | todo |
| `?geom_sigmoid` example | `parity/geom_sigmoid/example.md` | todo |
| README tutorial (simple, factor seasons) | `parity/geom_bump/{readme_simple,readme_factor_season}.md` (no cowplot/wesanderson) | todo |
| `?sigmoid`, `?rank_sigmoid` | `tests/test_helpers.py`, values from R | todo |
| (added) `direction = "y"` | `parity/geom_sigmoid/direction_y.md`, `parity/geom_bump/direction_y.md` | todo |

## Open questions

- Line widths: R `size`/`linewidth` is mm × `.pt`; plotnine's `geom_line` scales by `SIZE_FACTOR`.
  Settle this from parity results and record it in `docs/differences.md`.
