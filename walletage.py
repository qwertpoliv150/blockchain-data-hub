"""
WalletAge: Оцени возраст и активность Bitcoin-кошелька.
"""

import requests
from datetime import datetime
import argparse

def fetch_wallet_data(address):
    url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Ошибка получения данных.")
    return response.json()

def fetch_transaction_timestamp(txid):
    url = f"https://api.blockchair.com/bitcoin/raw/transaction/{txid}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    raw_data = response.json()
    try:
        block_time = raw_data["data"][txid]["decoded_raw_transaction"]["time"]
        return datetime.utcfromtimestamp(block_time)
    except Exception:
        return None

def analyze_wallet_age(address):
    print(f"🔍 Анализ кошелька: {address}")
    data = fetch_wallet_data(address)
    transactions = data["data"][address]["transactions"]

    if not transactions:
        print("❗ Нет транзакций у этого адреса.")
        return

    first_tx = transactions[-1]
    last_tx = transactions[0]

    first_time = fetch_transaction_timestamp(first_tx)
    last_time = fetch_transaction_timestamp(last_tx)

    if first_time and last_time:
        wallet_age_days = (datetime.utcnow() - first_time).days
        activity_span = (last_time - first_time).days or 1

        print(f"📆 Возраст кошелька: {wallet_age_days} дней")
        print(f"📊 Период активности: {activity_span} дней")
        print(f"🔁 Количество транзакций: {len(transactions)}")

        tx_per_day = round(len(transactions) / activity_span, 2)
        print(f"⚡ Среднее число транзакций в день: {tx_per_day}")
    else:
        print("⚠️ Не удалось получить временные метки транзакций.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WalletAge — возраст и активность Bitcoin-кошелька.")
    parser.add_argument("address", help="Bitcoin-адрес для анализа")
    args = parser.parse_args()
    analyze_wallet_age(args.address)
