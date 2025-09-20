from .ports import RatesPort


class ConversionService:
    def __init__(self, rates: RatesPort):
        self.rates = rates

    async def convert(self, amount: float, from_: str, to: str) -> dict:
        if amount <= 0:
            raise ValueError("amount must be > 0")
        if from_ == to:
            raise ValueError("from and to must differ")
        rate = await self.rates.get_rate(from_, to)
        converted = round(amount * rate, 2)
        return {
            "amount": amount,
            "from": from_,
            "to": to,
            "rate": rate,
            "converted": converted,
        }
