<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="q-px-xl">
        <q-toolbar-title> Metodos Numericos - Portafolio </q-toolbar-title>
        <EssentialLink title="Inicio" link="home" />
        <EssentialLink title="Periodo I" :child-links="linksList" />
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
