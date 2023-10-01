<script setup>
import useTravel from "../../stores/travel";

import { onMounted } from "vue";

const { getTrendingTrip, travels } = useTravel();
onMounted(() => getTrendingTrip());
</script>
<template>
  <div class="text-header">THỊNH HÀNH</div>
  <div class="flex-container">
    <div
      v-for="(trip, index) in travels"
      :key="index"
      style="position: relative"
    >
      <RouterLink :to="{ name: 'homestay', params: { id: trip.id } }">
        <img
          :src="`./public/assets/homestay_img/${trip.homestay_img}`"
          style="border-radius: 23px; height: 100%"
          alt="Travel image"
        />
        <div style="position: absolute; bottom: 0px; left: 10%; color: white">
          {{ trip.title }}
        </div>
      </RouterLink>
    </div>
  </div>
</template>
<style scoped>
.text-header {
  margin-top: 50px;
  padding: 20px 15%;
  color: #5f6516;
  font-family: Inter;
  font-size: 40px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.flex-container {
  background-color: FFFBF6;
  display: flex;
  justify-content: space-around;
  padding-inline: 10%;
  padding-bottom: 5%;
  height: 40vh;
  gap: 30px;
  z-index: 1;
}
</style>
