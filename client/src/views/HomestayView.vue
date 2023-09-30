<script setup>
import Information from "../components/homestay/Information.vue";
import Suggest from "../components/homestay/Suggest.vue";
import Booking from "../components/homestay/Booking.vue";
const showPopup = ref(false);
</script>
<template>
  <div class="container">
    <Information />
    <!-- <div>
      <button @click="showPopup = true">Open Pop-up</button>
      <div v-if="showPopup" class="popup">
        <div class="popup-content">
          <span @click="showPopup = false" class="close-button">X</span>
          <h2>Pop-up Content</h2>
          <p>
            This is a simple pop-up created with Vue 3 using
            <code>&lt;script setup&gt;</code>.
          </p>
        </div>
      </div>
    </div> -->
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

/* .popup {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.popup-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
  text-align: center;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
} */
</style>
