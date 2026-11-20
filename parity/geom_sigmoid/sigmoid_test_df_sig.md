---
id: sigmoid_test_df_sig
expect: {components: 10, measurable: true}
source: 'tests/testthat/test-numeric_inputs.R::"geom_sigmoid"'
data:
  xend: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  y: 1
  x: 1
  yend: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
---

# sigmoid_test_df_sig

Ten sigmoids fanning out from one point, including a zero-width one (x == xend).

```r
ggplot(df, aes(x = x, xend = xend, y = y, yend = yend, color = factor(yend))) +
                       geom_sigmoid(size = 2)
```

```python ggbump
ggplot(
    df, aes(x="x", xend="xend", y="y", yend="yend", color="factor(yend)")
) + geom_sigmoid(size=2)
```
