<script setup>
import Info from "./info/Info.vue";
import Image from "./info/Image.vue";
import useTravel from "../../stores/travel";
import { onMounted } from "vue";
const { getTravel, travel } = useTravel();
const props = defineProps({
    id: {
        required: true,
        type: String,
    },
});
onMounted(() => getTravel(props.id));
</script>
<template>
  <div class="header-text">{{ travel.title }}</div>
  <div class="container">
    <Image />
    <Info :id="props.id"/>
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
