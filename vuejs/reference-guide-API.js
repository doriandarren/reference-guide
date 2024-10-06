
/************************************************
 * 
 *  Fetch
 * 
 ************************************************/

/*


 - fetch es una llamada y solo se usa para leer archivos y en especial consultar API's
 - En la llamada se envia la URL de la API a consultar
 
 - El primer ".then()" es una llamada y dentro se envia una "arrow function". Aqui se convierte la respuesta de string a JSON. Recibe un argunmento y retorna ese argumento en formato JSON

 - El segundo ".then()" es una llamada y dentro se envia una "arrow function". Aqui se procesa la respuesta del API convertida en JSON en el primer ".then()" y aqui es donde se procesa el objeto de respuesta obtenida del API. Por ejemplo la variable "data" se puede procesar los objetos que vienen dentro de el; data.Data, donde "Data" es un valor que viene dentro del objeto "data"

 - El ".catch()" es una llamada y dentro se envia una "arrow function". Aqui solamente se obtiene el error al intentar conectarse o procesar la información hacia el API.

*/


// Ex.

fetch('https://min-api.cryptocompare.com/data/top/mktcapfull?limit=20&tsym=USD')
    .then( respuesta => respuesta.json() )
    .then( data => {
        console.log(data.Data);
        console.log(data.Message);
    })
    .catch((err) => {
        console.log(err);
    });

