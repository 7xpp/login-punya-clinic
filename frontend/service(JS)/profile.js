import { addressAPI } from "../api(JS)/address.js";

// Create Address
export const ServiceAddressRepair = async (cleandata, submitbtn) => {

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
        const result = await addressAPI(cleandata);
        setbtn(false);
        return result;
      }
    
      catch (error) {
        setbtn(false);
        throw error;
      }
};