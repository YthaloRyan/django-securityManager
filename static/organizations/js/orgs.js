import { httpGet } from '/static/js/utils.js';

function activateById(id) {
    const navLinks = document.getElementsByClassName('orgs');
    for (let i = 0; i < navLinks.length; i++) {
        navLinks[i].classList.remove('activated');
    }

    document.getElementById(id).classList.add('activated');
}


window.getOrg = async function (theUrl, id) {
    const data = await httpGet(theUrl);

    activateById(id);

    document.querySelector('.org-table').innerHTML = data;
}