/************************************************
 * 
 *  VARIABLES
 * 
 ************************************************/


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
//</script>


//<template>
    //...

    //<button 
        //...
        //@click="$emit('function-para-enviar')"
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
//</script>

