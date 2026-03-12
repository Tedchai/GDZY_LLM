import pandas as pd
import re

# 🔧 文件路径
input_csv = "realdatacapture_6blocks.csv"
output_csv = "realdatacapture_structured.csv"

# 正则：抓取数值+单位（单位可选）
pattern = re.compile(r"(\d+\.\d+)")

# 将 OCR 文本分割提取
def extract_numbers(text, expected_count):
    if pd.isna(text):
        return [""] * expected_count
    values = pattern.findall(text)
    # 如果识别数值少于应有列数，填充空值
    while len(values) < expected_count:
        values.append("")
    return values[:expected_count]

# 定义每块应该有的字段顺序
pressure_fields = ["压力给定", "母管压力", "母压均值", "总负荷给定", "总负荷"]
boiler_fields = ["负荷给定", "实际负荷", "主汽压力", "给粉转速", "外扰前馈", "给粉MOD"]

# 读取原始 CSV
df = pd.read_csv(input_csv)

cleaned_rows = []
for _, row in df.iterrows():
    timestamp = row["timestamp"]

    # 处理 pressure_summary 和 summary_values
    p_labels = extract_numbers(row["pressure_summary"], len(pressure_fields))
    p_values = extract_numbers(row["summary_values"], len(pressure_fields))

    # 处理 boiler1
    b1_labels = extract_numbers(row["boiler1_buttons"], len(boiler_fields))
    b1_values = extract_numbers(row["boiler1_values"], len(boiler_fields))

    # 处理 boiler2
    b2_labels = extract_numbers(row["boiler2_buttons"], len(boiler_fields))
    b2_values = extract_numbers(row["boiler2_values"], len(boiler_fields))

    # 合成一行
    cleaned_rows.append({
        "timestamp": timestamp,
        # 压力区
        pressure_fields[0]: p_values[0],
        pressure_fields[1]: p_values[1],
        pressure_fields[2]: p_values[2],
        pressure_fields[3]: p_values[3],
        pressure_fields[4]: p_values[4],
        # #1炉区
        "#1炉"+boiler_fields[0]: b1_values[0],
        "#1炉"+boiler_fields[1]: b1_values[1],
        "#1炉"+boiler_fields[2]: b1_values[2],
        "#1炉"+boiler_fields[3]: b1_values[3],
        "#1炉"+boiler_fields[4]: b1_values[4],
        "#1炉"+boiler_fields[5]: b1_values[5],
        # #2炉区
        "#2炉"+boiler_fields[0]: b2_values[0],
        "#2炉"+boiler_fields[1]: b2_values[1],
        "#2炉"+boiler_fields[2]: b2_values[2],
        "#2炉"+boiler_fields[3]: b2_values[3],
        "#2炉"+boiler_fields[4]: b2_values[4],
        "#2炉"+boiler_fields[5]: b2_values[5],
    })

# 转换为 DataFrame
clean_df = pd.DataFrame(cleaned_rows)

# 保存
clean_df.to_csv(output_csv, index=False, encoding="utf-8-sig")
print(f"✅ 清理完成，结构化 CSV 已保存到：{output_csv}")
