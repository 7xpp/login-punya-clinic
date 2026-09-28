const API_URL = "http://127.0.0.1:8005/api/v1";

// Reset password
export const changepasswordAPI = async (payload) => {
    const response = await fetch(`${API_URL}/reset_password_password`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail);
    }
    return result;
}

// Confirm reset password
export const confirmchangepasswordAPI = async (payload) => {
    const response = await fetch(`${API_URL}/reset_password`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail)
    }
    return result;
};