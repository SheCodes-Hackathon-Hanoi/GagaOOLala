<script setup>
import { RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import NavBar from "./components/layout/NavBar.vue";
import Footer from "./components/layout/Footer.vue";
</script>

<template>
  <NavBar />
  <RouterView />
  <Footer />
</template>