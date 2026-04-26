def score(row):
    s = 0
    
    # 涨幅
    if row['涨跌幅'] > 7:
        s += 20
    
    # 换手
    if 20 <= row['换手率'] <= 40:
        s += 20
    
    # 成交额
    if row['成交额'] > 5e8:
        s += 20
    
    return s


def pick(df):
    df['score'] = df.apply(score, axis=1)
    return df.sort_values(by='score', ascending=False).head(3)
