import pandas as pd

data = {
    "Age": [20, 22, 23, 21, 24, 100, 22, 23], 
    "Height": [160, 165, 170, 158, 172, 168, 169, None], 
    "Weight": [55, 60, 58, 57, 65, 300, 59, 60] 
}

df = pd.DataFrame(data)

print("Missing Data in Each Column:")
print(df.isnull().sum())
print()

def detect_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = column[(column < lower_bound) | (column > upper_bound)]
    return outliers

print("Outliers in Each Column:")
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    out = detect_outliers(df[col])
    print(f"{col}: {list(out)}")
