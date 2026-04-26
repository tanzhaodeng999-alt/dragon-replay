import akshare as ak
from strategy import pick
from replay import send

def run():

    # 获取涨停池
    df = ak.stock_zt_pool_em()

    # 选龙头
    leaders = pick(df)
    leader = leaders.iloc[0]

    msg = f"""
📊 A股复盘

🔥 今日龙头：{leader['名称']}
连板：{leader['连板数']}
涨幅：{leader['涨跌幅']}%
换手：{leader['换手率']}%

👉 明日策略：
龙头分歧低吸
"""

    send(msg)


if __name__ == "__main__":
    run()
