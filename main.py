import akshare as ak
from strategy import pick, market_emotion, generate_plan
from replay import send
import pandas as pd

def run():

    df = ak.stock_zt_pool_em()

    # 空数据保护
    if df is None or df.empty:
        send("⚠️ 当前无数据（非交易时间）")
        return

    # 龙头
    leaders = pick(df)
    leader = leaders.iloc[0]

    # 情绪
    emotion = market_emotion(df)

    # 交易计划
    plan = generate_plan(leader, emotion)

    msg = f"""
📊 A股复盘

🔥 龙头：{leader['名称']}
连板：{leader.get('连板数', 0)}
涨幅：{leader['涨跌幅']}%
换手：{leader['换手率']}%

📈 市场情绪：{emotion}

🧠 明日交易计划：
{plan}
"""

    send(msg)


if __name__ == "__main__":
    run()
