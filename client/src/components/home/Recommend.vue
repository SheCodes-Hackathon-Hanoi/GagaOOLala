<script setup>
import useTravel from "../../stores/travel";
import { onMounted } from "vue";

const { getRecommendTrip, travels } = useTravel();
onMounted(() => getRecommendTrip());
</script>
<template>
  <div class="text-header">GỢI Ý CHUYẾN ĐI THEO SỞ THÍCH CỦA BẠN</div>
  <div class="flex-container">
    <div
      v-for="(trip, index) in travels.recommendations"
      :key="index"
      class="max-w-xs bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
      style="position: relative"
    >
      <!-- <RouterLink :to="{ name: 'homestay', params: { id: trip.id } }"> -->
        <img
          :src="`./public/assets/homestay_img/${trip.homestay_img}`"
          class="rounded-t-lg"
          alt="Travel image"
        />
        <div class="p-5" sty>
          <h5
            class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
          >
            {{ trip.title }}
          </h5>
          <!-- <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
          </p> -->
        </div>
      <!-- </RouterLink> -->
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
  gap: 30px;
  z-index: 1;
}
</style>
