#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Retirement time calculator (inflation-adjusted)

Computes years to reach a retirement goal stated in *today's dollars* (purchasing power),
given constant annual contributions and nominal investment return scenarios.

We convert nominal returns to real returns using:
    r_real = (1 + r_nominal) / (1 + inflation) - 1
"""

from __future__ import annotations

import numpy_financial as npf


def real_rate(nominal_rate: float, inflation_rate: float) -> float:
    """Convert nominal return to real (inflation-adjusted) return."""
    return (1.0 + nominal_rate) / (1.0 + inflation_rate) - 1.0


def years_to_goal_real(
    annual_contribution: float,
    real_return: float,
    goal_today_dollars: float,
    start_balance: float = 0.0,
) -> float:
    """
    Years needed to reach a goal in today's dollars, assuming:
    - constant annual_contribution (end of each year),
    - constant real_return,
    - starting balance = start_balance.
    """
    if annual_contribution <= 0:
        raise ValueError("annual_contribution must be > 0.")
    if goal_today_dollars <= start_balance:
        return 0.0
    # nper uses the sign convention: deposits are negative cash flows
    return float(npf.nper(real_return, -annual_contribution, start_balance, goal_today_dollars))


def main() -> None:
    # Inputs (today's dollars)
    salary = 60_000
    goal_today = 1_500_000
    inflation = 0.02

    savings_rates = [0.10, 0.25, 0.40]
    nominal_returns = [0.04, 0.05, 0.06]

    print(f"Salary: ${salary:,.0f}")
    print(f"Goal (today's dollars): ${goal_today:,.0f}")
    print(f"Inflation: {inflation*100:.1f}%\n")

    # Table header
    header = "Savings\\Return | " + " | ".join(f"{r*100:.0f}%" for r in nominal_returns)
    print(header)
    print("-" * len(header))

    for s in savings_rates:
        annual_cash = salary * s
        row = [f"{s*100:.0f}% (${annual_cash:,.0f}/yr)".ljust(15)]

        for r_nom in nominal_returns:
            r_real = real_rate(r_nom, inflation)
            yrs = years_to_goal_real(annual_cash, r_real, goal_today)
            row.append(f"{yrs:6.1f}")

        print(" | ".join(row))


if __name__ == "__main__":
    main()

