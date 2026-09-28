import { signedUrlAPI, repairAPI } from "../api(JS)/user.js";

// Repair
export const ServiceRepair = async (cleandata, imgInput, submitbtn) => {

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

        const file = Array.from(imgInput.files);
        if (file.length === 0) {
            throw new Error("กรุณาเลือกรูปภาพ");
        }

        const fileList = file.map(file => ({
            file_name: file.name,
            file_type: file.type
        }));

        const signedresult = await signedUrlAPI(fileList);

        const uploadFileInSupabase = signedresult.data.map(async (item, index) => {

            const matchedFile = file[index];

            const uploadToSupabase = await fetch(item.signed_url, {
                method: "PUT",
                headers: { "Content-type": matchedFile.type },
                body: matchedFile
            });
            if (!uploadToSupabase.ok) { throw new Error("เกิดข้อผิดพลาดในการอัพโหลดไฟล์"); }
        })

        await Promise.all(uploadFileInSupabase);

        const allPublicUrls = signedresult.data.map(item => item.public_url).join(",");

        const payload = {
            ...cleandata,
            img_url: allPublicUrls
        };

        const result = await repairAPI(payload);
        setbtn(false);
        return result;
    }

    catch (error) {
        setbtn(false);
        throw error;
    }
};