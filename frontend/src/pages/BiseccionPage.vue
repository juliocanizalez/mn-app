<template>
  <q-page class="row justify-center gap-1">
    <q-form class="q-gutter-y-md q-mt-lg form-width-lg">
      <h3 class="text-bold">Biseccion</h3>
      <div class="row gap-1">
        <p class="text-nm text-formula"><em>f(x) </em>=</p>
        <q-input
          class="input-width-xs"
          v-model="func"
          label="Ingresa la funcion"
          stack-label
        />
      </div>
      <q-input
        v-model="aVal"
        label="Valor de a"
        stack-label
        class="input-width-sm"
      />
      <q-input
        v-model="bVal"
        label="Valor de b"
        stack-label
        class="input-width-sm"
      />
      <q-input
        v-model="errorText"
        label="Margen de error"
        stack-label
        class="input-width-sm"
        readonly
      >
        <q-tooltip anchor="top left" self="bottom left" :offset="[0, -10]">
          Valor predeterminado
        </q-tooltip>
      </q-input>
      <q-input
        v-model="iteraciones"
        label="Iteraciones"
        stack-label
        class="input-width-sm"
        readonly
      >
        <q-tooltip anchor="top left" self="bottom left" :offset="[0, -10]">
          Valor predeterminado
        </q-tooltip>
      </q-input>
      <q-space />
      <button-component is-submit />
    </q-form>
    <div class="form-width-lg q-mt-xl">
      <h6 class="q-mt-xl">Resultados</h6>
    </div>
  </q-page>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import ButtonComponent from 'src/components/ButtonComponent.vue';

const func = ref('');
const aVal = ref('');
const bVal = ref('');
const errorText = '1%';
const iteraciones = 100;
</script>
