<template>
  <div id="app">

    <navbar></navbar>

    <main role="main" class="flex-shrink-0">
      <div id="maincontent" class="container-fluid">
        <poodle></poodle>
      </div> <!-- /container -->
    </main>
  </div>
</template>

<script>
  //import config from './configuration'

  import Poodle from './components/Poodle'
  import Navbar from './components/Navbar'

  export default {
    name: 'App',
    components: {
      'poodle': Poodle,
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