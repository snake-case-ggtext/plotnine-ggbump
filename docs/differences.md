# Differences from R ggbump

ggbump follows R ggbump closely but uses plotnine's conventions where they clash. R spellings still
work as aliases. Each row here also appears as an `Adapted:` note in the parity case or test it affects.

| R ggbump | ggbump | Why |
|---|---|---|
| `geom_bump(size = 2)` / `linewidth = 2`: R draws 2 × 72.27/25.4 × 72/96 = 4.27 pt | `size=2` draws 2 × √π = 3.54 pt, as plotnine's `geom_line` does; `linewidth` is an alias | consistent with the rest of plotnine; the parity check `curve_width` is advisory and reports this |
| `geom_bump(geom = "point")` | `stat_bump(geom="point")` | a plotnine geom can't change its own geom |
| `show.legend`, `na.rm` | `show_legend`, `na_rm` | Python names |
| `StatSigmoid` prints its data on every build | silent | a debugging leftover in R |
| `StatBump` repeats each continuous-x curve once per input row (600 rows for 3 points) | each curve once (200 rows) | the copies overlap exactly; nothing visible changes |
| the `%>%` re-export | not provided | no Python counterpart |
| `aes(smooth = 10)` warns "Ignoring unknown aesthetics: smooth" (ggplot2) | the same warning, from `geom_bump`/`geom_sigmoid` | plotnine ignores unknown aesthetics silently |
