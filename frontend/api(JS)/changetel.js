const API_URL = "http://127.0.0.1:8005/api/v1";

// Create OTP
export const CreateResetTelOTPAPI = async (payload) => {
    const response = await fetch(`${API_URL}/reset_tel`, {
        method: "POST",
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

// Create OTP Again
export const CreateResetTelOTPAgainAPI = async () => {
    const response = await fetch(`${API_URL}/create_reset_tel_otp_again`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail)
    }
    return result;
};

// Check OTP
export const CheckResetTelOTPAPI = async (payload) => {
    const response = await fetch(`${API_URL}/check_otp_tel`, {
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