import { ServiceSignup } from "../../service(JS)/index.js";
import { ServiceLogin } from "../../service(JS)/index.js";

// Signup
const SignupForm = document.querySelector("#signup-form");
const signupModal = new bootstrap.Modal("#signupmodal");
const loginsModal = new bootstrap.Modal("#loginmodal");

if (SignupForm) {
    SignupForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            email: data.email.trim(),
            password: data.password.trim(),
            confirmpassword: data.confirmpassword.trim(),
            tel: data.tel.trim(),
            username: data.username.trim()
        };

        try {
            await ServiceSignup(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'สมัครสมาชิกสำเร็จ',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            form.reset();
            signupModal.hide();
            loginsModal.show();
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

// Login
const LoginForm = document.querySelector("#login-form");

if (LoginForm) {
    LoginForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            email: data.email.trim(),
            password: data.password.trim()
        };

        try {
            await ServiceLogin(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'เข้าสู่ระบบสำเร็จ',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location = "../main/user.html";
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
    })
}

// Repair
const repairwatchmodal = document.querySelector("#watchcard");
const repairremotemodal = document.querySelector("#remotecard");
const repairmodal = document.querySelector("#repaircard");
const repairautomodal = document.querySelector("#autowatchcard");

if (repairwatchmodal) {
    repairwatchmodal.addEventListener("click", () => {
        Swal.fire({
            title: 'ต้องเข้าสู่ระบบ',
            text: "กรุณาเข้าสู่ระบบเพื่อใช้บริการนี้",
            icon: 'error',
            confirmButtonText: 'ตกลง'
        });
    });
}

if (repairremotemodal) {
    repairremotemodal.addEventListener("click", () => {
        Swal.fire({
            title: 'ต้องเข้าสู่ระบบ',
            text: "กรุณาเข้าสู่ระบบเพื่อใช้บริการนี้",
            icon: 'error',
            confirmButtonText: 'ตกลง'
        });
    });
}

if (repairmodal) {
    repairmodal.addEventListener("click", () => {
        Swal.fire({
            title: 'ต้องเข้าสู่ระบบ',
            text: "กรุณาเข้าสู่ระบบเพื่อใช้บริการนี้",
            icon: 'error',
            confirmButtonText: 'ตกลง'
        });
    });
}

if (repairautomodal) {
    repairautomodal.addEventListener("click", () => {
        Swal.fire({
            title: 'ต้องเข้าสู่ระบบ',
            text: "กรุณาเข้าสู่ระบบเพื่อใช้บริการนี้",
            icon: 'error',
            confirmButtonText: 'ตกลง'
        });
    });
}