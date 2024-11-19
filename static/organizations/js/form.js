import { httpGet } from '/static/js/utils.js';



async function formListener(){
    document.getElementById('orgForm').addEventListener('submit', async function (event) {
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
                localStorage.setItem("requestForm", "true");

                location.reload();
            } else {
                const errorData = await response.text();
                
                document.querySelector('.org-table').innerHTML = errorData;

                formListener();
            }
        } catch (error) {
            console.error('unexpected error:', error);
        }
    });
}


window.getForm = async function (theUrl) {
    const elements = document.querySelectorAll('.org-link.activated');

    elements.forEach((element) => {
    if (element.id !== 'org-form') {
        element.classList.remove('activated');
        console.log(`Classe 'activated' removida do elemento com ID: ${element.id}`);
    }
    });


    const data = await httpGet(theUrl);

    document.querySelector('.org-table').innerHTML = data;
    
    formListener();
}

window.addEventListener("load", async function() {
    if (localStorage.getItem("requestForm") === "true") {
        localStorage.removeItem("requestForm");

        getForm('/organizations/create_org');
    }
});