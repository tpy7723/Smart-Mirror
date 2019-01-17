import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-socket.io'
Vue.config.productionTip = false

Vue.use(new VueSocketIO({
  debug: true,
  connection: "http://127.0.0.1:5000"
}))
new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
