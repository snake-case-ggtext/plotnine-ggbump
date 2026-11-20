---
id: bump_direction_y
expect: {components: 4, measurable: true}
source: 'added: the direction argument of ?geom_bump'
data:
  country: ["India", "India", "India", "Sweden", "Sweden", "Sweden", "Germany", "Germany", "Germany", "Finland", "Finland", "Finland"]
  year: [2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013]
  month: ["January", "July", "November", "January", "July", "November", "January", "July", "November", "January", "July", "November"]
  rank: [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3]
---

# bump_direction_y

direction = "y": the curve is smoothed along y instead of x.

```r
ggplot(df, aes(rank, year, color = country)) +
  geom_bump(size = 2, direction = "y")
```

```python ggbump
ggplot(df, aes("rank", "year", color="country")) + geom_bump(size=2, direction="y")
```
