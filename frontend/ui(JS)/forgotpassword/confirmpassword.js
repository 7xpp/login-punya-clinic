import { ServiceConfirmPassword } from "../../service(JS)/forgotpassword.js";

// ConfirmPassword
const ConfirmForgotPassword = document.querySelector("#confirm-fotgot-password-form");

if (ConfirmForgotPassword) {
    ConfirmForgotPassword.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            password: data.password,
            confirmpassword: data.confirmpassword
        };

        try {
            await ServiceConfirmPassword(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'เปลี่ยนรหัสผ่านสำเร็จ',
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