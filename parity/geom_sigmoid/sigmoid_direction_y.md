---
id: sigmoid_direction_y
expect: {components: 6, measurable: true}
source: 'added: the direction argument of ?geom_sigmoid'
data:
  x: [1, 2, 3, 4, 5, 6]
  y: [5, 6, 7, 8, 9, 10]
  xend: 7
  yend: [-3, -2, -1, 0, 1, 2]
---

# sigmoid_direction_y

direction = "y": each sigmoid is smoothed along y.

```r
ggplot(df, aes(x = x, xend = xend, y = y, yend = yend, color = factor(x))) +
  geom_sigmoid(direction = "y", smooth = 6)
```

```python ggbump
ggplot(
    df, aes(x="x", xend="xend", y="y", yend="yend", color="factor(x)")
) + geom_sigmoid(direction="y", smooth=6)
```
