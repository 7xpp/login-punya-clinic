const API_URL = "http://127.0.0.1:8005/api/v1";

// Signup
export const signupAPI = async (payload) => {
    const response = await fetch(`${API_URL}/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail);
    }
    return result;
};

// Login
export const loginAPI = async (payload) => {
    const response = await fetch(`${API_URL}/login`, {
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