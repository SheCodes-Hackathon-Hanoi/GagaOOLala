<script setup>
import { reactive } from "vue";
import useTravel from "../../stores/travel";
import { onMounted } from "vue";
const form = reactive({
  checkin: "",
  checkout: "",
});
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
  <div class="header-text">Đặt lịch</div>
  <div class="flexb">
    <form onsubmit="return false">
      <div class="grip">
        <label for="checkin">Ngày nhận phòng: </label>
        <input type="date" id="checkin" v-model="form.checkin" />
        <label for="checkout">Ngày trả phòng: </label>
        <input type="date" id="checkout" v-model="form.checkout" />
      </div>
      <button
        type="submit"
        style="
          background-color: #b4c01a;
          padding: 10px 10px;
          border-radius: 11px;
          border: 1px solid #4d5300;
        "
      >
        Đặt phòng
      </button>
    </form>
    <table>
      <tr>
        <th>Ngày nhận phòng</th>
        <th>Ngày trả phòng</th>
        <th>Tình trạng phòng</th>
        <th>Tổng giá</th>
        <th>Mô tả</th>
      </tr>
      <tr>
        <td>{{ form.checkin }}</td>
        <td>{{ form.checkout }}</td>
        <td>Avalable</td>
        <td>{{ travel.price }}</td>
        <td>{{ travel.place }} <br> {{ travel.type }}</td>
      </tr>
    </table>
  </div>
</template>
<style scoped>
.header-text {
  color: #000;
  font-family: Inter;
  font-size: 40px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  padding: 20px 5%;
}
form {
  padding: 5% 5%;
  border: 2px solid #8e8e8e;
  border-radius: 15px;
  text-align: center;
}
.grip {
  display: grid;
  grid-template-columns: 50% 50%;
  grid-column-gap: 5px;
  grid-row-gap: 5px;
  margin-bottom: 10px;
}
.flexb {
  display: grid;
  grid-template-columns: 40% 60%;
  grid-column-gap: 10px;
  grid-row-gap: 50px;
  padding-left: 5%;
  padding-bottom: 50px;
}

table {
  border: 1px solid #8e8e8e;
}
th {
  background: #b4c01a;
}
tr {
    text-align: center;
}
</style>
