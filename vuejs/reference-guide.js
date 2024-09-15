/************************************************
 * 
 *  VARIABLES
 * 
 ************************************************/

/**
Notas: 

Template: <template>...</template>

 - Cuando este presente un '@' hace referencia a una funcion. Ex: @click.prevent="unaFuncion"
 - Cuando este presente un ':' hace referencia a una variable. Ex: :src="unaVariable" / :unaVarible="unaVariable"
 - Cuando se use el "v-model" hace referencia a los input. Ex: <input v-model="nombre" />
 - Aquí NO SE UTILIZA el '.value' para las variables



Script: <script></script>





EMITS:

- En el PADRE se escribe en camelCase. Ex: 1) Declaración de la función: const ocultarModal = () => { //Cuerpo de la función }. 2) En el componente: @ocultar-modal="ocultarModal". 

- En el hijo se escribe la función con guion '-'. Ex: 1) Se recibe la función: const emit = defineEmits(['ocultar-modal']). 2) En la etiqueta: @click.prevent="$emit('ocultar-modal')"  



*/






/** 
 * Para hacer una variable ref:  
 */ 
//1.- Import
import { ref } from 'vue';

//2.- Declaracion de variables ref
const nombreVariableEntera = ref(0); // Variable Ejemplo
const nombreVariableDouble = ref(0.0); 
const nombreVariableString = ref(''); 
const nombreVariableNull = ref(null); 
const nombreVariableArray = ref([]); 
const nombreVariableObject = ref({}); 


// 3.- Asignación de variables ref
nombreVariableEntera.value = 30;        
nombreVariableDouble = 0.0; 
nombreVariableString = 'Milena la mejor'; 
nombreVariableNull = null; 
nombreVariableArray = [1,2,3,4]; 
nombreVariableObject = {nombre: "Pepelepu", edad: 18}; 



/** 
 * Para hacer una variable reactive:  
 */ 
//1.- Import
import { reactive } from 'vue';

//2.- Declaracion de variables reactive
const formulario = reactive({
    nombre: '',
    edad: 0,
});   

// 3.- Asignación de variables reactive
formulario.nombre = 'Pepe';  
formulario.edad = 38;  






/** 
 * Para conocer cual es el componente PADRE y cual es el componente HIJO   
 * 
 */ 


// PADRE: Ejemplo archivo App.vue:
// El componente PADRE tiene el "import" obligatoriamente del componente HIJO, es decir:

//<script setup>
    //...
    import Alerta from './components/Alerta.vue';
    //...
//</script>


<template>
    ...

    <Alerta 
        // @function-para-enviar="functionParaEnviar"
        // :variableParaEnviar="variableParaEnviar"
        // Se pueden definir otras propiedades, por ejemplo:
        // class="text-center" ó :class="text-center"
        // v-if="condicion>0"
        // v-else
    />

    ....

</template>






// HIJO: Ejemplo Archivo componets/Alerta.vue
// El componente hijo debe es donde se definen los "defineEmits" y "defineProps"

// 1.- Ejemplo para las funciones "defineEmits"

//<script setup>
    //...
    
    const emit = defineEmits(['function-para-enviar'])
    
    //...

    emit('function-para-enviar')

//</script>


//<template>
    //...

    //<button 
        //...
        //@click.prevent="$emit('function-para-enviar')"
    //>
    //</button>

    //...

//</template>







// 2.- Ejemplo para las variables "defineProps"

//<script setup>
    //...
    const props = defineProps({
        variableParaEnviar: {
            type: Number,
            required: true
        }
    })
    //...

    //Para usar en el script
    props.variableParaEnviar;

//</script>


<template>

    <p>
        {{ variableParaEnviar }}
    </p>
    
</template>
