<script setup lang="ts"></script>

<template>
  <div>
    <header>
      <NuxtLink to="/">Главная</NuxtLink>
    </header>
    <main>
      <NuxtPage />
    </main>
  </div>
</template>

<style scoped>
header {
  padding-bottom: 16px;
  border-bottom: 1px solid gray;
}
</style>
