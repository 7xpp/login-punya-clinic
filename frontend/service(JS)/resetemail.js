import { CreateResetEmailOTPAPI } from "../api(JS)/resetemail.js";
import { CheckResetEmailOTPAPI } from "../api(JS)/resetemail.js";

// Create OTP
export const ServiceResetEmailOTP = async (cleandata, submitbtn) => {

  const setbtn = (btnloading) => {

    if (!submitbtn) return;

    submitbtn.disabled = btnloading;
    submitbtn.style.pointerEvents = btnloading ? "none" : "auto";

    if (btnloading) {
      submitbtn.dataset.originalText = submitbtn.textContent;
      submitbtn.textContent = "Loading...";
    }

    else { submitbtn.textContent = submitbtn.dataset.originalText || "ถัดไป"; }
  };

  try {
    setbtn(true);
    const result = await CreateResetEmailOTPAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};

// Check OTP
export const ServiceResetEmail = async (cleandata, submitbtn) => {

  const setbtn = (btnloading) => {

    if (!submitbtn) return;

    submitbtn.disabled = btnloading;
    submitbtn.style.pointerEvents = btnloading ? "none" : "auto";

    if (btnloading) {
      submitbtn.dataset.originalText = submitbtn.textContent;
      submitbtn.textContent = "Loading...";
    }

    else { submitbtn.textContent = submitbtn.dataset.originalText || "ถัดไป"; }
  };

  try {
    setbtn(true);
    const result = await CheckResetEmailOTPAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};