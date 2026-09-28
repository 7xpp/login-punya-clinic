const API_URL = "http://127.0.0.1:8005/api/v1";

// Create Address
export const addressAPI = async (payload) => {
    const response = await fetch(`${API_URL}/address`, {
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
};

// Response Address
export const responseAddressAPI = async () => {
    const response = await fetch(`${API_URL}/addressdatail`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail);
    }
    return result;
};

// Edit Address Response
export const responseEditAddressAPI = async (id) => {
    const response = await fetch(`${API_URL}/edit_address_response/${id}`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail);
    }
    return result;
};

// Edit Address
export const editAddressAPI = async (payload, id) => {
    const response = await fetch(`${API_URL}/edit_address/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail);
    }
    return result;
};

// Delete Address Response
export const responseDeleteAddress = async (id) => {
    const response = await fetch(`${API_URL}/delete_address_response/${id}`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail);
    }
    return result;
}

// Delete Address
export const deleteAddressAPI = async (id) => {
    const response = await fetch(`${API_URL}/delete_address/${id}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        credentials: "include"
    });
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail);
    }
    return result;
};