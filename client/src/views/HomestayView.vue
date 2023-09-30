<script setup>
import Information from "../components/homestay/Information.vue";
import Suggest from "../components/homestay/Suggest.vue";
import Booking from "../components/homestay/Booking.vue";
import Popup from "../components/homestay/Popup.vue";
import Vr from "../components/homestay/Vr.vue";

</script>
<template>
  <div class="container">
    <Information />
    <Popup>
      <template #header>
        <div class="popover" style="text-align: center; color: red">Trải nghiệm VR</div>
      </template>
      <template #content>
        <div class="popover-content"><Vr imageSource="../../public/test.jpg" /></div>
      </template>
    </Popup>
    <Booking />
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
