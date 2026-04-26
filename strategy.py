def score(row):
    s = 0
    
    # 1️⃣ 连板（最重要）
    if '连板数' in row:
        s += row['连板数'] * 10
    
    # 2️⃣ 涨幅
    if row['涨跌幅'] > 7:
        s += 20
    
    # 3️⃣ 换手（人气）
    if 20 <= row['换手率'] <= 40:
        s += 20
    
    # 4️⃣ 成交额（资金参与）
    if row['成交额'] > 5e8:
        s += 20
    
    return s


def pick(df):
    df['score'] = df.apply(score, axis=1)
    df = df.sort_values(by='score', ascending=False)
    
    return df.head(3)
