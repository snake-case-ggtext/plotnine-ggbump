---
id: bump_example_discrete
expect: {components: 8, measurable: true}
source: '?geom_bump example 2'
data:
  country: ["India", "India", "India", "Sweden", "Sweden", "Sweden", "Germany", "Germany", "Germany", "Finland", "Finland", "Finland"]
  year: [2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013]
  month: ["January", "July", "November", "January", "July", "November", "January", "July", "November", "January", "July", "November"]
  rank: [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3]
---

# bump_example_discrete

A character x axis: each (x, country) is its own group, so the lag between x positions comes from setup_data.

```r
ggplot(df, aes(month, rank, color = country)) +
  geom_bump(size = 2)
```

```python ggbump
ggplot(df, aes("month", "rank", color="country")) + geom_bump(size=2)
```
