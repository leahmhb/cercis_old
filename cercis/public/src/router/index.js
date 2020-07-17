import Vue from "vue"
import VueRouter from "vue-router"
import Home from "../views/Home.vue"
import Poodle from "../views/Poodle.vue"
import About from "../views/About.vue"

Vue.use(VueRouter)

const routes = [{
    name: 'poodle-detail',
    path: '/poodle/:slug',
    component: Poodle
  },
  {
    name: 'home',
    path: '/',
    component: Home
  },
  {
    name: 'about',
    path: '/about',
    component: About
  }
]



const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router
