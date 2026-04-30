# Python Data Processing Lesson

# 1. Why Python is used for data work
# Python is easy to read and has libraries for tables, numbers, charts, and models.
# People use Python to clean data, explore it, find patterns, and make predictions.

# 2. Load data with pandas
import pandas as pd

data = {
    "age": [22, 25, 30, 28, 35],
    "score": [88, 92, 95, 90, 85]
}
df = pd.DataFrame(data)
print("Data table")
print(df)
print("Mean age:", df["age"].mean())
print("Max score:", df["score"].max())

# 3. Clean data by filling missing values
clean_df = pd.DataFrame({
    "value": [10, None, 20, 30, None]
})
clean_df["value"] = clean_df["value"].fillna(clean_df["value"].mean())
print("Cleaned data")
print(clean_df)

# 4. Find patterns with grouping
pattern_df = pd.DataFrame({
    "group": ["A", "A", "B", "B", "A"],
    "sales": [100, 120, 80, 90, 130]
})
print("Average sales by group")
print(pattern_df.groupby("group")["sales"].mean())

# 5. Basic machine learning example
from sklearn.linear_model import LinearRegression

ml_df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5],
    "score": [50, 60, 70, 80, 90]
})
X = ml_df[["hours"]]
y = ml_df["score"]
model = LinearRegression()
model.fit(X, y)
print("Prediction for 6 hours:", model.predict([[6]])[0])

# 6. How these fields connect
# - Data analytics: use Python to collect, clean, and summarize data.
# - Data analysis: inspect numbers and charts to understand data.
# - Data mining: search data for hidden patterns or groups.
# - Machine learning: train models that learn from data and make predictions.

# 7. Useful libraries
# pandas - work with tables and data frames
# numpy - work with numeric arrays
# matplotlib - make charts
# scikit-learn - make machine learning models
