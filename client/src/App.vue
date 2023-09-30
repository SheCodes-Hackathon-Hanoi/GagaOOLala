<script setup>
import { RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import NavBar from "./components/navbar/NavBar.vue";
</script>

<template>
  <NavBar />
  <RouterView />
</template>