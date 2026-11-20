---
id: bump_test_discrete_points
expect: {components: 8, measurable: true}
source: 'tests/testthat/test-numeric_inputs.R::"Discrete x axis"'
data:
  country: ["India", "India", "India", "Sweden", "Sweden", "Sweden", "Germany", "Germany", "Germany", "Finland", "Finland", "Finland"]
  year: [2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013]
  month: ["January", "July", "November", "January", "July", "November", "January", "July", "November", "January", "July", "November"]
  rank: [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3]
---

# bump_test_discrete_points

A character x axis with points drawn under the curves.

```r
ggplot(df, aes(month, rank, color = country)) +
                  geom_point(size = 10) +
                  geom_bump(size = 2)
```

```python ggbump
(
    ggplot(df, aes("month", "rank", color="country"))
    + geom_point(size=10)
    + geom_bump(size=2)
)
```
