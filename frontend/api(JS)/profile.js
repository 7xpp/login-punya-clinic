const API_URL = "http://127.0.0.1:8005/api/v1";

export const ResponseRepairAPI = async () => {
    const response = await fetch(`${API_URL}/repair_response`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail || "เกิดข้อผิดพลาดในการดึงข้อมูลรายการซ่อม");
    }
    return result;
};

export const CancelRepairAPI = async (id) => {
    const response = await fetch(`${API_URL}/cancel_repair/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail || "เกิดข้อผิดพลาดในการยกเลิกรายการซ่อม");
    }
    return result;
};