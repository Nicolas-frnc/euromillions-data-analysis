import pandas as pd
import glob
import os

folder = "data_set"
all_files = glob.glob(os.path.join(folder, "*.csv"))

df_list = []
for file in all_files:
    df = pd.read_csv(file, sep=";", encoding="latin1", header=None)
    df_list.append(df)

df_all = pd.concat(df_list)
df_all.to_csv("mix1.csv", index=False, encoding="utf-8")

print("ok pour les fichiers dans le dossier :", folder )

