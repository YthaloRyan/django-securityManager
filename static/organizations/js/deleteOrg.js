function getCSRFToken() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}



window.deleteOrg = async function (org)  {
    if (!confirm("Are you sure you want to delete this item?")) {
        return;
    }

    await fetch(`/organizations/delete_org/${org}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            console.log(Error);
            throw new Error("Error deleting item.");
        }
    })
    .then(data => {
        console.log(data.message);
        alert("Item deleted successfully!");
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("An error occurred while deleting the item.");
    });

    location.reload();
}


