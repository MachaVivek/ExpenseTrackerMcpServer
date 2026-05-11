from fastmcp import Context

from app.mcp.server import mcp


# =========================================================
# SIMPLE INTEREST CALCULATOR
# =========================================================
# This tool does NOT require authentication.
# Anyone using the MCP server can access it.
#
# Formula:
# SI = (P × R × T) / 100
#
# P = Principal Amount
# R = Annual Interest Rate
# T = Time in Years
# =========================================================
@mcp.tool()
async def calculate_simple_interest(
    ctx: Context,
    principal: float,
    rate: float,
    time: float
):
    if principal <= 0:
        return {
            "error": "Principal amount must be greater than 0"
        }
    if rate <= 0:
        return {
            "error": "Interest rate must be greater than 0"
        }
    if time <= 0:
        return {
            "error": "Time must be greater than 0"
        }
    simple_interest = (
        principal * rate * time
    ) / 100
    total_amount = principal + simple_interest
    return {
        "success": True,
        "calculation_type": "Simple Interest",
        "principal": round(principal, 2),
        "rate": round(rate, 2),
        "time_years": round(time, 2),
        "interest": round(simple_interest, 2),
        "total_amount": round(total_amount, 2)
    }


# =========================================================
# COMPOUND INTEREST CALCULATOR
# =========================================================
# This tool also does NOT require authentication.
#
# Formula:
# A = P(1 + R/N)^(N*T)
#
# Compound Interest = A - P
#
# P = Principal
# R = Annual Rate
# N = Times compounded per year
# T = Time in years
# =========================================================
@mcp.tool()
async def calculate_compound_interest(
    ctx: Context,
    principal: float,
    rate: float,
    time: float,
    compounds_per_year: int = 1
):
    if principal <= 0:
        return {
            "error": "Principal amount must be greater than 0"
        }
    if rate <= 0:
        return {
            "error": "Interest rate must be greater than 0"
        }
    if time <= 0:
        return {
            "error": "Time must be greater than 0"
        }
    if compounds_per_year <= 0:
        return {
            "error": "Compounds per year must be greater than 0"
        }

    decimal_rate = rate / 100

    total_amount = principal * (
        1 + decimal_rate / compounds_per_year
    ) ** (compounds_per_year * time)

    compound_interest = (
        total_amount - principal
    )

    return {
        "success": True,
        "calculation_type": "Compound Interest",
        "principal": round(principal, 2),
        "rate": round(rate, 2),
        "time_years": round(time, 2),
        "compounds_per_year": compounds_per_year,
        "interest": round(compound_interest, 2),
        "total_amount": round(total_amount, 2)
    }

