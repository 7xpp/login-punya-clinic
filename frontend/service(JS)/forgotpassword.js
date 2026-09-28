import { CheckOTPAPI } from "../api(JS)/forgotpassword.js";
import { ConfirmPasswordAPI } from "../api(JS)/forgotpassword.js";

// Check OTP
export const ServiceCheckOTP = async (cleandata, submitbtn) => {

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
    const result = await CheckOTPAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};


// Confirm Password
export const ServiceConfirmPassword = async (cleandata, submitbtn) => {

  if (cleandata.password !== cleandata.confirmpassword) {
    throw new Error("รหัสผ่านไม่ตรงกัน");
  }

  const setbtn = (btnloading) => {

    if (!submitbtn) return;

    submitbtn.disabled = btnloading;
    submitbtn.style.pointerEvents = btnloading ? "none" : "auto";

    if (btnloading) {
      submitbtn.dataset.originalText = submitbtn.textContent;
      submitbtn.textContent = "Loading...";
    }

    else { submitbtn.textContent = submitbtn.dataset.originalText || "ยืนยัน"; }
  };

  try {
    setbtn(true);
    const result = await ConfirmPasswordAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};