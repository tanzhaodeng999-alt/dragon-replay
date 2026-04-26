import akshare as ak
import pandas as pd
from strategy import pick
from replay import send

def get_data():
    print("正在从 akshare 获取全市场行情...")
    try:
        # 获取实时行情快照（非交易时间会显示上一个交易日的数据）
        df = ak.stock_zh_a_spot_em()
        
        if df is None or df.empty:
            print("❌ 未获取到数据")
            return None
            
        # --- 关键点：把中文表头统一改成英文，防止后面识别错误 ---
        # 提取：代码, 名称, 涨跌幅, 换手率
        df = df[['代码', '名称', '涨跌幅', '换手率']]
        df.columns = ['code', 'name', 'pct_chg', 'turnover']
        
        # 转换数字类型，防止它是字符串导致没法计算
        df['pct_chg'] = pd.to_numeric(df['pct_chg'], errors='coerce')
        df['turnover'] = pd.to_numeric(df['turnover'], errors='coerce')
        
        return df
    except Exception as e:
        print(f"获取数据报错: {e}")
        return None

def run():
    df = get_data()
    # 运行策略
    result = pick(df)
    
    if result is not None and not result.empty:
        print(f"✅ 策略筛选完成，准备推送 {len(result)} 只股票")
        for index, row in result.iterrows():
            msg = f"📊 龙头扫描结果：\n股票：{row['name']}({row['code']})\n涨幅：{row['pct_chg']}%\n换手：{row['turnover']}%"
            send(msg)
    else:
        print("💡 当前未匹配到符合条件的股票。")

if __name__ == "__main__":
    run()
