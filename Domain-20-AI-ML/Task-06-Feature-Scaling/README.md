# Task 06 - Feature Scaling

This task shows why feature scaling matters in machine learning.

Some features, like attendance percentage, may have much larger numeric ranges than others, like study hours. Scaling puts features on comparable ranges so distance-based models such as KNN work better.

## Scaling Methods

- Standard scaling: centers values around 0 with a standard deviation of 1.
- Min-max scaling: converts values into a 0 to 1 range.

## Run

```bash
python feature_scaling.py
```
