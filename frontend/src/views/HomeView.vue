<!-- src/views/HomeView.vue -->
<template>
  <div class="home">
    <h1>青岛文化之旅地图</h1>
    <AmapContainer />
  </div>
</template>

<template>
  <div class="home">
    <h1 style="color: red">测试标题</h1> <!-- 红色标题测试 -->
    <div style="width: 100px; height: 100px; background: blue"></div> <!-- 蓝色方块测试 -->
    <AmapContainer />
  </div>
</template>

<script>
import AmapContainer from '@/components/AmapContainer.vue'

export default {
  components: {
    AmapContainer
  }
}
</script>
