import { ResponseRepairAPI, CancelRepairAPI } from "../../api(JS)/profile.js";
import { CreateOTPAPI } from "../../api(JS)/forgotpassword.js";

// Response Repair
const ResponseRepair = async () => {
    const container = document.querySelector("#repair-response");
    if (!container) return;
    try {
        const result = await ResponseRepairAPI();
        const repairList = result.data;
        if (!repairList || repairList.length === 0) {
            container.innerHTML = `
                <div class="card border-0 w-100 rounded-5 bg-custom">
                    <div class="card-body pt-3 pb-3">
                        <div class="d-flex-column justify-content-center">
                            <i class="fa-solid fa-plus text-gray"></i>
                            <p class="small text-gray mt-2">ยังไม่มีข้อมูลการซ่อม</p>
                        </div>
                    </div>
                </div>
            `;
            return;
        }
        let htmlContent = "";
        repairList.forEach((item, index) => {
            const defaultImg = "../../frontend(img)/S__23076867.jpg";
            const rawImg = (item.img_url && item.img_url.trim() !== "") 
                ? item.img_url.split(",")[0].trim() 
                : defaultImg;

            const modalId = `cancelModal-${index}`;
            htmlContent += `
                <div class="card border-0 w-100 rounded-5 bg-custom mt-3">
                    <div class="card-body pt-0">
                        <div class="d-flex justify-content-end mt-3 me-2">
                            <button type="button" class="btn btn3-custom" data-bs-toggle="modal" data-bs-target="#${modalId}"><p class="small mb-0">ยกเลิกส่งซ่อม</p></button>
                        </div>
                        <div class="d-flex flex-wrap gap-3 mb-1 text-start">
                            <div class="d-flex-column">
                                <p class="small text-gray mb-0">ยี่ห้อ : ${item.brand}</p>
                                <p class="small text-gray mb-0">อาการ : ${item.problem}</p>
                                <p class="small text-gray mb-0">วันที่ส่งซ่อม : ${new Date(item.created_at).toLocaleDateString("th-TH")}</p>
                                <p class="text-orange fs-6 fw-bold mb-0 mt-3">สถานะ : ${item.status}</p>
                            </div>
                        </div>
                        <div class="d-flex flex-column mb-0">
                            <div class="d-flex align-items-center gap-2 mb-1 mt-4">
                                <p class="fw-bold fs-6 text-dark mb-0">${item.name || ""}</p>
                                <p class="text-muted fs-6 mb-0">|</p>
                                <p class="text-muted fs-6 mb-0">${item.tel || ""}</p>
                            </div>
                            <div class="d-flex flex-column justify-content-start text-start">
                                <p class="text-secondary mb-0 small pt-2">${item.address || ""}</p>
                                <p class="text-secondary mb-0 small pb-0">${item.address_detail || ""}</p>
                            </div>
                            <div class="d-flex flex-column text-end me-3">
                                <h4 class="text-dark mb-0 pt-2">${item.price || ""}</h4>
                            </div>
                        </div>

                        <div class="modal fade" id="${modalId}" tabindex="-1">
                            <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content rounded-4">
                                    <div class="modal-header">
                                        <h5 class="modal-title">ต้องการยกเลิกใช่ไหม</h5>
                                    </div>
                                    <div class="modal-footer d-flex justify-content-end">
                                        <button class="btn btn1-custom" data-bs-dismiss="modal">ยกเลิก</button>
                                        <button type="button" class="btn btn2-custom btn-cancel-repair" data-repair-id="${item.id}" data-modal-id="${modalId}">ยืนยัน</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            `;
        });

        container.innerHTML = htmlContent;

        container.querySelectorAll(".btn-cancel-repair").forEach((btn) => {
            btn.addEventListener("click", async () => {
                const repairId = btn.dataset.repairId;
                const modalId = btn.dataset.modalId;

                try {
                    await CancelRepairAPI(repairId);

                    const modalEl = document.querySelector(`#${modalId}`);
                    if (modalEl && window.bootstrap) {
                        const modalInstance = bootstrap.Modal.getInstance(modalEl);
                        if (modalInstance) modalInstance.hide();
                    }

                    await Swal.fire({
                        title: 'สำเร็จ!',
                        text: 'ยกเลิกรายการซ่อมสำเร็จ',
                        icon: 'success',
                        confirmButtonText: 'ตกลง'
                    });

                    ResponseRepair();

                } catch (error) {
                    Swal.fire({
                        title: 'เกิดข้อผิดพลาด!',
                        text: error.message,
                        icon: 'error',
                        confirmButtonText: 'ลองใหม่'
                    });
                }
            });
        });
    }
    catch (error) {
        console.error("Error fetching repair data:", error);
        container.innerHTML = `<p class="text-danger small">${error.message}</p>`;

// Response address
const ResponseRepair = async () => {

    const container = document.querySelector(".repair-response");
    if (!container) return;

    try {
        const result = await getRepairResponseAPI();
        const repairList = result.data;

        if (!repairList || repairList.length === 0) {
            container.innerHTML = `
                <div class="card border-0 w-100 rounded-5 bg-custom">
                    <div class="card-body pt-3 pb-3">
                        <div class="d-flex-column justify-content-center">
                            <i class="fa-solid fa-plus text-gray"></i>
                            <p class="small text-gray mt-2">ยังไม่มีข้อมูลที่อยู่</p>
                            <a href="createaddress.html" class="btn btn1-custom"><p class="small mt-0 mb-0">+ เพิ่มที่อยู่</p></a>
                        </div>
                    </div>
                </div>
            `;
            return;
        }

        let htmlContent = "";

        repairList.forEach((item, index) => {
            const imgSrc = item.img_url ? item.img_url.split(",")[0] : "../frontend(img)/S__23076867.jpg";
            const modalId = `cancelModal-${index}`;

            htmlContent += `
                <div class="card border-0 w-100 rounded-5 bg-custom mt-3">
                        <div class="card-body pt-0">
                            <div class="d-flex justify-content-end mt-3 me-2">
                            <button type="button" class="btn btn3-custom" data-bs-toggle="modal" data-bs-target="#${modalId}"><p class="small mb-0">ยกเลิก</p></button>
                            </div>

                            <div class="d-flex flex-wrap gap-3 mb-1 text-start">
                            <img src="${imgSrc}" class="rounded-3" style="max-width: 120px; max-height: 120px; object-fit: cover;">
                                <div class="d-flex-column">
                                <p class="small text-gray mb-0">ยี่ห้อ : ${item.brand}</p>
                                <p class="small text-gray mb-0">อาการ : ${item.problem}</p>
                                <p class="small text-gray mb-0">วันที่ส่งซ่อม : ${new Date(item.created_at).toLocaleDateString("th-TH")}</p>
                                <p class="text-orange fs-6 fw-bold mb-0 mt-3">สถานะ : ${item.status}</p>
                                </div>
                            </div>
                            <div class="d-flex flex-column mb-0">
                                <div class="d-flex align-items-center gap-2 mb-1 mt-4">
                                <p class="fw-bold fs-6 text-dark mb-0">${item.name || ""}</p>
                                    <p class="text-muted fs-6 mb-0">|</p>
                                <p class="text-muted fs-6 mb-0">${item.tel || ""}</p>
                                </div>
                                <div class="d-flex flex-column justify-content-start text-start">
                                <p class="text-secondary mb-0 small pt-2">${item.address || ""}</p>
                                <p class="text-secondary mb-0 small pb-0">${item.address_detail || ""}</p>
                                </div>
                                <div class="d-flex flex-column text-end me-3">
                                <h4 class="text-dark mb-0 pt-2">${item.price || ""}</h4>
                            </div>
                        </div>
                        <div class="modal fade" id="${modalId}" tabindex="-1">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content rounded-4">
                                <div class="modal-header">
                                    <h5 class="modal-title">ต้องการลบข้อมูลใช่ไหม</h5>
                                </div>
                                <div class="modal-footer d-flex justify-content-end">
                                        <button class="btn btn1-custom" data-bs-dismiss="modal">ยกเลิก</button>
                                        <button type="button" class="btn btn2-custom btn-cancel-repair" data-repair-id="${item.id}" data-modal-id="${modalId}">ยืนยัน</button>
                                    </div>
                            </div>
                        </di    v>
                    </di    v>
                        </div>
                        </div>
                    </div>
            `;
        });

        container.innerHTML = htmlContent;

        // ผูก Event ให้ปุ่มยกเลิกทุกปุ่ม
        container.querySelectorAll(".btn-cancel-repair").forEach((btn) => {
            btn.addEventListener("click", async () => {
                const repairId = btn.dataset.repairId;
                const modalId = btn.dataset.modalId;

                try {
                    await cancelRepairAPI(repairId);

                    // ปิด Modal
                    const modalEl = document.querySelector(`#${modalId}`);
                    if (modalEl && window.bootstrap) {
                        const modalInstance = bootstrap.Modal.getInstance(modalEl);
                        if (modalInstance) modalInstance.hide();
                    }

                    await Swal.fire({
                        title: 'สำเร็จ!',
                        text: 'ยกเลิกรายการซ่อมสำเร็จ',
                        icon: 'success',
                        confirmButtonText: 'ตกลง'
                    });

                    // โหลดข้อมูลใหม่
                    repairResponse();

                } catch (error) {
                    Swal.fire({
                        title: 'เกิดข้อผิดพลาด!',
                        text: error.message,
                        icon: 'error',
                        confirmButtonText: 'ลองใหม่'
                    });
                }
            });
        });
    }
    catch (error) {
        console.error("Error fetching repair data:", error);
        container.innerHTML = `<p class="text-danger small">${error.message}</p>`;
    }
};

repairResponse();
erHTML = `<p class="text-danger small">${error.message}</p>`; 
    }
};

ResponseRepair();

// Create OTP
const CreateOTP = document.querySelector("#forgot-password");

if (CreateOTP) {
    CreateOTP.addEventListener("click", async (event) => {
        event.preventDefault();

        try {
            await CreateOTPAPI();
            await Swal.fire({
                title: 'สำเร็จ',
                text: 'ส่ง OTP สำเร็จ',
                icon: 'success',
                confirmButtonText: 'ตกลง'
            });
            window.location.href = "../forgotpassword/forgotpasswordotp.html"
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