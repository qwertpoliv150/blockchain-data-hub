# WalletAge

**WalletAge** — это утилита на Python для анализа возраста и активности криптовалютных кошельков (Bitcoin).

## Особенности

- Получает дату первой и последней транзакции
- Оценивает возраст кошелька
- Вычисляет период активности
- Подсчитывает среднее количество транзакций в день

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python walletage.py <bitcoin_address>
```

Пример:

```bash
python walletage.py 1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY
```

## Примечание

- Используется публичное API Blockchair (может потребоваться API-ключ при массовом использовании)
- Поддерживается только Bitcoin в текущей версии

## Лицензия

MIT License
