const API_URL = "http://127.0.0.1:8005/api/v1";

// Signed Upload URL
export const signedUrlAPI = async (fileList) => {
    const payload = Array.isArray(fileList) ? { file_list: fileList } : fileList;
    const response = await fetch(`${API_URL}/upload_img_repair`, {
        method: "POST",
        credentials: 'include',
        headers: { "Content-type": "application/json" },
        body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail)
    }
    return result;
};

// Response Address Repair
export const repairAddressResponseAPI = async () => {
    const response = await fetch(`${API_URL}/response_address_repair`, {
        method: "GET",
        credentials: 'include',
        headers: { "Content-type": "application/json" }
    });
    const result = await response.json();
    return result;
};

// Repair
export const repairAPI = async (payload) => {
    const response = await fetch(`${API_URL}/repair`, {
        method: "POST",
        credentials: 'include',
        headers: { "Content-type": "application/json" },
        body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail)
    }
    return result;
};

