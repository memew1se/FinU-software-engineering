<script setup lang="ts">
const { data: project } = await useFetch<Project>(`/projects/${useRoute().params.id}/`, {
  baseURL: useRuntimeConfig().public.apiBase,
})
</script>

<template>
  <div class="flex flex-col gap-y-4 bg-white px-4 py-6 rounded">
    <h1 class="text-2xl">{{ project?.title }}</h1>
    <p class="text-neutral-400">{{ project?.description }}</p>
    <div class="flex gap-x-1">
      <span class="text-neutral-400">Начало</span>
      <span>{{ new Date(project?.start).toLocaleDateString() }}</span>
    </div>
    <div class="flex gap-x-1">
      <span class="text-neutral-400">Конец</span>
      <span>{{ new Date(project?.end).toLocaleDateString() }}</span>
    </div>
  </div>
</template>
