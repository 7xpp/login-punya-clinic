import { CreateOTPAgainAPI } from "../../api(JS)/forgotpassword.js";
import { ServiceCheckOTP } from "../../service(JS)/forgotpassword.js";

// Create OTP Again
const CreateOTPAgain = document.querySelector("#createotpagain");

if (CreateOTPAgain) {
    CreateOTPAgain.addEventListener("click", async (event) => {
        event.preventDefault();

        try {
            await CreateOTPAgainAPI();
            Swal.fire({
                title: 'สำเร็จ',
                text: 'ส่ง OTP สำเร็จ',
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
const ConfirmForgotPassword = document.querySelector("#forgot-password-form");

if (ConfirmForgotPassword) {
    ConfirmForgotPassword.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            otp: data.otp.trim()
        };

        try {
            await ServiceCheckOTP(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'OTP ถูกต้อง',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "confirmforgotpassword.html"
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