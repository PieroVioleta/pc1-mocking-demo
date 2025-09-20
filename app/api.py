from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from .adapters_fake import FakeRatesAdapter
from .domain import ConversionService
from .ports import RatesPort

router = APIRouter()


def get_rates_port() -> RatesPort:
    return FakeRatesAdapter()


class ConvertResponse(BaseModel):
    amount: float
    from_: str
    to: str
    rate: float
    converted: float
    source: str


@router.get("/convert", response_model=ConvertResponse)
async def convert(
    amount: float = Query(..., gt=0),
    from_: str = Query("USD"),
    to: str = Query("PEN"),
    rates: RatesPort = Depends(get_rates_port),
):
    svc = ConversionService(rates)
    try:
        result = await svc.convert(amount, from_, to)
        return {**result, "from_": result["from"], "source": "fake"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=400, detail=str(e))
