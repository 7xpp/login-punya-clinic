const API_URL = "http://127.0.0.1:8005/api/v1";

// Create OTP
export const CreateOTPAPI = async () => {
    const response = await fetch(`${API_URL}/forgot_password`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail)
    }
    return result;
};

// Create OTP Again
export const CreateOTPAgainAPI = async () => {
    const response = await fetch(`${API_URL}/create_forgot_password_otp_again`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail)
    }
    return result;
};

// Check OTP
export const CheckOTPAPI = async (payload) => {
    const response = await fetch(`${API_URL}/check_otp`, {
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

// Confirm Password
export const ConfirmPasswordAPI = async (payload) => {
    const response = await fetch(`${API_URL}/confirm_password`, {
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