import json
from decimal import Decimal

with open("trades.json", "r") as f:
    trades_data = json.load(f)

    bought = Decimal("0")
    sold = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        if trade["bought"]:
            bought += Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
            matecoin_account += Decimal(trade["bought"])
        else:
            sold += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

profit = {
    "earned_money": float(sold - bought),
    "matecoin_account": float(matecoin_account)
}
with open("profit.json", "w") as f:
    json.dump(profit, f, indent=2)
