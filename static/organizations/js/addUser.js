import { httpGet, formListener } from '/static/js/utils.js';


window.getAddUserForm = async function (theUrl, org) {
    const data = await httpGet(theUrl);
    
    localStorage.setItem('globalOrg', org);

    document.querySelector('.org-table').innerHTML = data;
    
    await formListener('addUserForm', '.org-table', false);
}

