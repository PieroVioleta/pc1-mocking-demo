from typing import Dict, Tuple

from .ports import RatesPort


class FakeRatesAdapter(RatesPort):
    def __init__(self, table: Dict[Tuple[str, str], float] | None = None):
        self.table = table or {
            ("USD", "PEN"): 3.72,
            ("EUR", "PEN"): 4.05,
            ("PEN", "USD"): 0.27,
        }

    async def get_rate(self, from_: str, to: str) -> float:
        try:
            return self.table[(from_, to)]
        except KeyError as exc:
            raise LookupError("currency pair not supported") from exc


async def get_rate(self, from_: str, to: str) -> float:
    try:
        return self.table[(from_, to)]
    except KeyError as exc:
        raise LookupError("currency pair not supported") from exc
