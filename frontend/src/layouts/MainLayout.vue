<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> Metodos Numericos - Portafolio </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> Listado de Ejercicios </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import EssentialLink from 'components/EssentialLink.vue';
import { routes } from 'src/utils';

const linksList = [
  {
    title: 'Inicio',
    icon: 'home',
    link: 'home',
  },
  {
    title: 'Biseccion',
    icon: ' ',
    link: routes.biseccion,
  },
  {
    title: 'Falsa Posicion',
    icon: ' ',
    link: routes.falsaPosicion,
  },
  {
    title: 'Newton-Raphson',
    icon: ' ',
    link: routes.newtonRaphson,
  },
  {
    title: 'Punto Fijo',
    icon: ' ',
    link: routes.puntoFijo,
  },
  {
    title: 'Secante',
    icon: ' ',
    link: routes.secante,
  },
];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
