from unittest.mock import AsyncMock

import pytest

from app.domain import ConversionService


@pytest.mark.asyncio
async def test_convert_ok():
    """
    GIVEN   a ConversionService with a mocked RatesPort returning 3.5
    WHEN    converting 100 USD to PEN
    THEN    the result should include rate=3.5 and converted=350.0
    """
    rates = AsyncMock()
    rates.get_rate.return_value = 3.5
    svc = ConversionService(rates)
    out = await svc.convert(100, "USD", "PEN")
    assert out["rate"] == 3.5
    assert out["converted"] == 350.0


@pytest.mark.asyncio
async def test_convert_invalid_amount():
    """
    GIVEN   a ConversionService with a mocked RatesPort
    WHEN    converting with amount=0
    THEN    a ValueError should be raised
    """
    rates = AsyncMock()
    svc = ConversionService(rates)
    with pytest.raises(ValueError):
        await svc.convert(0, "USD", "PEN")


@pytest.mark.asyncio
async def test_convert_same_currency():
    """
    GIVEN   a ConversionService with a mocked RatesPort
    WHEN    converting from and to the same currency (USD -> USD)
    THEN    a ValueError should be raised
    """
    rates = AsyncMock()
    svc = ConversionService(rates)
    with pytest.raises(ValueError):
        await svc.convert(10, "USD", "USD")
