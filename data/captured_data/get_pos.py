import pyautogui
import time

regions = []  # to store all regions

for i in range(1, 4):  # 3 regions
    print(f"\n==== 第 {i} 个区域 ====")
    print("移动鼠标到你想要截取区域的【左上角】，5秒后获取位置...")
    time.sleep(5)
    top_left = pyautogui.position()
    print("左上角坐标:", top_left)

    print("移动鼠标到你想要截取区域的【右下角】，5秒后获取位置...")
    time.sleep(5)
    bottom_right = pyautogui.position()
    print("右下角坐标:", bottom_right)

    # calculate region
    left = top_left.x
    top = top_left.y
    width = bottom_right.x - top_left.x
    height = bottom_right.y - top_left.y
    region = (left, top, width, height)
    regions.append(region)

    print(f"第 {i} 个区域的 region 参数: {region}")

print("\n全部区域已记录完毕：")
for idx, r in enumerate(regions, start=1):
    print(f"Region {idx}: {r}")
