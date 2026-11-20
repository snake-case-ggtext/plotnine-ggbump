---
id: bump_direction_y
expect: {components: 4, measurable: true}
source: 'added: the direction argument of ?geom_bump (Adapted: two time points per line, because R orders each line by x; see docs/differences.md)'
data:
  country: ["India", "India", "Sweden", "Sweden", "Germany", "Germany", "Finland", "Finland"]
  year: [2011, 2013, 2011, 2013, 2011, 2013, 2011, 2013]
  rank: [4, 2, 3, 4, 2, 1, 1, 3]
---

# bump_direction_y

A vertical bump chart: time on y, rank on x, direction = "y". Each line has two points because R orders a line by x, which matches time order only when the line moves one way.

```r
ggplot(df, aes(rank, year, color = country)) +
  geom_bump(size = 2, direction = "y")
```

```python ggbump
ggplot(df, aes("rank", "year", color="country")) + geom_bump(size=2, direction="y")
```
