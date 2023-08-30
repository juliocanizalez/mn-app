<template>
  <q-page class="row justify-center gap-1 bg-grey-1 text-focus-in">
    <q-form
      class="q-gutter-y-md q-mt-lg form-width-lg"
      @reset="onReset"
      @submit="onSubmit"
    >
      <h3 class="text-bold">Newton-Raphson</h3>
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
        v-model="xSubZero"
        label="X&#8320;"
        stack-label
        class="input-width-sm"
      />
      <q-input
        v-model.number="errorText"
        label="Margen de error (%)"
        type="number"
        stack-label
        class="input-width-sm"
      >
        <q-tooltip anchor="top left" self="bottom left" :offset="[0, -10]">
          1 = 1%
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
const xSubZero = ref(0);
const errorText = ref(1);
const dataArray: Ref<string[]> = ref([]);

const onReset = () => {
  func.value = '';
  xSubZero.value = 0;
  errorText.value = 1;
};

const onSubmit = async () => {
  const err = errorText.value / 100;
  const data = {
    func: func.value,
    x: xSubZero.value,
    err,
  };

  try {
    const response = await api.post(endpoints.newtonRaphson, data);
    dataArray.value = response.data;
  } catch (error) {
    // do nothing
  }
};
</script>
