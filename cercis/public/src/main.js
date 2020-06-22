import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'

import './assets/styles/custom-bootstrap-overrides.scss'
import 'bootstrap/scss/bootstrap.scss'
import 'bootstrap-vue/src/index.scss'


Vue.use(BootstrapVue)
Vue.config.productionTip = false


new Vue({
  render: h => h(App),
}).$mount('#app')
