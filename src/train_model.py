import pandas as pd

# 1. โหลดข้อมูลที่เราทำไว้
df = pd.read_csv('vibration_features.csv')

# 2. ตั้งเกณฑ์ความปลอดภัย (Threshold) 
# สมมติว่าจากมาตรฐานเครื่องจักร ถ้า RMS > 0.58 คือเริ่มอันตราย (Warning)
def check_status(rms):
    if rms > 0.58:
        return 'Danger (Need Maintenance)'
    elif rms > 0.50:
        return 'Warning'
    else:
        return 'Normal'

# 3. ลองทำนายผลจากข้อมูลที่มี
df['Predicted_Status'] = df['RMS'].apply(check_status)

# 4. แสดงผลลัพธ์
print("--- สรุปผลการวิเคราะห์สภาพเครื่องจักร (Predictive Maintenance) ---")
print(df[['filename', 'RMS', 'Predicted_Status']])

# 5. บันทึกผลส่งอาจารย์
df.to_csv('maintenance_report.csv', index=False)
print("\nบันทึกรายงาน maintenance_report.csv เรียบร้อย!")