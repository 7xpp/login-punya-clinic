import { changepasswordAPI } from "../api(JS)/changepassword.js";
import { confirmchangepasswordAPI } from "../api(JS)/changepassword.js";

export const ServiceChangePassword = async (cleandata, submitbtn) => {

    const setbtn = (btnloading) => {

        if (!submitbtn) return;

        submitbtn.disabled = btnloading;
        submitbtn.style.pointerEvent = btnloading ? "none" : "auto";

        if (btnloading) {
            submitbtn.dataset.originalText = submitbtn.textContent;
            submitbtn.textContent = "Loading...";
        }

        else { submitbtn.textContent = submitbtn.dataset.originalText || "ถัดไป"; }
    }

    try {
        setbtn(true);
        const result = await changepasswordAPI(cleandata);
        setbtn(false);
        return result;
    }
    catch (error) {
        setbtn(false);
        throw error;
    }
};

export const ServiceConfirmPassword = async (cleandata, submitbtn) => {

    const setbtn = (btnloading) => {

        if (!submitbtn) return;

        submitbtn.disabled = btnloading;
        submitbtn.style.pointerEvent = btnloading ? "none" : "auto";

        if (btnloading) {
            submitbtn.dataset.originalText = submitbtn.textContent;
            submitbtn.textContent = "Loading...";
        }

        else { submitbtn.textContent = submitbtn.dataset.originalText || "ยืนยัน"; }
    }

    try {
        setbtn(true);
        const result = await confirmchangepasswordAPI(cleandata);
        setbtn(false);
        return result;
    }
    catch (error) {
        setbtn(false);
        throw error;
    }
};