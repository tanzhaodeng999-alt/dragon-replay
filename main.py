import akshare as ak
from strategy import pick
from replay import send
import pandas as pd
from datetime import datetime

def run():

    now = datetime.now()

    # 👉 判断是否交易时间（简单版）
    is_trade_time = now.hour >= 9 and now.hour <= 15

    df = ak.stock_zt_pool_em()

    # 👉 非交易时间 or 数据为空 → 用测试数据
    if df is None or df.empty:
        send("⚠️ 当前非交易时间，进入测试模式")

        df = pd.DataFrame([
            {"名称": "测试龙头A", "涨跌幅": 10, "换手率": 28, "成交额": 8e8, "连板数": 3},
            {"名称": "测试龙头B", "涨跌幅": 9, "换手率": 22, "成交额": 6e8, "连板数": 2},
        ])

    leaders = pick(df)
    leader = leaders.iloc[0]

    msg = f"""
📊 模拟复盘

🔥 龙头：{leader['名称']}
连板：{leader.get('连板数', 0)}
涨幅：{leader['涨跌幅']}%
换手：{leader['换手率']}%

👉 明日策略：
龙头分歧低吸
"""

    send(msg)


if __name__ == "__main__":
    run()
