<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="q-px-xl bg-grey-1 no-shadow">
        <q-toolbar-title class="text-dark title-bar-text"
          >Metodos Numericos - Portafolio</q-toolbar-title
        >
        <div class="q-mx-lg"></div>
        <EssentialLink class="text-grey-8" title="Inicio" link="home" />
        <EssentialLink
          class="text-grey-8"
          title="Periodo I"
          :child-links="linksList"
        />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import EssentialLink from 'components/EssentialLink.vue';
import { routes } from 'src/utils';

const linksList = [
  {
    title: 'Biseccion',
    link: routes.biseccion,
  },
  {
    title: 'Falsa Posicion',
    link: routes.falsaPosicion,
  },
  {
    title: 'Newton-Raphson',
    link: routes.newtonRaphson,
  },
  {
    title: 'Punto Fijo',
    link: routes.puntoFijo,
  },
  {
    title: 'Secante',
    link: routes.secante,
  },
];
</script>
