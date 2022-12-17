<script setup lang="ts">
const { data: projects } = await useFetch<Project[]>("/projects/", {
  baseURL: useRuntimeConfig().public.apiBase,
})
</script>

<template>
  <div>
    <h1>Список проектов</h1>
    <div class="projects-list">
      <NuxtLink v-for="project in projects" :key="project.id" :to="`/projects/${project.id}`">{{ project.title }}</NuxtLink>
    </div>
  </div>
</template>

<style scoped>
.projects-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
</style>
