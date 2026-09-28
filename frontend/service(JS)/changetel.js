import { CreateResetTelOTPAPI } from "../api(JS)/changetel.js";
import { CheckResetTelOTPAPI } from "../api(JS)/changetel.js";

// Create OTP
export const ServiceResetTelOTP = async (cleandata, submitbtn) => {

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
    const result = await CreateResetTelOTPAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};

// Check OTP
export const ServiceResetTel = async (cleandata, submitbtn) => {

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
    const result = await CheckResetTelOTPAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};