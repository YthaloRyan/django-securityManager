function getCSRFToken() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}



export async function httpGet(theUrl, id) {
    try {
        const response = await fetch(theUrl);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.text();
        
        return data;
    } catch (error) {
        console.error('Erro ao fazer a solicitação:', error);
    }
}

export async function httpDelete(theUrl)  {
    if (!confirm("Are you sure you want to delete this item?")) {
        return;
    }

    await fetch(theUrl, {
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

export async function formListener(id, inner_path, save = true, info = 'true'){
    document.getElementById(id).addEventListener('submit', async function (event) {
        event.preventDefault(); // Impede o envio padrão do formulário

    
        const form = event.target;
        const formData = new FormData(form);
    
        try {
            const response = await fetch(form.action, {
                method: form.method,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                },
                body: formData
            });
            
            
            if (response.ok) {
                if (save) {
                    localStorage.setItem(`${id}-storage`, info);
                }

                location.reload();
            } else {
                const errorData = await response.text();
                
                document.querySelector(inner_path).innerHTML = errorData;

                await formListener(id, inner_path);
            }
        } catch (error) {
            console.error('unexpected error:', error);
        }
    });
}


window.addEventListener("load", async function() {
    const addUserStorage = 'addUserForm-storage'

    if (localStorage.getItem(addUserStorage)) {
        const savedOrg = localStorage.getItem(addUserStorage);
        
        localStorage.removeItem(addUserStorage);

        const data = await httpGet(`/organizations/users/${savedOrg}`);
        document.querySelector('.org-table').innerHTML = data;  
    }
});