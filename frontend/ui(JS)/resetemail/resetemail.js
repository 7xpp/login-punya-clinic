import { ServiceResetEmailOTP } from "../../service(JS)/resetemail.js";

const ResetEmailFrom = document.querySelector("#reset-email-form");

if (ResetEmailFrom) {
    ResetEmailFrom.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            password: data.password.trim(),
            email: data.email.trim()
        };

        try {
            await ServiceResetEmailOTP(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'รหัส OTP ส่งไปยังอีเมลของคุณแล้ว',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "../resetemail/confirmresetemail.html"
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