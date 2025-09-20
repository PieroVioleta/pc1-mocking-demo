from typing import Protocol


class RatesPort(Protocol):
    async def get_rate(self, from_: str, to: str) -> float:
        """Return the FX rate to convert from -> to."""
        ...
