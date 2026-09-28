import { deleteAddressAPI, responseDeleteAddress } from "../../api(JS)/address.js";

const urlParams = new URLSearchParams(window.location.search);
let addressId = urlParams.get("id");

const DeleteAddress = async () => {

    const container = document.querySelector("#delete-address");
    if (!container) return;

    try {
        const result = await responseDeleteAddress(addressId);
        const dataaddress = result.data;

        if (!dataaddress) {
            Swal.fire({
                title: 'ไม่พบข้อมูล',
                text: 'ไม่พบข้อมูลที่อยู่ที่ต้องการลบ',
                icon: 'error',
                confirmButtonText: 'ตกลง'
            });
            container.innerHTML = `<p class="text-danger small">ไม่พบข้อมูลที่อยู่</p>`;
            return;
        }

        if (!addressId) addressId = dataaddress.id;

        await deleteAddressAPI(addressId);
        Swal.fire({
            title: 'สำเร็จ',
            text: 'ลบที่อยู่เรียบร้อยแล้ว',
            icon: 'success',
            confirmButtonText: 'ตกลง'
        });

        container.innerHTML = `
            <div class="card border border-danger w-100 rounded-5">
                <div class="card-body pt-3 pb-0">
                    <div class="d-flex-column mb-1 text-start">
                        <p class="fs-6 fw-medium text-danger">${dataaddress.name}</p>
                        <p class="small text-danger">${dataaddress.tel}</p>
                    </div>
                    <div class="d-flex-column mb-1 mt-4 text-start pt-3 border-top border-danger">
                        <p class="fs-6 fw-medium text-danger">${dataaddress.address}</p>
                        <p class="small text-danger">${dataaddress.address_detail}</p>
                    </div>
                </div>
            </div>
            <a href="../main/user.html" class="btn btn1-custom w-75 mt-5 mb-2">กลับไปยังหน้าแรก</a>
        `;
    }

    catch (error) {
        Swal.fire({
            title: 'เกิดข้อผิดพลาด',
            text: error.message,
            icon: 'error',
            confirmButtonText: 'ตกลง'
        });
        container.innerHTML = `<p class="text-danger small">${error.message}</p>`; 
    }
};

DeleteAddress();