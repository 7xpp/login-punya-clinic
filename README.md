# ======================
# Punya Clinic Watch
# ======================
    เป้นเว็บไซต์สำหรับซ่อมนาฬิกาที่ถูกสร้างขึ้นมาเพื่อรองรับธุรกิจที่บ้าน โดยมุ่งเน้นการพัฒนา Backend Architecture
    ****ในส่วนของ Frontend เป็นเพียงแค่ตัว Prototype ที่ถูกสร้างขึ้นมาเพื่อแสดงการทำงานของฝั่ง Backend เท่านั้น****
    
  ## Punya Clinic Watch
      Layered Architecture 3 ชั้น : แบ่งแยกความรับผิดชอบชัดเจนระหว่าง API, Service Layer และ Repository

  ## Technologies
      Backend Framework: FastAPI (Python)
      Unit Of Work
      Generic TypeVar
      CrudBase : create(), update(), remove()
      Database & ORM: SQLAlchemy ORM, SQLite (Local) / Supabase PostgreSQL (Production)
      Authentication & Security: JWT (JSON Web Tokens), HTTP-Only Cookies, Passlib (Bcrypt Password Hashing)
      Frontend ( Prototype )

  ## Features
      1. Authentication
        - Login
        - Signup
      2. การส่งซ่อม
        - ขอ Signed URL เพื่อบันทึกรูปภาพลง database โดยตรง
        - การดึงที่อยู่ที่มีค่าเป็น ที่อยู่หลักมาไว้อัตโนมัติ
        - การแสดงผลข้อมูลการซ่อม
      3. Address
        - การเพิ่มที่อยู่ (สูงสุด 5 ที่อยู่)
        - การแก้ไขที่อยู่โดยจะดึงข้อมูลที่จะแก้มาแสดง และจะส่งไปแค่ฟิลด์ที่ผู้ใช้กรอกเข้ามา
        - การลบที่อยู่โดยการดึงข้อมูลที่ลบแล้วมาแสดงว่าลบข้อมูลตัวไหนไป
            **การลบที่อยู่ที่เป็นค่า Default จะเปลี่ยนค่าในกับที่อยู่ที่สร้างใหม่ล่าสุด
      4. เปลี่ยนข้อมูล (ในอนาคตจะมีการใช้บริการ SMTP ในการส่ง OTP)
        - เปลี่ยนรหัสผ่าน (ใช้รหัสผ่านเก่า)
        - เปลี่ยนรหัสผ่าน (OTP)
        - เปลี่ยนอีเมล (OTP)
        - เปลี่ยนเบอร์โทร (OTP)

  ## Setup
        - Python 3.10+
  ## Clone Repository:**
     bash
     git clone [https://github.com/7xpp/login-punya-clinic.git](https://github.com/7xpp/login-punya-clinic.git)
     cd login-punya-clinic

   pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-multipart

   python -m uvicorn main.main:app --reload --port 8005

   pip install -r requirements.txt
