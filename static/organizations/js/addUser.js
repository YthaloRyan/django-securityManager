import { httpGet, formListener } from '/static/js/utils.js';


window.getAddUserForm = async function (theUrl, org) {
    const data = await httpGet(theUrl);

    document.querySelector('.org-table').innerHTML = data;
    
    await formListener('addUserForm', '.org-table', true, org);

    
}



