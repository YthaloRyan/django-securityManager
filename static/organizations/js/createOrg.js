import { httpGet, formListener } from '/static/js/utils.js';



window.getCreateOrgForm = async function (theUrl) {
    const elements = document.querySelectorAll('.org-link.activated');

    elements.forEach((element) => {
    if (element.id !== 'org-form') {
        element.classList.remove('activated');
    }
    });


    const data = await httpGet(theUrl);

    document.querySelector('.org-table').innerHTML = data;
    
    await formListener('orgForm', '.org-table');

    
}

window.addEventListener("load", async function() {
    const storage = 'orgForm-storage';
    if (localStorage.getItem(storage) === "true") {
        localStorage.removeItem(storage);

        getCreateOrgForm('/organizations/create_org/');
    }
});

