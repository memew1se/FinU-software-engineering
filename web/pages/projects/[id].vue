<script setup lang="ts">
const { data: project } = await useFetch<Project>(`/projects/${useRoute().params.id}/`, {
  baseURL: useRuntimeConfig().public.apiBase,
})
</script>

<template>
  <div>
    <h1>{{ project?.title }}</h1>
    <p>
      <span>Начало</span>
      <span>{{ new Date(project?.start).toLocaleString() }}</span>
    </p>
    <p>
      <span>Конец</span>
      <span>{{ new Date(project?.end).toLocaleString() }}</span>
    </p>
  </div>
</template>

<style scoped>
p {
  display: flex;
  gap: 4px;
}

p span:first-of-type {
  color: gray;
}
</style>
