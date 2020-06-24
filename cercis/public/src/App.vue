<template>
  <div id="app">

    <div id="navbarSlot">
      <navbar></navbar>
    </div>

    <main role="main" class="flex-shrink-0">
      <div id="maincontent" class="container-fluid">
        <router-view></router-view>
      </div> <!-- /container -->
    </main>
  </div>
</template>

<script>
  //import config from './configuration'

  import Navbar from './components/Navbar'

  export default {
    name: 'App',
    components: {

      'navbar': Navbar,
    },
    data: function () {
      return {

      }
    },
    mounted() {

    },
    computed: {

    },
    methods: {

    }
  }
</script>

<style scoped>
  .tab-content.col-10 {
    padding: 0
  }
</style>