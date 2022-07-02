profit = int(input("请输入当月利润："))
if profit <= 10:
    commission = profit * 0.1
elif profit <= 20:
    commission = 10 * 0.1 + (profit - 10) * 0.075
elif profit <= 40:
    commission = 10 * 0.1 + 10 * 0.075 + (profit - 20) * 0.05
elif profit <= 60:
    commission = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (profit - 40) * 0.03
elif profit <= 100:
    commission = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (profit - 60) * 0.015
else:
    commission = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (profit - 100) * 0.01
print(f"奖金为{commission}万元")