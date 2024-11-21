import { httpDelete } from '/static/js/utils.js';


window.deleteOrg = async function (org)  {
    httpDelete(`delete_org/${org}`);
}