<template>
  <q-table
    flat
    bordered
    dense
    :columns="columns"
    :rows="rows"
    class="text-focus-in bg-white shadow-2"
  />
</template>
<script setup lang="ts">
import { IResults } from 'src/interfaces';

defineProps<{
  columns: [];
  rows: IResults[];
}>();
</script>
