# Vibration Predictive Maintenance Project

โปรเจกต์วิเคราะห์และทำนายสภาพเครื่องจักร (ปั๊มน้ำ) โดยใช้ข้อมูลการสั่นสะเทือน (Vibration Analysis)

## 📌 โครงสร้างโปรเจกต์
- `data/`: เก็บไฟล์ข้อมูล Raw Signal (.txt) แบ่งตามอุปกรณ์และเดือน
- `src/`: โค้ดหลักสำหรับการจัดการข้อมูลและสกัด Feature
- `notebooks/`: ไฟล์วิเคราะห์ข้อมูลและพลอตกราฟสรุปผล
- `vibration_features.csv`: ข้อมูล Feature ที่สกัดได้ (RMS, Peak, Kurtosis)

## 🚀 วิธีการใช้งาน
1. รัน `python src/extract_features.py` เพื่อเตรียมข้อมูล
2. รัน `python src/train_model.py` เพื่อทำนายสภาพเครื่องจักร
3. ดูผลวิเคราะห์ฉบับเต็มได้ใน `notebooks/Final_Analysis.ipynb`

## 📊 ผลการวิเคราะห์
ระบบสามารถแยกแยะความผิดปกติของเครื่องจักรได้จากค่า RMS และ Peak โดยพบว่า Cooling Pump มีแนวโน้มต้องการการบำรุงรักษาเนื่องจากค่าการสั่นสะเทือนพุ่งสูงขึ้นอย่างต่อเนื่อง