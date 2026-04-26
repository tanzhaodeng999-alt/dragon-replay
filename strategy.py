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
def market_emotion(df):
    if df is None or df.empty:
        return "未知"
    
    zt_count = len(df)
    
    if zt_count > 60:
        return "高潮"
    elif zt_count > 30:
        return "活跃"
    elif zt_count > 10:
        return "一般"
    else:
        return "冰点"
   def leader_stage(row):
    lb = row.get('连板数', 0)
    
    if lb <= 2:
        return "启动期"
    elif lb <= 5:
        return "主升期"
    else:
        return "高位期"
def generate_plan(row, emotion):
    stage = leader_stage(row)
    name = row['名称']
    
    # 情绪优先
    if emotion == "冰点":
        return f"🧊 情绪冰点：小仓位试错 {name}"
    
    if emotion == "高潮":
        return "⚠️ 情绪高潮：禁止追高，考虑减仓"
    
    # 阶段逻辑
    if stage == "启动期":
        return f"🚀 启动期：关注 {name} 打板机会"
    
    elif stage == "主升期":
        return f"🔥 主升期：低吸 {name}（回踩不破低点）"
    
    elif stage == "高位期":
        return f"⚠️ 高位期：只做分歧，不追 {name}"
    
    return "观望"
