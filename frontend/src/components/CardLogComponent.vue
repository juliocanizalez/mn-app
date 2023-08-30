<template>
  <q-card class="bg-white overflow-auto card-logs">
    <q-card-section>
      <h6 class="q-ma-xs">Resultados</h6>
    </q-card-section>
    <template v-for="(text, index) in data" :key="index">
      <q-card-section class="q-py-xs">
        {{ text }}
      </q-card-section>
      <q-separator
        class="q-my-sm"
        inset
        v-if="(index + 1) % 3 === 0 && index !== data.length - 1"
      />
    </template>
  </q-card>
</template>
<script setup lang="ts">
defineProps({
  data: {
    type: Array,
    required: true,
  },
});
</script>
