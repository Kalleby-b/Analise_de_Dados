import pandas as pd
df = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\total_data.csv")
df_abril2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\abril2018.csv")
df_abril2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\abril2019.csv")
df_abril2020 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\abril2020.csv")
df_agosto2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\agosto2019.csv")
df_agosto2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\agosto2018.csv")
df_dezembro2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\dezembro2018.csv")
df_dezembro2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\dezembro2019.csv")
df_fevereiro2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\fevereiro2019.csv")
df_fevereiro2020 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\fevereiro2020.csv")
df_janeiro2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\janeiro2019.csv")
df_janeiro2020 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\janeiro2020.csv")
df_julho2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\julho2018.csv")
df_julho2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\julho2019.csv")
df_junho2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\junho2019.csv")
df_maio2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\maio2018.csv")
df_maio2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\maio2019.csv")
df_maio2020 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\maio2020.csv")
df_maro2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\maro2019.csv")
df_maro2020 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\maro2020.csv")
df_novembro2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\novembro2018.csv")
df_novembro2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\novembro2019.csv")
df_outubro2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\outubro2018.csv")
df_outubro2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\outubro2019.csv")
df_setembro2018 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\setembro2018.csv")
df_setembro2019 = pd.read_csv("C:\\Users\\user\\Downloads\\archive (8)\\setembro2019.csv")

grup = df.groupby("id")
df_n_repete = grup.first()

lista = [df ,df_abril2018 ,df_abril2019 ,df_abril2020 ,df_agosto2019 ,df_agosto2018 ,df_dezembro2018,df_dezembro2019,
df_fevereiro2019,df_fevereiro2020,df_janeiro2019,df_janeiro2020,df_julho2018,df_julho2019,df_junho2019 ,df_maio2018 ,
df_maio2019 ,df_maio2020 ,df_maro2019 ,df_maro2020 ,df_novembro2018,df_novembro2019 ,df_outubro2018,df_outubro2019,
df_setembro2018,df_setembro2019 ]

a = pd.DataFrame(df_n_repete[df_n_repete["neighbourhood_cleansed"].isnull()])
b = a["id"]
print(len(b))
for i in range(len(lista)):
    c = lista[i].loc[lista[i]["id"].isin(b)]
    print("tabela {}".format(i))
    if len(c[c["neighbourhood_cleansed"].notnull()])>0:
        print(c.loc[c["neighbourhood_cleansed"].notnull() , "id" ], "e neighbourhood_cleansed: ", c.loc[c["neighbourhood_cleansed"].notnull(), "neighbourhood_cleansed"])
    elif len(c[c["neighbourhood_cleansed"].notnull()]) == 0:
        print("id presente, mas neighbourhood_cleansed ausentes")
    else:
        print("sem os ids")

