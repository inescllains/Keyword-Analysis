import pandas as pd

df = pd.read_excel("Newspaper articles spreadsheets/Noticias 2019 Cabo DelgadoIL.xlsx")


# create a function to check if the second word in the text column is "Publicidade"
def check_publicidade(row):
    if pd.notna(row["Text"]):
        words = row["Text"].split()
        if len(words) >= 2:
            first_word = words[0]
            second_word = words[1]
            if (
                first_word == "publicidade"
                or first_word == "PUBLICIDADE"
                or first_word == "NECROLOGIA"
                or first_word == "Desporto"
                or first_word == "necrologia"
            ):
                row["Relevance"] = 0
                row["Confidence"] = 10
            elif (
                second_word == "publicidade"
                or second_word == "PUBLICIDADE"
                or second_word == "NECROLOGIA"
                or second_word == "Classificados"
                or second_word == "classificados"
            ):
                row["Relevance"] = 0
                row["Confidence"] = 10
    print(row["Relevance"])
    return row


df = df.apply(check_publicidade, axis=1)

print(df["Relevance"])

print(df["Relevance"].value_counts())

print(df.columns)


df.to_excel(
    "Newspaper articles spreadsheets/Noticias 2019 Cabo DelgadoIL.xlsx", index=False
)
