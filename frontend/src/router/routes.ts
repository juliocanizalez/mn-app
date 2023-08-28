import { RouteRecordRaw } from 'vue-router';
import { routes as r } from 'src/utils';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/IndexPage.vue'),
        name: 'home',
      },
      {
        path: r.biseccion,
        component: () => import('pages/BiseccionPage.vue'),
        name: r.biseccion,
      },
      {
        path: r.falsaPosicion,
        component: () => import('pages/FalsaPosicionPage.vue'),
        name: r.falsaPosicion,
      },
      {
        path: r.newtonRaphson,
        component: () => import('pages/NewtonRaphson.vue'),
        name: r.newtonRaphson,
      },
      {
        path: r.puntoFijo,
        component: () => import('pages/PuntoFijoPage.vue'),
        name: r.puntoFijo,
      },
      {
        path: r.secante,
        component: () => import('pages/SecantePage.vue'),
        name: r.secante,
      },
    ],
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
