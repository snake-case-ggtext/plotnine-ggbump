---
id: bump_readme_simple
expect: {components: 4, measurable: true}
source: 'README.Rmd "Make a bump chart" (Adapted: ranks precomputed; the README ranks with ties.method = "random", which gives these ranks since no year has ties)'
data:
  country: ["India", "India", "India", "Sweden", "Sweden", "Sweden", "Germany", "Germany", "Germany", "Finland", "Finland", "Finland"]
  year: [2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013]
  month: ["January", "July", "November", "January", "July", "November", "January", "July", "November", "January", "July", "November"]
  rank: [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3]
---

# bump_readme_simple

The default geom_bump: default smooth and line width.

```r
ggplot(df, aes(year, rank, color = country)) +
    geom_bump()
```

```python ggbump
ggplot(df, aes("year", "rank", color="country")) + geom_bump()
```
