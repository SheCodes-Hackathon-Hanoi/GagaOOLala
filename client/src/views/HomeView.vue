<script setup>
import Search from '../components/home/Search.vue';
import Trending from '../components/home/Trending.vue';
import Recommend from '../components/home/Recommend.vue';
// import useTravel from "../../stores/travel";

// import { onMounted } from 'vue';

// const { getTrendingTrip, travels } = useTravel();
// onMounted(async() => getTrendingTrip());
</script>

<template>
  <main>
    <Search />
    <Trending />
    <Recommend />
  </main>
</template>
