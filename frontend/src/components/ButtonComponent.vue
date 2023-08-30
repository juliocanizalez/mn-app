<template>
  <q-btn
    color="primary"
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
