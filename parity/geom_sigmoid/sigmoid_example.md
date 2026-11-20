---
id: sigmoid_example
expect: {components: 6, measurable: true}
source: '?geom_sigmoid example'
data:
  x: [1, 2, 3, 4, 5, 6]
  y: [5, 6, 7, 8, 9, 10]
  xend: 7
  yend: [-3, -2, -1, 0, 1, 2]
---

# sigmoid_example

Six sigmoid curves from (x, y) to (xend, yend), one group per row.

```r
ggplot(df, aes(x = x, xend = xend, y = y, yend = yend, color = factor(x))) +
  geom_sigmoid()
```

```python ggbump
(
    ggplot(df, aes(x="x", xend="xend", y="y", yend="yend", color="factor(x)"))
    + geom_sigmoid()
)
```
