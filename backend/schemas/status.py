from enum import Enum

class StatusRepair(str, Enum):
    PENDING_VERIFICATION = "กำลังตรวจสอบ"
    PENDING_PAYMENT = "รอการชำระเงิน"
    PENDING_DELIVERY = "รอการจัดส่ง"
    UNDER_REPAIR = "กำลังดำเนินการซ่อม"
    DELIVERING = "กำลังจัดส่ง"
    COMPLETED = "เสร็จสิ้น"
    CANCELLED = "ยกเลิก"