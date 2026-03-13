import pandas as pd
import numpy as np
import os

def load_and_summarize(file_path):
    # เพิ่ม on_bad_lines='skip' เพื่อข้ามบรรทัดที่คอลัมน์ไม่เท่ากัน
    # และใช้ engine='python' เพื่อให้รองรับการจัดการไฟล์ที่โครงสร้างไม่เป๊ะ
    try:
        raw_df = pd.read_csv(
            file_path, 
            skiprows=8, 
            header=None, 
            sep='\s+', 
            on_bad_lines='skip', 
            engine='python'
        )
    except Exception as e:
        print(f"ไม่สามารถอ่านไฟล์ {file_path} ได้: {e}")
        return None

    vals = []
    # เนื่องจากบางบรรทัดอาจจะโดน skip ไป เราต้องเช็คจำนวนคอลัมน์ที่มีอยู่จริงด้วย
    num_cols = raw_df.shape[1]
    for i in range(0, min(num_cols, 8), 2):
        if i+1 < num_cols:
            vals.extend(raw_df[i+1].dropna().tolist())
    
    # ส่วนที่เหลือเหมือนเดิม...
    arr = pd.to_numeric(vals, errors='coerce')
    arr = arr[~np.isnan(arr)]
    
    if len(arr) == 0: return None # ถ้าไม่มีข้อมูลเลยให้ข้ามไฟล์นี้

    rms = np.sqrt(np.mean(arr**2))
    peak = np.max(np.abs(arr))
    kurtosis = pd.Series(arr).kurtosis()
    
    return {
        'filename': os.path.basename(file_path),
        'RMS': rms,
        'Peak': peak,
        'Kurtosis': kurtosis
    }

# วนลูปอ่านทุกไฟล์ในโฟลเดอร์ data
data_dir = 'data'
all_features = []

for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        path = os.path.join(data_dir, filename)
        print(f"กำลังประมวลผล: {filename}")
        features = load_and_summarize(path)
        all_features.append(features)

# สร้างเป็น DataFrame สรุปผล
summary_df = pd.DataFrame(all_features)
print("\n--- ตารางสรุป Feature สำหรับทำ ML ---")
print(summary_df)

# บันทึกเป็น CSV ไว้ใช้เทรน AI
summary_df.to_csv('vibration_features.csv', index=False)
print("\nบันทึกไฟล์ vibration_features.csv สำเร็จ!")