# Inflation-adjusted retirement calculator

Computes the number of years to reach a retirement goal stated in **today’s dollars**
(purchasing power), assuming constant yearly contributions and constant returns.

## How it handles inflation
Nominal return is converted to real return:
`r_real = (1 + r_nominal) / (1 + inflation) - 1`

## Run
```bash
pip install -r requirements.txt
python retirement_inflation.py
