import pandas as pd

def pick(df):
    # 1. 断路器：如果数据是空的，直接退出
    if df is None or df.empty:
        return None

    try:
        # 2. 策略筛选逻辑（这里你可以根据游资逻辑修改参数）
        # 筛选：涨幅在 9.5% 以上（锁定涨停或强力冲击涨停的）
        # 且换手率在 3% 到 20% 之间（保证活跃度）
        dragons = df[
            (df['pct_chg'] > 9.5) & 
            (df['turnover'] > 3) & 
            (df['turnover'] < 25)
        ].copy()

        if dragons.empty:
            return None

        # 3. 简单评分排序：涨幅 * 0.7 + 换手 * 0.3
        dragons['score'] = dragons['pct_chg'] * 0.7 + dragons['turnover'] * 0.3
        
        # 取评分最高的前 3 名
        top_3 = dragons.sort_values(by='score', ascending=False).head(3)
        return top_3

    except Exception as e:
        print(f"策略模块报错: {e}")
        return None
