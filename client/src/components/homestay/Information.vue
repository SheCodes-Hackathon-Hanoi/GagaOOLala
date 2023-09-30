<script setup>
import Info from "./info/Info.vue";
import Image from "./info/Image.vue";
</script>
<template>
  <div class="header-text">Homestay của anh Nùng Cao N</div>
  <div class="container">
    <Image />
    <Info />
  </div>
</template>
<style scoped>
.container {
  display: flex;
  gap: 20px;
  padding: 20px 5%;
  margin: auto;
}
.header-text {
  color: #000;
  font-family: Inter;
  font-size: 40px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  padding: 20px 5%;
}
</style>
