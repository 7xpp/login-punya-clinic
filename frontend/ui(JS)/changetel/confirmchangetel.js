import { CreateResetTelOTPAgainAPI} from "../../api(JS)/changetel.js";
import { ServiceResetTel } from "../../service(JS)/changetel.js";

// Create OTP Again
const CreateResetTelOTPAgain = document.querySelector("#creatteleotpagain");

if (CreateResetTelOTPAgain) {
    CreateResetTelOTPAgain.addEventListener("click", async (event) => {
        event.preventDefault();

        try {
            await CreateResetTelOTPAgainAPI();
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
const ConfirmResetTelFrom = document.querySelector("#confirm-reset-tel-form");

if (ConfirmResetTelFrom) {
    ConfirmResetTelFrom.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            otp: data.otp.trim()
        };

        try {
            await ServiceResetTel(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'เปลี่ยนอีเมลสำเร็จ',
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