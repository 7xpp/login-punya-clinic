import { responseAddressAPI } from "../../api(JS)/address.js";

// Response address
const ResponseAddress = async () => {

    const container = document.querySelector("#response-address");
    const createcontainer = document.querySelector("#create-address");
    if (!container) return;

    try {
        const result = await responseAddressAPI();
        const dataaddress = result.data;

        if (!dataaddress || dataaddress.length === 0) {
            createcontainer.hidden = true;
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

        let htmlContent ="";

        dataaddress.forEach((item) => {
            htmlContent += `
                <div class="p-3 rounded-3 border mb-3 mt-3">
                    <div class="d-flex justify-content-end gap-2">
                        <a href="editaddress.html?id=${item.id}" class="text-decoration-none d-flex justify-content-end"><button class="btn btn1-custom small" style="cursor: pointer;"><p class="small mb-0 ">แก้ไข</p></button></a>
                        <div class="d-flex justify-content-end me-2">
                            <button type="button" class="btn btn3-custom" data-bs-toggle="modal" data-bs-target="#deletemodal"><p class="small mb-0">ลบ</p></button>
                        </div>
                    </div>
                    <div class="d-flex align-items-start">
                        <div class="d-flex flex-column mb-0">
                            <div class="d-flex align-items-center gap-2 mb-1">
                                <p class="fw-bold fs-6 text-dark mb-0">${item.name}</p>
                                <p class="text-muted fs-6 mb-0">|</p>
                                <p class="text-muted fs-6 mb-0"">${item.tel}</p>
                            </div>
                            <div class="border-top mt-2 pt-2 d-flex flex-column justify-content-start text-start">
                                <p class="text-secondary mb-0 small pt-2">${item.address}</p>
                                <p class="text-secondary mb-0 small pb-0">${item.address_detail}</p>
                                <p class="text-orange fw-light small mt-3 pb-0 mb-0 border-top pt-2">${item.is_default ? "ที่อยู่หลัก" : ""}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="modal fade" id="deletemodal" tabindex="-1">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content rounded-4">

                            <div class="modal-header">
                                <h5 class="modal-title">ต้องการลบข้อมูลใช่ไหม</h5>
                            </div>
                            <div class="modal-header">
                                <p class="text-gray">ถ้าคุณลบแล้วจะไม่สามารถกู้คืนได้</p>
                            </div>
                            <div class="modal-footer d-flex justify-content-end">
                                <button class="btn btn1-custom" data-bs-dismiss="modal">ยกเลิก</button>
                                <a href="deleteaddress.html?id=${item.id}" class="btn btn2-custom">ลบ</a>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        });

        container.innerHTML = htmlContent;
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

ResponseAddress();