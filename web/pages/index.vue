<script setup lang="ts">
const { data: projects, refresh } = await useFetch<Project[]>("/projects/", {
  baseURL: useRuntimeConfig().public.apiBase,
})

const form = ref({
  title: "",
  description: "",
  start: new Date(),
  end: new Date(),
})

async function addProject() {
  await useFetch("/projects/", {
    baseURL: useRuntimeConfig().public.apiBase,
    method: "POST",
    body: form,
  }).then(() => {
    refresh()
    form.value = {
      title: "",
      description: "",
      start: new Date(),
      end: new Date(),
    }
  })
}
</script>

<template>
  <div class="flex flex-col gap-y-8">
    <h1 class="text-2xl">Список проектов</h1>
    <div class="grid grid-cols-3 gap-4">
      <NuxtLink class="bg-white p-6 rounded shadow-sm hover:shadow transition-shadow flex flex-col gap-y-2" v-for="project in projects" :key="project.id" :to="`/projects/${project.id}`">
        <h2 class="text-xl">{{ project.title }}</h2>
        <p v-if="project.description" class="text-neutral-400">{{ project.description }}</p>
        <p v-if="project.end" class="w-max bg-neutral-50 text-neutral-400 rounded-full px-2 py-1 text-sm">до {{ new Date(project.end).toLocaleDateString() }}</p>
      </NuxtLink>
    </div>
    <div class="grid grid-cols-3 gap-4">
      <form @submit.prevent="addProject" class="flex flex-col gap-y-4 bg-white p-6 rounded shadow-sm">
        <div class="flex flex-col gap-y-2">
          <label for="title">Заголовок</label>
          <input id="title" type="text" class="bg-neutral-50 h-10 rounded px-3" placeholder="Введите заголовок" v-model="form.title" />
        </div>
        <div class="flex flex-col gap-y-2">
          <label for="description">Описание</label>
          <input id="description" type="text" class="bg-neutral-50 h-10 rounded px-3" placeholder="Введите описание" v-model="form.description" />
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div class="flex flex-col gap-y-2">
            <label for="startDate">Дата начала</label>
            <input id="startDate" type="date" class="bg-neutral-50 h-10 rounded px-3" v-model="form.start" />
          </div>
          <div class="flex flex-col gap-y-2">
            <label for="endDate">Дата окончания</label>
            <input id="endDate" type="date" class="bg-neutral-50 h-10 rounded px-3" v-model="form.end" />
          </div>
        </div>
        <button type="submit" class="px-3 h-10 bg-blue-50 text-blue-500 mt-4 rounded hover:bg-blue-100 transition-colors">Добавить проект</button>
      </form>
    </div>
  </div>
</template>
