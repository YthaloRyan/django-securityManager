import { httpGet } from '/static/js/utils.js';

const org_url = '/organizations/users/'; 

function activateById(id) {
    const navLinks = document.getElementsByClassName('orgs');
    for (let i = 0; i < navLinks.length; i++) {
        navLinks[i].classList.remove('activated');
    }

    document.getElementById(id).classList.add('activated');
}



window.getOrg = async function (org) {
    const data = await httpGet(`${org_url}${org}`);

    activateById(org);

    document.querySelector('.org-table').innerHTML = data;
}


window.addUserBack = async function (org) {
    getOrg(org);

    
}