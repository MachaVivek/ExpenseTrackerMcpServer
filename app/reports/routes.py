from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import StreamingResponse

from datetime import date, datetime
from io import StringIO

import pandas as pd

from app.database.prisma import db
from app.auth.dependencies import get_current_user


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/export-csv")
async def export_csv(
    startDate: date,
    endDate: date,
    current_user=Depends(get_current_user)
):
    # Export user transactions and budgets as CSV file between selected dates.

    # Convert date → datetime range
    start_date = datetime.combine(
        startDate,
        datetime.min.time()
    )

    end_date = datetime.combine(
        endDate,
        datetime.max.time()
    )

    # Fetch transactions
    transactions = await db.transaction.find_many(
        where={
            "userId": current_user.id,
            "transactionDate": {
                "gte": start_date,
                "lte": end_date
            }
        }
    )

    # Fetch budgets
    budgets = await db.budget.find_many(
        where={
            "userId": current_user.id,
            "startDate": {
                "gte": start_date
            },
            "endDate": {
                "lte": end_date
            }
        }
    )

    # Final CSV rows
    rows = []

    # Add transactions to CSV rows
    for transaction in transactions:

        rows.append({
            "TYPE": "TRANSACTION",
            "TITLE": transaction.title,
            "AMOUNT": transaction.amount,
            "CATEGORY": transaction.category,
            "TRANSACTION_TYPE": transaction.type,
            "DATE": transaction.transactionDate
        })

    # Add budgets to CSV rows
    for budget in budgets:

        rows.append({
            "TYPE": "BUDGET",
            "TITLE": budget.name,
            "AMOUNT": budget.amount,
            "CATEGORY": budget.category,
            "TRANSACTION_TYPE": budget.period,
            "DATE": budget.startDate
        })

    # Create pandas DataFrame
    df = pd.DataFrame(rows)

    # Create in-memory CSV buffer
    csv_buffer = StringIO()

    # Convert DataFrame → CSV
    df.to_csv(
        csv_buffer,
        index=False
    )

    # Move cursor to start
    csv_buffer.seek(0)

    # Dynamic filename
    filename = (
        f"financial_report_"
        f"{startDate}_to_{endDate}.csv"
    )

    # Return downloadable CSV response
    return StreamingResponse(
        iter([csv_buffer.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":
            f"attachment; filename={filename}"
        }
    )