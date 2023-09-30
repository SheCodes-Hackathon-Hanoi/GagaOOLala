<script setup>
import { ref, onMounted } from "vue";

const images = ref([
  "../../../../public/demo_rcm.jpeg",
  "https://picsum.photos/id/238/1024/800",
  "../../../../public/demo_rcm.jpeg",
]);

let active = ref(0);

onMounted(() => {
  let i = 0;
  setInterval(() => {
    if (i > images.value.length - 1) {
      i = 0;
    }
    active.value = i;
    i++;
  }, 2000);
});
</script>
<template>
  <div class="relative slide">
    <div
      class="carousel-indicators absolute bottom-0 flex bg-yellow-100 h-24 w-full justify-center items-center"
    >
      <ol class="z-50 flex w-4/12 justify-center">
        <li
          v-for="(img, i) in images"
          :key="i"
          class="md:w-4 md:h-4 bg-gray-300 rounded-full cursor-pointer mx-2"
        ></li>
      </ol>
    </div>
    <div class="carousel-inner relative overflow-hidden w-full">
      <div
        v-for="(img, i) in images"
        :id="`slide-${i}`"
        :key="i"
        :class="`${active === i ? 'active' : 'left-full'}`"
        class="carousel-item inset-0 relative w-full transform transition-all duration-500 ease-in-out"
      >
        <img class="block w-full h-auto" :src="img" alt="First slide" />
      </div>
    </div>
  </div>
</template>

<style>
.left-full {
  left: -100%;
}

.carousel-item {
  float: left;
  position: relative;
  display: block;
  width: 100%;
  margin-right: -100%;
  backface-visibility: hidden;
}

.carousel-item.active {
  left: 0;
}
</style>
