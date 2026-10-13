import pandas as pd 
df = pd.read_csv("data/students.csv")
# print(df.tail(3))

# print(df.shape) 
# print(df.columns.tolist()) 
# print(df.dtypes)


# df.info()

# print(df["name"].head(3)) 
# print(df[["name", "maths"]].head(3)) 
# print(df["maths"].mean())

# print(df.loc[2, "name"]) 
# print(df.loc[0:2, ["name", "python"]]) 
# print(df.iloc[0:3, 1:3])


# print(df[df["maths"] > 80][["name", "maths"]]) 
# print(df[(df["department"] == "CSE") & (df["python"] >= 90)][["name", "python"]])
# print(df[df["city"].isin(["Chennai", "Bangalore"])][["name", "city"]])

# print (df.sort_values("maths", ascending =True)[["name", "maths"]].head(3))

# df["passed_maths"] = df["maths"] >= 60
# df["maths_out_of_20"] = (df["maths"]/5).round(1)
# print(df[["name", "maths", "passed_maths", "maths_out_of_20"]].tail(5))


print(df["city"].value_counts())
print(df.groupby("department")["maths"].mean().round(1))