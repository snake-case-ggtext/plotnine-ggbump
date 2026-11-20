---
id: bump_example_continuous
expect: {components: 4, measurable: true}
source: '?geom_bump example 1 (also tests/testthat/test-numeric_inputs.R::"Basic usage" 1)'
data:
  country: ["India", "India", "India", "Sweden", "Sweden", "Sweden", "Germany", "Germany", "Germany", "Finland", "Finland", "Finland"]
  year: [2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013]
  month: ["January", "July", "November", "January", "July", "November", "January", "July", "November", "January", "July", "November"]
  rank: [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3]
---

# bump_example_continuous

Four bump curves over a continuous x axis, drawn over large points.

```r
ggplot(df, aes(year, rank, color = country)) +
  geom_point(size = 10) +
  geom_bump(size = 2)
```

```python ggbump
(
    ggplot(df, aes("year", "rank", color="country"))
    + geom_point(size=10)
    + geom_bump(size=2)
)
```
