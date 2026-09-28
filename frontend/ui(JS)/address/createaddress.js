import { ServiceCreateAddress } from "../../service(JS)/address.js";

// Create address
const CreateAddressForm = document.querySelector("#create-address-form");

if (CreateAddressForm) {
    CreateAddressForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            name: data.name.trim(),
            tel: data.tel.trim(),
            address: data.address.trim(),
            address_detail: data.address_detail.trim()
        };

        if (!cleandata.name || !cleandata.tel || !cleandata.address || !cleandata.address_detail) {
            Swal.fire({
                title: 'เกิดข้อผิดพลาด',
                text: 'กรุณากรอกข้อมูลให้ครบถ้วน',
                icon: 'error',
                confirmButtonText: 'ตกลง'
            });
            return;
        }

        try {
            await ServiceCreateAddress(cleandata, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'เพิ่มที่อยู่สำเร็จ',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "responseaddress.html";
            form.reset();
        }

        catch (error) { 
            Swal.fire({
                title: 'เกิดข้อผิดพลาด',
                text: error.message,
                icon: 'error',
                confirmButtonText: 'ตกลง'
            });
        }
    });
}