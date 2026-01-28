import requests

def get_exchange_rate(from_currency, to_currency):
    """
    This function returns the exchange rate of from_currency to to_currency taken from exchangerate API

    :param from_currency: currency to convert from
    :param to_currency: currency to convert to
    :return: convertion rate
    """
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return data['rates'].get(to_currency.upper())

    except requests.RequestException:
        return None


def convert_currency(amount, from_currency, to_currency):
    """
    This function returns the converted amount of two currencies

    :param amount: amount to convert
    :param from_currency: exchange currency to convert from
    :param to_currency: exchange currency to convert to
    :return: converted amount
    """
    rate = get_exchange_rate(from_currency, to_currency)

    if rate is None:
        return None

    return amount * rate

