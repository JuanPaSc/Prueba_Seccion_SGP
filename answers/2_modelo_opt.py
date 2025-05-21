import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def clean_and_aggregate_money(cell, agg="mean"):
    try:
        numbers = [float(val.replace("$", "")) for val in str(cell).split("$") if val]
        if not numbers:
            return np.nan
        return np.mean(numbers) if agg == "mean" else np.sum(numbers)
    except:
        return np.nan


def clean_currency_column(df, columns):
    for col in columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def convert_yes_to_binary(df, columns):
    for col in columns:
        df[col] = df[col].apply(lambda x: 1 if "YES" in str(x).upper() else 0)
    return df


def load_and_prepare_transaction_data():
    transactions_df = pd.read_csv("./data/raw/transactions_data.csv")
    transactions_df["amount"] = transactions_df["amount"].astype(str)
    transactions_df["amount"] = (
        transactions_df["amount"].str.extract(r"\$?([\d\.]+)").astype(float)
    )
    transactions_df["use_chip"] = pd.to_numeric(
        transactions_df["use_chip"], errors="coerce"
    )
    transactions_df["errors"] = pd.to_numeric(
        transactions_df["errors"], errors="coerce"
    )

    return transactions_df


def load_and_prepare_card_data():

    card_data = pd.read_csv("./data/raw/cards_data.csv")

    card_data["credit_limit"] = card_data["credit_limit"].apply(
        lambda x: clean_and_aggregate_money(x, agg="mean")
    )
    card_data = convert_yes_to_binary(card_data, ["has_chip", "card_on_dark_web"])

    return card_data


def load_and_prepare_client_data():

    client_data = pd.read_csv("./data/raw/users_data.csv")

    client_data = clean_currency_column(
        client_data, ["total_debt", "yearly_income", "per_capita_income"]
    )
    client_data["debt_to_income_ratio"] = (
        client_data["total_debt"] / client_data["yearly_income"]
    )

    return client_data


def feature_engineering(transactions_df, card_data, client_data):
    agg_txns = (
        transactions_df.groupby(["client_id", "mcc"])
        .agg(
            total_spent=("amount", "sum"),
            num_txns=("amount", "count"),
            avg_txn_amount=("amount", "mean"),
        )
        .reset_index()
    )

    card_features = (
        card_data.groupby("client_id")
        .agg(
            {
                "credit_limit": ["mean", "sum"],
                "num_cards_issued": "sum",
                "has_chip": "mean",
                "card_on_dark_web": "max",
            }
        )
        .reset_index()
    )
    card_features.columns = [
        "client_id",
        "avg_credit_limit",
        "total_credit_limit",
        "total_cards_issued",
        "pct_chip_cards",
        "any_dark_web_card",
    ]

    clients_with_cards = pd.merge(
        client_data, card_features, left_on="id", right_on="client_id", how="left"
    )
    final_data = pd.merge(
        agg_txns, clients_with_cards, left_on="client_id", right_on="id", how="left"
    )

    return final_data


def train_model(final_data):
    features = [
        "current_age",
        "retirement_age",
        "birth_year",
        "birth_month",
        "per_capita_income",
        "yearly_income",
        "total_debt",
        "credit_score",
        "num_credit_cards",
        "debt_to_income_ratio",
        "avg_credit_limit",
        "total_credit_limit",
        "total_cards_issued",
        "pct_chip_cards",
        "any_dark_web_card",
        "mcc",
    ]

    model_data = final_data[features + ["total_spent"]].copy()
    model_data.dropna(inplace=True)
    model_data["mcc"] = model_data["mcc"].astype("category")

    X = model_data[features]
    y = model_data["total_spent"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LGBMRegressor(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE del modelo: {rmse:.2f}")

    r2 = r2_score(y_test, y_pred)
    print(f"R² del modelo: {r2:.2f}")

    rmse_relative = rmse / y_test.mean()
    print(f"RMSE relativo: {rmse_relative:.2%}")

    return model, final_data


# def plot_mcc_behavior(transactions_df, sample_size=5):
#     sample_clients = (
#         transactions_df["client_id"]
#         .drop_duplicates()
#         .sample(sample_size, random_state=1)
#     )
#     transactions_df["mcc"] = transactions_df["mcc"].astype(str)

#     plt.figure(figsize=(12, 6))
#     sns.lineplot(
#         data=transactions_df[transactions_df["client_id"].isin(sample_clients)],
#         x="mcc",
#         y="amount",
#         hue="client_id",
#         marker="o",
#     )
#     plt.title("Comportamiento de gasto por cliente y categoría MCC")
#     plt.xlabel("Categoría MCC")
#     plt.ylabel("Total gastado")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()


# def plot_predictions_vs_actual(final_data, model):
#     data = final_data.copy()
#     data.dropna(inplace=True)
#     data["mcc"] = data["mcc"].astype("category")

#     # Preparar features y predicciones
#     features = [
#         "current_age",
#         "retirement_age",
#         "birth_year",
#         "birth_month",
#         "per_capita_income",
#         "yearly_income",
#         "total_debt",
#         "credit_score",
#         "num_credit_cards",
#         "debt_to_income_ratio",
#         "avg_credit_limit",
#         "total_credit_limit",
#         "total_cards_issued",
#         "pct_chip_cards",
#         "any_dark_web_card",
#         "mcc",
#     ]
#     X = data[features]
#     y = data["total_spent"]
#     y_pred = model.predict(X)

#     # Agregar al DataFrame
#     data["prediction"] = y_pred

#     # Mostrar solo las top categorías más frecuentes para legibilidad
#     top_mcc = data["mcc"].value_counts().nlargest(10).index
#     data = data[data["mcc"].isin(top_mcc)]

#     plt.figure(figsize=(14, 6))
#     sns.boxplot(data=data, x="mcc", y="total_spent", color="skyblue", width=0.5)
#     sns.stripplot(
#         data=data, x="mcc", y="prediction", color="red", alpha=0.3, jitter=0.2
#     )
#     plt.title("Distribución real del gasto y predicciones por categoría MCC")
#     plt.xlabel("Categoría MCC")
#     plt.ylabel("Total gastado")
#     plt.xticks(rotation=45)
#     plt.legend(
#         handles=[
#             plt.Line2D(
#                 [0],
#                 [0],
#                 marker="o",
#                 color="w",
#                 label="Predicción",
#                 markerfacecolor="red",
#                 markersize=8,
#             ),
#             plt.Rectangle(
#                 (0, 0), 1, 1, fc="skyblue", edgecolor="none", label="Valor real"
#             ),
#         ]
#     )
#     plt.tight_layout()
#     plt.show()


if __name__ == "__main__":
    transactions_df = load_and_prepare_transaction_data()
    card_data = load_and_prepare_card_data()
    client_data = load_and_prepare_client_data()
    final_data = feature_engineering(transactions_df, card_data, client_data)
    model, final_data = train_model(final_data)
    # plot_mcc_behavior(transactions_df)
    # plot_predictions_vs_actual(final_data, model)
