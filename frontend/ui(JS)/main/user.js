import { ServiceRepair } from "../../service(JS)/user.js";
import { repairAddressResponseAPI } from "../../api(JS)/user.js";

// Addrress Response
const addressRepairResponse = async () => {

    const container = document.querySelector("#address-response-repair");
    if (!container) return;

    try {
        const result = await repairAddressResponseAPI();
        const dataaddress = result.data;
    
        if (!dataaddress) {
            container.innerHTML = `
                <div class="card border-0 w-100 rounded-4 bg-custom text-center p-3 mb-3">
                    <div class="card-body py-2">
                        <i class="fa-solid fa-location-dot text-secondary fs-4 mb-2"></i>
                        <p class="small text-secondary mb-2">ยังไม่มีข้อมูลที่อยู่สำหรับจัดส่ง</p>
                        <a href="../address/createaddress.html" class="btn btn1-custom btn-sm">
                            <span class="small">+ เพิ่มที่อยู่</span>
                        </a>
                    </div>
                </div>
            `;
            return;
        }
        
        container.innerHTML = `
            <input type="hidden" name="address_id" value="${dataaddress.id}">
            <div class="p-3 rounded-3 border mb-3 mt-2">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <div class="d-flex align-items-center gap-2">
                        <span class="fw-bold small text-dark"><i class="fa-solid fa-location-dot me-1 text-gold"></i>ที่อยู่จัดส่ง</span>
                        ${dataaddress.is_default ? '<span class="badge text-bg-warning small" style="font-size: 0.75rem;">ที่อยู่หลัก</span>' : ''}
                    </div>
                    <div class="d-flex gap-2">
                        <a href="../address/editaddress.html?id=${dataaddress.id}" class="text-decoration-none">
                            <button type="button" class="btn btn1-custom btn-sm py-1 px-2" style="cursor: pointer;"><p class="small mb-0">แก้ไข</p></button>
                        </a>
                        <a href="../address/responseaddress.html" class="text-decoration-none">
                            <button type="button" class="btn btn1-custom btn-sm py-1 px-2" style="cursor: pointer;"><p class="small mb-0">เปลี่ยนที่อยู่</p></button>
                        </a>
                    </div>
                </div>
                <div class="d-flex align-items-start">
                    <div class="d-flex flex-column mb-0 w-100">
                        <div class="d-flex align-items-center gap-2 mb-1">
                            <p class="fw-bold fs-6 text-dark mb-0">${dataaddress.name}</p>
                            <p class="text-muted fs-6 mb-0">|</p>
                            <p class="text-muted fs-6 mb-0">${dataaddress.tel}</p>
                        </div>
                        <div class="border-top mt-2 pt-2 d-flex flex-column justify-content-start text-start">
                            <p class="text-secondary mb-0 small pt-1">${dataaddress.address}</p>
                            ${dataaddress.address_detail ? `<p class="text-secondary mb-0 small pb-0">${dataaddress.address_detail}</p>` : ''}
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    catch (error) {
        console.error("Error fetching repair address:", error);
    }
};

addressRepairResponse();

// Create Repair
const RepairForm = document.querySelector("#repair-form");

if (RepairForm) {
    RepairForm.addEventListener("submit", async(event) => {
        event.preventDefault();

        const form = event.currentTarget;
        const submitbtn = form.querySelector("button[type='submit']");
        const imgInput = form.querySelector('input[type="file"][name="image"]');

        const formdata = new FormData(form);
        const data = Object.fromEntries(formdata);

        if (!data.address_id) {
            const Swal = window.Swal;
            Swal.fire({
                title: 'กรุณาเลือกที่อยู่',
                text: 'ยังไม่มีข้อมูลที่อยู่จัดส่ง กรุณาเพิ่มหรือเลือกที่อยู่ก่อนส่งซ่อม',
                icon: 'warning',
                confirmButtonText: 'ตกลง'
            });
            return;
        }

        const cleandata = {
            brand: (data.brand || "").trim(),
            problem: (data.problem || "").trim(),
            address_id: data.address_id
        };

        try {
            await ServiceRepair(cleandata, imgInput, submitbtn);
            const Swal = window.Swal;
            Swal.fire({
                title: 'สำเร็จ!',
                text: 'ส่งซ่อมสำเร็จ',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            RepairForm.reset();

            const modalEl = document.querySelector("#repairmodal");
            if (modalEl && window.bootstrap) {
                const modalInstance = bootstrap.Modal.getInstance(modalEl);
                if (modalInstance) {
                    modalInstance.hide();
                }
            }
        }

        catch (error) {
            const Swal = window.Swal;
            Swal.fire({
                title: 'เกิดข้อผิดพลาด!',
                text: error.message,
                icon: 'error',
                confirmButtonText: 'ลองใหม่'
            });
        }
    });
}