from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field


from .domain import ConversionService
from .ports import RatesPort
from .adapters_fake import FakeRatesAdapter


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
async def convert(amount: float = Field(gt=0), from_: str = "USD", to: str = "PEN", rates: RatesPort = Depends(get_rates_port)):
    svc = ConversionService(rates)
    try:
        result = await svc.convert(amount, from_, to)
        return {**result, "from_": result["from"], "source": "fake"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=400, detail=str(e))