import { httpDelete } from '/static/js/utils.js';


window.deleteUser = async function (org, user)  {
    localStorage.setItem('globalOrg', org);
    
    httpDelete(`remove_user/${org}/${user}`);
}