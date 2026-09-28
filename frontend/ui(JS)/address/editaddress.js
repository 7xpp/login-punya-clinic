import { responseEditAddressAPI } from "../../api(JS)/address.js";
import { ServiceEditAddress } from "../../service(JS)/address.js";

const urlParams = new URLSearchParams(window.location.search);
let addressId = urlParams.get("id");

//Response Address
const EditAddressForm = document.querySelector("#edit-address-form");

const EditAddressResponse = async () => {

    if (!EditAddressForm) return;

    try {
        const result = await responseEditAddressAPI(addressId);
        const dataaddress = result.data;

        if (!dataaddress) {
            Swal.fire({
                title: 'ไม่พบข้อมูล',
                text: 'ไม่พบข้อมูลที่อยู่ที่ต้องการแก้ไข',
                icon: 'error',
                confirmButtonText: 'ตกลง'
            });
            EditAddressForm.name.disabled = true;
            EditAddressForm.tel.disabled = true;
            EditAddressForm.address.disabled = true;
            EditAddressForm.address_detail.disabled = true;
            window.location.href = "responseaddress.html";
        }

        EditAddressForm.name.value = dataaddress.name;
        EditAddressForm.tel.value = dataaddress.tel;
        EditAddressForm.address.value = dataaddress.address;
        EditAddressForm.address_detail.value = dataaddress.address_detail;
        if (dataaddress.is_default === true){
            EditAddressForm.is_default.checked = true;
            EditAddressForm.is_default.disabled = true;
        }
    }

    catch (error) {
        Swal.fire({
            title: 'เกิดข้อผิดพลาด!',
            text: error.message,
            icon: 'error',
            confirmButtonText: 'ตกลง'
        });
        EditAddressForm.name.disabled = true;
        EditAddressForm.tel.disabled = true;
        EditAddressForm.address.disabled = true;
        EditAddressForm.address_detail.disabled = true;
        EditAddressForm.is_default.disabled = true;
        window.location.href = "responseaddress.html";
    }
};

// Edit address
if (EditAddressForm) {
    EditAddressForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector('button[type="submit"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        const cleandata = {
            name: data.name.trim(),
            tel: data.tel.trim(),
            address: data.address.trim(),
            address_detail: data.address_detail.trim(),
            is_default: data.is_default
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

        if (!addressId) {
            Swal.fire({
                title: 'เกิดข้อผิดพลาด',
                text: 'ไม่พบข้อมูลที่อยู่ที่ต้องการแก้ไข',
                icon: 'error',
                confirmButtonText: 'ตกลง'
            });
            return;
        }

        try {
            await ServiceEditAddress(cleandata, addressId, submitbtn);
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'แก้ไขที่อยู่สำเร็จ',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "responseaddress.html";
        }

        catch (error) {
            Swal.fire({
                title: 'เกิดข้อผิดพลาด',
                text: error.message,
                icon: 'error',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "responseaddress.html";
        }
    });
}

EditAddressResponse();