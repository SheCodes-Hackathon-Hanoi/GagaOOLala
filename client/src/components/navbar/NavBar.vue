<script setup>
import { RouterLink } from "vue-router";
</script>
<template>
  <nav
    class="bg-white border-gray-200 dark:bg-gray-900"
    style="background-color: #c5d12c"
  >
    <div
      class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4"
    >
      <RouterLink to="/" class="flex items-center">
        <span
          style="
            color: #000;
            font-family: Krona One;
            font-size: 40px;
            font-style: normal;
            font-weight: 400;
            line-height: normal;
          "
        >
          MiniGoAI
        </span>
      </RouterLink>
      <div class="flex items-center">
        <RouterLink
          to="/"
          class="mr-6 text- text-black-500 dark:text-white hover:underline"
          >Đăng nhập</RouterLink
        >
        <RouterLink
          to="/"
          class="mr-6 text- text-black-500 dark:text-white hover:underline"
          >Đăng ký</RouterLink
        >
      </div>
    </div>
  </nav>
  <nav class="bg-gray-50 dark:bg-gray-700 flex flex-wrap items-center justify-between">
    <div class="max-w-screen-xl px-4 py-3 mx-auto">
      <div class="flex items-center">
        <ul class="flex flex-row font-medium mt-0 mr-6 space-x-8 text-sm">
          <li>
            <RouterLink
              to="/"
              class="text-gray-900 dark:text-white focus:font-bold"
              aria-current="page"
              >TRANG CHỦ</RouterLink
            >
          </li>
          <li>
            <RouterLink
              to="/app"
              class="text-gray-900 dark:text-white focus:font-bold"
              aria-current="page"
              >TOUR</RouterLink
            >
          </li>
          <li>
            <RouterLink
              to=""
              class="text-gray-900 dark:text-white focus:font-bold"
              aria-current="page"
              >CHỖ Ở</RouterLink
            >
          </li>
          <li>
            <RouterLink
              to=""
              class="text-gray-900 dark:text-white focus:font-bold"
              aria-current="page"
              >DI CHUYỂN</RouterLink
            >
          </li>
          <li>
            <RouterLink
              to=""
              class="text-gray-900 dark:text-white focus:font-bold"
              aria-current="page"
              >HOẠT ĐỘNG TRẢI NGHIỆM</RouterLink
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
