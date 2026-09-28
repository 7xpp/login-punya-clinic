import { CreateResetEmailOTPAgainAPI} from "../../api(JS)/resetemail.js";
import { ServiceResetEmail } from "../../service(JS)/resetemail.js";

// Create OTP Again
const CreateResetEmailOTPAgain = document.querySelector("#creatresetemaileotpagain");

if (CreateResetEmailOTPAgain) {
    CreateResetEmailOTPAgain.addEventListener("click", async (event) => {
        event.preventDefault();

        try {
            await CreateResetEmailOTPAgainAPI();
            Swal.fire({
                title: 'สำเร็จ',
                text: 'รหัส OTP ส่งไปยังอีเมลของคุณแล้ว',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
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

// Check OTP
const ConfirmResetEmailFrom = document.querySelector("#confirm-reset-email-form");

if (ConfirmResetEmailFrom) {
    ConfirmResetEmailFrom.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            otp: data.otp.trim()
        };

        try {
            await ServiceResetEmail(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'เปลี่ยนเบอร์โทรศัพท์สำเร็จ',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "../main/user.html"
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