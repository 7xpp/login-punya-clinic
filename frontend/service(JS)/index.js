import { signupAPI } from "../api(JS)/index.js"
import { loginAPI } from "../api(JS)/index.js"

// Signup
export const ServiceSignup = async (cleandata, submitbtn) => {

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

    else { submitbtn.textContent = submitbtn.dataset.originalText || "สมัครสมาชิก"; }
  };

  try {
    setbtn(true);
    const result = await signupAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};

// Login
export const ServiceLogin = async (cleandata, submitbtn) => {

  const setbtn = (btnloading) => {

    if (!submitbtn) return;

    submitbtn.disabled = btnloading;
    submitbtn.style.pointerEvents = btnloading ? "none" : "auto";

    if (btnloading) {
      submitbtn.dataset.originalText = submitbtn.textContent;
      submitbtn.textContent = "Loading...";
    }

    else { submitbtn.textContent = submitbtn.dataset.originalText || "เข้าสู่ระบบ"; }
  };

  try {
    setbtn(true);
    const result = await loginAPI(cleandata);
    setbtn(false);
    return result;
  }

  catch (error) {
    setbtn(false);
    throw error;
  }
};