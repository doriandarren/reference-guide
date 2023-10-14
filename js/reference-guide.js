//creacion de variables
export var variableVar;            // es la más antigua
let variableLet;            // sustituye a la var
const variableConst = 'Valor Predefinido';   // Es la más usada



//asignación de variables
variableVar = 'Hola';
variableLet = 'Mundo';
const variableConstAsignada = 'Hello';

//Vuejs
// const variable = ref('');   // Declaracion 
// variable.value = 30;        // Asignación


// Creación de un arreglo o array
let arrayNumero = [];                       //array vacio
let arrayNumeroLleno = [20, 30, 40, 50];    // array con valores



//Creación de objetos
let objetoCarro = {};  //objeto vacio

let objetoCarroLleno = {  //objeto con valores
    color: 'Blanco',
    marca: 'Fiat',
    puertas: 4
};  


//Array de objetos
let arrayObjetos = [{}]; //array objetos vacios


let arrayObjetosLlenos = [//array vacio
    {
        color:'Blanco',
        marca: 'Palio',
        puertas: 4
    },
    {
        color: 'Verde',
        marca: 'Chevrolet',
        puertas: 5
    },
];

//console.log(arrayObjetosLlenos[0]);


//Array dentro de Objetos

let objectoMesa = {
    medidas: [20, 30, 40],
    niveles: [1, 2, 3],
    color: 'Negro'
};

console.log(objectoMesa);


//crear metodo o funcion
function nombreFuncion(nombre, apellido){ // argumentos
    //Aqui en código
}


//crear metodo flecha
const nombreFuncionFlecha = (nombre, apellido) => { // argumentos
    //Aqui en código
}



//Crear clase
class NombreClase{

    //aqui las propiedades
    nombre;

    constructor(){

    }

    //aqui los metodos o fuciones de clase

    nombreMetodo(){

    }

}

//Get y Set

let getVariable;  // coge el valor de la variable
let setVariable;  // almacena el valor de la variable


let variableGet = getVariable();
let variableSet = setVariable('Nuevo valor');





//bucles o iteradores

for(let i = 0; i < 10; i++){
    //TODO aqui va el código o la lógica 
}


let edad = 10;
while(edad < 18){
    //TODO aqui va el código o la lógica 

    edad++;
}


do{
    //TODO aqui va el código o la lógica 

    edad++;
}while(17 < 16);