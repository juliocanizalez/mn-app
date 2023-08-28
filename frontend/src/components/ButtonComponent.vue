<template>
  <q-btn
    color="secondary"
    :label="label! || 'Calcular'"
    :type="isSubmit ? 'subtmit' : 'button'"
  ></q-btn>
</template>
<script setup lang="ts">
defineProps({
  label: String,
  isSubmit: Boolean,
});
</script>
