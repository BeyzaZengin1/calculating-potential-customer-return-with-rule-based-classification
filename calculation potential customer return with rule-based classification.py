import pandas as pd
df = pd.read_csv("persona.csv")

df.info()
df.head()
df.describe().T

df["SOURCE"].nunique()
df["SOURCE"].value_counts()
df["PRICE"].nunique()
df["PRICE"].value_counts()
df["COUNTRY"].value_counts()

df.groupby("COUNTRY").agg({"PRICE": "sum"})
df.groupby("SOURCE").value_counts()
df.groupby("COUNTRY").agg({"PRICE": "mean"})
df.groupby("SOURCE").agg({"PRICE": "mean"})
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})
df.groupby(["COUNTRY", "SOURCE", "AGE", "SEX"]).agg({"PRICE": "mean"}).head()

agg_df = df.groupby(["COUNTRY", "SOURCE", "AGE", "SEX"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df = agg_df.reset_index()

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
labels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]
agg_df["age_cat"]=pd.cut(agg_df["AGE"],bins,labels=labels)
agg_df.head()
agg_df.columns

for row in agg_df.values:
    print(row)

[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]


agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()


agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))

agg_df["customers_level_based"].value_counts()


agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})


agg_df = agg_df.reset_index()
agg_df.head()


agg_df["customers_level_based"].value_counts()
agg_df.head()


agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]


new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
