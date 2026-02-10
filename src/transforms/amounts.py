import re 
from decimal import Decimal, InvalidOperation


CURRENCY_SYMBOLS = {"$": "USD", "€": "EUR", "£": "GBP", "¥": "JPY", "₹": "INR"} 

# This function fixes string amounts such as "$1,000.00", "1000,00", "$1000" to "1000.00" and identifies the currency as "USD". It also handles cases like "1,000" (without a currency symbol) and assumes a default currency if none is found.

def _clean_amount_str(amount_str: str):
    amount_str = amount_str.strip() 
    currency = None 
    
    for sym, currency in CURRENCY_SYMBOLS.items():
        if sym in amount_str:
            currency = currency 
            amount_str = amount_str.replace(sym, "")
    amount_str = amount_str.replace(",", "")  # Remove commas from the amount string
    amount_str = re.sub(r'[^\d\.\-]', '', amount_str) # Remove non-numeric characters except for '.' and '-'.
    return amount_str, currency
    
def parse_amount(value, default_currency: str = "NGN") -> tuple[float | None, str]:
    currency = default_currency
    if value is None:
        return None, currency
    if isinstance(value, (int, float)):
        if isinstance(value, int) and value >=1000:
            return float(Decimal(value) / Decimal(100)), currency
        return float(value), currency
    if isinstance(value, str):
        amt_str, detected_currency = _clean_amount_str(value)
        if detected_currency:
            currency = detected_currency
        if not amt_str:
            return None, currency
        try: 
            d = Decimal(amt_str) 
        except InvalidOperation:  # If the cleaned amount string is not a valid decimal, return None
            return None, currency
        if re.fullmatch(r"\d{4,}", amt_str): # If the cleaned amount is a long integer, assume it's in minor units
            d = d / Decimal(100)  # Convert from minor units to major units
            return float(d), currency
    return None, currency    