import { createApp } from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
const app = createApp(App)
app.use(Vuetify)
app.mount('#app')



//import router from './router'  // 添加这行

createApp(App)
  //.use(router)  // 添加这行
  .mount('#app')
