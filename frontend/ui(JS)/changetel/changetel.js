import { ServiceResetTelOTP } from "../../service(JS)/changetel.js";

const ResetTelFrom = document.querySelector("#reset-tel-form");

if (ResetTelFrom) {
    ResetTelFrom.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            password: data.password.trim(),
            tel: data.tel.trim()
        };

        try {
            await ServiceResetTelOTP(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'รหัส OTP ส่งไปยังอีเมลของคุณแล้ว',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "../changetel/confirmchangetel.html"
            form.reset();
        }

        catch (error) {
            Swal.fire({
                title: 'เกิดข้อผิดพลาด',
                text: error.message,
                icon: 'error',
                confirmButtonText: 'ลองใหม่'
            });
        }
    });
}