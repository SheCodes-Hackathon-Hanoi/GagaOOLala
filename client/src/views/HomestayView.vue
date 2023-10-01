<script setup>
import Information from "../components/homestay/Information.vue";
import Suggest from "../components/homestay/Suggest.vue";
import Booking from "../components/homestay/Booking.vue";
import Popup from "../components/homestay/Popup.vue";
import Vr from "../components/homestay/Vr.vue";
import useTravel from "../stores/travel.js";
import { onMounted } from "vue";

const props = defineProps({
    id: {
        required: true,
        type: String,
    },
});
const { getTravel, travel } = useTravel();
onMounted(() => getTravel(props.id));
console.log(travel);
</script>
<template>
  <div class="container">
    <Information :id="props.id"/>
    <Popup>
      <template #header>
        <div class="popover" style="text-align: center; color: red">Trải nghiệm VR</div>
      </template>
      <template #content>
        <div class="popover-content"><Vr imageSource="../../public/test.jpg" /></div>
      </template>
    </Popup>
    <Booking :id="props.id"/>
    <Suggest />
  </div>
</template>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  margin: auto;
}
</style>
