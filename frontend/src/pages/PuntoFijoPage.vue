<template>
  <q-page class="row justify-center gap-1 bg-grey-1 text-focus-in">
    <q-form
      class="q-gutter-y-md q-mt-lg form-width-lg"
      @reset="onReset"
      @submit="onSubmit"
    >
      <h3 class="text-bold">Punto Fijo</h3>
      <div class="row gap-1">
        <p class="text-nm text-formula"><em>g(x) </em>=</p>
        <q-input
          class="input-width-xs"
          v-model="func"
          label="Ingresa la funcion"
          stack-label
        >
          <q-tooltip
            anchor="top middle"
            self="bottom middle"
            :offset="[0, -20]"
          >
            Ingresar formula despejada
          </q-tooltip>
        </q-input>
      </div>
      <q-input
        v-model="x"
        label="X&#8320;"
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
      <div class="q-gutter-x-md">
        <button-component is-submit />
        <button-component label="Limpiar" flat type="reset" />
      </div>
    </q-form>
    <div class="form-width-lg q-mt-xl">
      <card-log-component class="q-mt-xl" :data="dataArray" />
    </div>
  </q-page>
</template>
<script setup lang="ts">
import { ref, Ref } from 'vue';
import ButtonComponent from 'src/components/ButtonComponent.vue';
import CardLogComponent from 'src/components/CardLogComponent.vue';
import { api } from 'src/boot/axios';
import { endpoints } from 'src/utils';

const func = ref('');
const x = ref(0);
const errorText = '1%';
const iteraciones = 100;
const dataArray: Ref<string[]> = ref([]);

const onReset = () => {
  func.value = '';
  x.value = 0;
};

const onSubmit = async () => {
  const data = {
    func: func.value,
    x: x.value,
    err: 0.01,
    iterations: iteraciones,
  };

  try {
    const response = await api.post(endpoints.puntoFijo, data);
    dataArray.value = response.data;
  } catch (error) {
    // do nothing
  }
};
</script>
