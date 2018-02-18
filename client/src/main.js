import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import Report from './Report.vue'
import Landing from './Landing.vue'

Vue.use(BootstrapVue)
Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {path: '/', component: Landing},
    {path: '/report', component: Report}
  ],
  mode: 'history'
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
