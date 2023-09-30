<script setup></script>
<template>
  <div class="flex-container">
    <div class="price">300,000VNĐ</div>
    <button
      type="button"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    >
      Đặt ngay
    </button>
    <div class="info">
      Địa chỉ: Tổ 2, thị trấn Mù Cang Chải <br />
      Host: Nùng Cao N <br />
      Thuộc khu vực: Mù Cang Chải, Yên Bái <br />
      Các dịch vụ nổi bật do host cung cấp: <br />
      Du lịch sinh thái: cắm trại, trekking rừng <br />
      Du lịch cộng đồng: Trải nghiệm nếp sống và tự tay nấu những món ăn ngon
      dân dã của người dân địa phương
    </div>
  </div>
</template>
<style scoped>
.flex-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.price {
  color: #000;
  text-align: center;
  font-family: Inter;
  font-size: 40px;
  font-style: normal;
  font-weight: 700;
  line-height: 30px;
  text-transform: uppercase;
}
.info {
  color: #565656;
  font-family: Inter;
  font-size: 19px;
  font-style: normal;
  font-weight: 400;
  line-height: 23px;
  border-radius: 8px;
  border: 2px solid #d9d9d9;
  background: #fff;
  padding: 10px;
}
</style>
