import pyautogui
import pytesseract
import pandas as pd
import time
from datetime import datetime
import os

# =========================
# 配置 Tesseract-OCR 安装路径
# =========================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tess_lang = "chi_sim+eng"

# =========================
# 定义两套区域
# =========================
# 🖥️ Desktop 上的区域 (原来的)
desktop_regions = {
    "summary_values": (3470, 336, 3785-3470, 692-336),
    "boiler1_values": (3445, 864, 3778-3445, 1287-864),
    "boiler2_values": (3440, 1411, 3784-3440, 1824-1411),
}

# 💻 Laptop 上的区域 (你的新记录)
laptop_regions = {
    "summary_values": (3380, 418, 387, 366),
    "boiler1_values": (3400, 930, 385, 418),
    "boiler2_values": (3394, 1477, 387, 408),
}

# =========================
# 选择当前使用的区域
# =========================
# 改成 laptop_regions 就能用你的笔记本区域
regions = laptop_regions
# regions = desktop_regions  # 想切回桌面时用这个

# =========================
# 输出文件夹 C:\Users\game0\OneDrive\Desktop\Cursior\captured data
# =========================
output_dir = r"C:\Users\game0\OneDrive\Desktop\Cursior\captured data"
os.makedirs(output_dir, exist_ok=True)
test_file = r"C:\Users\game0\OneDrive\Desktop\Cursior\captured data\test.csv"
open(test_file, "w").close()

current_hour = None
output_csv = None

print(f"✅ 已启动，每小时新建 CSV 并强制 flush，保存路径：{output_dir}\n按 Ctrl+C 停止。\n")

try:
    while True:
        now = datetime.now()
        # ⚠️ 文件名格式注意：不要用冒号
        hour_tag = now.strftime("%Y-%m-%d_%H")  # 例如 2025-07-23_16
        output_filename = f"capture_{hour_tag}.csv"
        output_csv = os.path.join(output_dir, output_filename)

        # 如果小时变化了，创建新文件
        if hour_tag != current_hour:
            current_hour = hour_tag
            # 初始化文件并写入表头
            df_init = pd.DataFrame({
                "timestamp": [],
                "summary_values": [],
                "boiler1_values": [], 
                "boiler2_values": []
            })
            df_init.to_csv(output_csv, index=False, mode="w", encoding="utf-8-sig")
            print(f"🆕 新文件已创建: {output_csv}")

            # 新建后立即 flush 一次，确保文件头写入
            try:
                with open(output_csv, 'a', encoding='utf-8-sig') as f:
                    f.flush()
                    os.fsync(f.fileno())
                print(f"💾 文件头已 flush：{output_csv}")
            except Exception as e:
                print(f"⚠️ 文件头 flush 出错: {e}")

        # 采集数据
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        row_data = {"timestamp": timestamp}

        for region_name, (x, y, w, h) in regions.items():
            img = pyautogui.screenshot(region=(x, y, w, h))
            text = pytesseract.image_to_string(img, lang=tess_lang, config="--psm 6")
            row_data[region_name] = text.replace("\n", " ").strip()

        # 写入 CSV
        pd.DataFrame([row_data]).to_csv(output_csv, mode="a", index=False, header=False, encoding="utf-8-sig")
        print(f"[{timestamp}] ✅ 已记录一行数据")

        # 每秒采集一次
        time.sleep(1)

except KeyboardInterrupt:
    print("⏹️ 已停止捕捉，数据保存于:", output_dir)
