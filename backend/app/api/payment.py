# Dummy payment API
from fastapi import APIRouter, Depends, HTTPException
from ..models.payment import Payment
from ..services.payment_service import PaymentService

router = APIRouter()

@router.post("/process", response_model=Payment)
async def process_payment(payment: Payment, service: PaymentService = Depends()):
    try:
        processed = await service.process_payment(payment)
        return processed
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
