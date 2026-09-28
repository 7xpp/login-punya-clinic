const API_URL = "http://127.0.0.1:8005/api/v1";

// Create OTP
export const CreateResetEmailOTPAPI = async (payload) => {
    const response = await fetch(`${API_URL}/reset_email`, {
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
export const CreateResetEmailOTPAgainAPI = async () => {
    const response = await fetch(`${API_URL}/create_reset_email_otp_again`, {
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
export const CheckResetEmailOTPAPI = async (payload) => {
    const response = await fetch(`${API_URL}/check_otp_email`, {
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