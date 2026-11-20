---
id: bump_readme_pimped
expect: {components: 4, measurable: true}
source: 'README.Rmd "Pimp the bump chart!" (Adapted: no cowplot theme or theme() call, which plotparity pins; wes_palette("GrandBudapest1") written out; dplyr::filter namespaced)'
data:
  country: ["India", "India", "India", "Sweden", "Sweden", "Sweden", "Germany", "Germany", "Germany", "Finland", "Finland", "Finland"]
  year: [2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013]
  month: ["January", "July", "November", "January", "July", "November", "January", "July", "November", "January", "July", "November"]
  rank: [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3]
---

# bump_readme_pimped

Bump curves with labels at both ends, a reversed y scale, manual colours and explicit smooth.

```r
ggplot(df, aes(year, rank, color = country)) +
  geom_point(size = 7) +
  geom_text(data = df %>% dplyr::filter(year == min(year)),
            aes(x = year - .1, label = country), size = 5, hjust = 1) +
  geom_text(data = df %>% dplyr::filter(year == max(year)),
            aes(x = year + .1, label = country), size = 5, hjust = 0) +
  geom_bump(size = 2, smooth = 8) +
  scale_x_continuous(limits = c(2010.6, 2013.4),
                     breaks = seq(2011, 2013, 1)) +
  labs(y = "RANK",
       x = NULL) +
  scale_y_reverse() +
  scale_color_manual(values = c("#F1BB7B", "#FD6467", "#5B1A18", "#D67236"))
```

```python ggbump
(
    ggplot(df, aes("year", "rank", color="country"))
    + geom_point(size=7)
    + geom_text(
        data=df[df["year"] == df["year"].min()],
        mapping=aes(x="year - .1", label="country"),
        size=5 * 72.27 / 25.4,
        ha="right",
    )
    + geom_text(
        data=df[df["year"] == df["year"].max()],
        mapping=aes(x="year + .1", label="country"),
        size=5 * 72.27 / 25.4,
        ha="left",
    )
    + geom_bump(size=2, smooth=8)
    + scale_x_continuous(limits=(2010.6, 2013.4), breaks=[2011, 2012, 2013])
    + labs(y="RANK", x=None)
    + scale_y_reverse()
    + scale_color_manual(values=["#F1BB7B", "#FD6467", "#5B1A18", "#D67236"])
)
```
