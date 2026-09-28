import { ServiceChangePassword } from "../../service(JS)/changepassword.js";

const changePasswordFrom = document.querySelector("#change-password-form");

if (changePasswordFrom) {
    changePasswordFrom.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            password: data.password
        };
        try {
            await ServiceChangePassword(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'รหัสผ่านถูกต้อง',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "confirmchangepassword.html";
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