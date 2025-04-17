<template>
  <div class="map-wrapper">
    <!-- 地图容器 -->
    <div id="map-container" ref="mapContainer"></div>

    <!-- 缩放控件 -->
    <div class="map-controls">
      <button @click="zoomIn">+</button>
      <button @click="zoomOut">-</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AmapContainer', // ✅ 修复name属性语法
  data() {
    return {
      map: null,
      zoom: 12
    }
  },
  mounted() {
    this.initMap()
  },
  methods: {
    // 初始化地图
    initMap() {
      this.map = new AMap.Map('map-container', {
        zoom: this.zoom,
        center: [120.3826, 36.0671],
        viewMode: '2D'
      })
      this.map.addControl(new AMap.ZoomControl())
    },
    // 添加标记点方法
    addMarker(lng, lat, title) {
      const marker = new AMap.Marker({
        position: [lng, lat],
        title: title,
        map: this.map
      })
      marker.on('click', () => {
        new AMap.InfoWindow({
          content: `<h3>${title}</h3>`
        }).open(this.map, marker.getPosition())
      })
    },
    zoomIn() {
      this.zoom = Math.min(this.zoom + 1, 18)
      this.map.setZoom(this.zoom)
    },
    zoomOut() {
      this.zoom = Math.max(this.zoom - 1, 3)
      this.map.setZoom(this.zoom)
    }
  }
}
</script>

<style scoped>
.map-wrapper {
  position: relative;
  width: 100%;
  height: 600px;
}

#map-container {
  width: 100%;
  height: 100%;
  border: 5px solid red !important; /* 调试边框 */
}

.map-controls {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 999;
}

button {
  display: block;
  margin-bottom: 5px;
  padding: 5px 10px;
}
</style>
