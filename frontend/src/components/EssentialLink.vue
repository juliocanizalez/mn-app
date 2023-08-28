<template>
  <q-btn-dropdown
    v-if="childLinks?.length"
    flat
    class="link-button"
    :label="title"
  >
    <q-list>
      <q-item
        clickable
        v-close-popup
        v-for="(child, index) in childLinks!"
        :key="index"
        @click="navigateTo(child.link!)"
      >
        <q-item-section>
          <q-item-label>{{ child.title }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-btn-dropdown>
  <q-btn v-else flat class="link-button" @click="navigateTo(props.link!)">
    {{ title }}
  </q-btn>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const props = defineProps({
  title: String,
  link: String,
  childLinks: Array as () => Array<{ title: string; link: string }>,
});

const router = useRouter();

const navigateTo = (link: string) => {
  router.push({ name: link });
};
</script>
