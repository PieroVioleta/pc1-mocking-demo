from unittest.mock import AsyncMock

import pytest

from app.domain import ConversionService


@pytest.mark.asyncio
async def test_convert_ok():
    rates = AsyncMock()
    rates.get_rate.return_value = 3.5
    svc = ConversionService(rates)
    out = await svc.convert(100, "USD", "PEN")
    assert out["rate"] == 3.5
    assert out["converted"] == 350.0


@pytest.mark.asyncio
async def test_convert_invalid_amount():
    rates = AsyncMock()
    svc = ConversionService(rates)
    with pytest.raises(ValueError):
        await svc.convert(0, "USD", "PEN")


@pytest.mark.asyncio
async def test_convert_same_currency():
    rates = AsyncMock()
    svc = ConversionService(rates)
    with pytest.raises(ValueError):
        await svc.convert(10, "USD", "USD")
