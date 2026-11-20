---
id: bump_readme_factor_season
expect: {components: 20, measurable: true}
source: 'README.Rmd "geom_bump with factors" (Adapted: no cowplot theme; the factor is built inline)'
data:
  season: ["Spring", "Pre-season", "Summer", "Season finale", "Autumn", "Winter", "Spring", "Pre-season", "Summer", "Season finale", "Autumn", "Winter", "Spring", "Pre-season", "Summer", "Season finale", "Autumn", "Winter", "Spring", "Pre-season", "Summer", "Season finale", "Autumn", "Winter"]
  rank: [1, 3, 4, 2, 1, 4, 2, 4, 1, 3, 2, 3, 4, 1, 2, 4, 4, 1, 3, 2, 3, 1, 3, 2]
  player: ["David", "David", "David", "David", "David", "David", "Anna", "Anna", "Anna", "Anna", "Anna", "Anna", "Franz", "Franz", "Franz", "Franz", "Franz", "Franz", "Ika", "Ika", "Ika", "Ika", "Ika", "Ika"]
---

# bump_readme_factor_season

An ordered factor x axis, a large smooth, no legend for the curves, and shaped points.

```r
df$season <- factor(df$season, levels = unique(df$season))
ggplot(df, aes(season, rank, color = player)) +
  geom_bump(size = 2, smooth = 20, show.legend = F) +
  geom_point(size = 5, aes(shape = player))
```

```python ggbump
df["season"] = pd.Categorical(df["season"], categories=df["season"].unique())
(
    ggplot(df, aes("season", "rank", color="player"))
    + geom_bump(size=2, smooth=20, show_legend=False)
    + geom_point(aes(shape="player"), size=5)
)
```
