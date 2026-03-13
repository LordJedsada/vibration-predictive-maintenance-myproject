import pandas as pd
import matplotlib.pyplot as plt

def load_vibration_data(file_path):
    # อ่านไฟล์โดยข้ามหัว 8 บรรทัดแรก
    raw_df = pd.read_csv(file_path, skiprows=8, header=None, sep='\s+')
    
    time_series = []
    amp_series = []
    
    # รวมข้อมูลจาก 4 คู่คอลัมน์ให้เป็นเส้นเดียว
    for i in range(0, 8, 2):
        time_series.extend(raw_df[i].dropna().tolist())
        amp_series.extend(raw_df[i+1].dropna().tolist())
    
    return pd.DataFrame({'Time_mS': time_series, 'Amplitude_G': amp_series})

# เลือกไฟล์มาลอง 1 ไฟล์ (เช่น Cooling Pump เดือน มิ.ย.)
file_to_test = 'data/A_Cooling Pump OAH 02_M1H_1480_Jun24.txt'

try:
    df = load_vibration_data(file_to_test)
    print(f"--- ข้อมูลจากไฟล์: {file_to_test} ---")
    print(df.head())
    print(f"จำนวนจุดข้อมูลทั้งหมด: {len(df)} จุด")

    # พลอตกราฟดูรูปร่างคลื่น
    plt.figure(figsize=(12, 5))
    plt.plot(df['Time_mS'], df['Amplitude_G'], color='blue', linewidth=0.5)
    plt.title('Vibration Waveform - Cooling Pump (Jun 24)')
    plt.xlabel('Time (mS)')
    plt.ylabel('Amplitude (G)')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")