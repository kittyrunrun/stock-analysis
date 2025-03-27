import pandas as pd

# อ่านข้อมูลจากไฟล์ CSV
data = pd.read_csv("stock_data.csv")

# กรองข้อมูลเฉพาะหุ้น AOT
aot_data = data[data['Stock'] == 'AOT'].copy()  # ใช้ .copy() เพื่อป้องกัน Warning

# คำนวณแนวโน้มราคาหุ้น 
aot_data['Price_Change'] = aot_data['Price'].diff()
aot_data['Trend'] = aot_data['Price_Change'].apply(lambda x: 'Up' if x > 0 else 'Down' if x < 0 else 'Stable')

# สรุปผลการวิเคราะห์
trend_summary = aot_data['Trend'].value_counts()

# บันทึกผลการวิเคราะห์ลงไฟล์
with open("aot_analysis.txt", "w", encoding="utf-8") as file:
    file.write("AOT Stock Trend Analysis\n")
    file.write("=========================\n")
    file.write(f"Total Days: {len(aot_data)}\n")
    file.write(f"Up Days: {trend_summary.get('Up', 0)}\n")
    file.write(f"Down Days: {trend_summary.get('Down', 0)}\n")
    file.write(f"Stable Days: {trend_summary.get('Stable', 0)}\n")

print("Analysis completed! Results saved in 'aot_analysis.txt'")
