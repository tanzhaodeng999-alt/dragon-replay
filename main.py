import akshare as ak
from strategy import pick
from replay import send

def run():

    df = ak.stock_zt_pool_em()

    top = pick(df)

    leader = top.iloc[0]

    msg = f"""
📊 A股复盘

🔥 龙头：{leader['名称']}
评分：{leader['score']}
涨幅：{leader['涨跌幅']}%
换手：{leader['换手率']}%

👉 明日策略：
- 龙头分歧低吸
"""

    send(msg)


if __name__ == "__main__":
    run()
