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