---
id: bump_test_sweden
expect: {components: 1, measurable: true}
source: 'tests/testthat/test-numeric_inputs.R::"Basic usage" 2'
data:
  country: ["India", "India", "India", "Sweden", "Sweden", "Sweden", "Germany", "Germany", "Germany", "Finland", "Finland", "Finland"]
  year: [2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013, 2011, 2012, 2013]
  month: ["January", "July", "November", "January", "July", "November", "January", "July", "November", "January", "July", "November"]
  rank: [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3]
---

# bump_test_sweden

A single curve with no colour grouping.

```r
ggplot(dplyr::filter(df, country == "Sweden"), aes(year, rank)) +
                  geom_point(size = 10) +
                  geom_bump(size = 2)
```

```python ggbump
(
    ggplot(df[df["country"] == "Sweden"], aes("year", "rank"))
    + geom_point(size=10)
    + geom_bump(size=2)
)
```
