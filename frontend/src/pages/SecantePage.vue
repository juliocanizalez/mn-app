<template>
  <q-page class="row justify-center gap-1 bg-grey-1 text-focus-in">
    <q-form
      class="q-gutter-y-md q-mt-lg form-width-lg"
      @reset="onReset"
      @submit="onSubmit"
    >
      <h3 class="text-bold q-mb-none">Secante y</h3>
      <h3 class="text-bold">Secante Modificada</h3>
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
        v-if="!isModified"
        v-model="xPrev"
        type="number"
        step="0.01"
        stack-label
        class="input-width-sm"
        label="Valor de X&#8336;&#8331;&#8321;"
      />
      <q-input
        v-if="!isModified"
        v-model="x"
        type="number"
        step="0.01"
        label="Valor de X&#8336;"
        stack-label
        class="input-width-sm"
      />
      <q-input
        v-if="isModified"
        v-model="x"
        type="number"
        step="0.01"
        stack-label
        class="input-width-sm"
        label="Valor de X&#8320;"
      />
      <q-input
        v-if="isModified"
        v-model="delta"
        type="number"
        step="0.01"
        label="Valor de delta"
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
      <q-toggle v-model="isModified" label="Secante Modificada" />
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
import { IData } from 'src/interfaces';

const func = ref('');
const xPrev = ref(0);
const x = ref(0);
const delta = ref(0);
const isModified = ref(false);
const errorText = '1%';
const iteraciones = 100;
const dataArray: Ref<string[]> = ref([]);

const doPost = async (data: IData) => {
  try {
    const response = await api.post(endpoints.secante, data);
    dataArray.value = response.data;
  } catch (error) {
    // do nothing
  }
};

const onReset = () => {
  func.value = '';
  xPrev.value = 0;
  x.value = 0;
  delta.value = 0;
  isModified.value = false;
};

const onSubmit = () => {
  const data = {
    func: func.value,
    x: x.value,
    iterations: iteraciones,
    err: 0.01,
    isModified: isModified.value,
  };

  if (isModified.value) {
    const dataModified = {
      ...data,
      delta: delta.value,
    };

    doPost(dataModified);
  } else {
    const dataNotModified = {
      ...data,
      xPrev: xPrev.value,
    };

    doPost(dataNotModified);
  }
};
</script>
