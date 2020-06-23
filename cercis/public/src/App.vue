<template>
  <div id="app">
    <div v-if="loading" class="d-flex flex-row justify-content-center align-items-center">
      <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner"></b-spinner>
      <small class="center-block">
        Loading...
      </small>
    </div>

      <h1 class="page-header d-flex flex-row justify-content-between align-items-center">
        <div>{{ poodle.name_registered }} <span v-if="poodle.name_call">| <span class="text-condensed">{{
            poodle.name_call
            }}</span></span>
        </div>
      </h1>

      <section id="info-card">
          <b-tabs nav-wrapper-class="col-2" content-class="col-10" lazy pills vertical>
            <b-tab title="Basic" active>
              <poodle-basic :poodle="poodle" :showBasicForm="showBasicForm"></poodle-basic>
            </b-tab>
            <b-tab title="Registration">
              <poodle-registration :poodle="poodle" :showRegistrationForm="showRegistrationForm"></poodle-registration>
            </b-tab>
            <b-tab title="Health">
              <poodle-health :poodle="poodle" :showHealthForm="showHealthForm"></poodle-health>
            </b-tab>
            <b-tab title="Comments">
              <poodle-comments :poodle="poodle" :showCommentsForm="showCommentsForm"></poodle-comments>
            </b-tab>
          </b-tabs>       
      </section>

      <section id="related-card">
       
          <b-tabs nav-wrapper-class="col-2" content-class="col-10" lazy pills vertical>
            <b-tab title="Pedigree" active>
              <three-gen-pedigree :poodle="poodle"></three-gen-pedigree>
            </b-tab>

            <b-tab title="Offspring" class="" v-if="poodle.offspring && poodle.offspring.length > 0">
              <b-list-group flush>
                <poodle-list-item v-for="p in poodle.offspring" v-bind:key="p.id" :poodle="p" type="offspring">
                </poodle-list-item>
              </b-list-group>
            </b-tab>

            <b-tab title="Siblings">
              <b-tabs pills card vertical end id="sibling-sub-tabs">
                <b-tab title="Full" v-if="poodle.siblings_full && poodle.siblings_full.length > 0">
                  <b-list-group flush>
                    <poodle-list-item v-for="p in poodle.siblings_full" v-bind:key="p.id" :poodle="p" type="full">
                    </poodle-list-item>
                  </b-list-group>
                </b-tab>

                <b-tab title="Dam's Side" v-if="poodle.siblings_damside && poodle.siblings_damside.length > 0">
                  <b-list-group flush>
                    <poodle-list-item v-for="p in poodle.siblings_damside" v-bind:key="p.id" :poodle="p" type="damside">
                    </poodle-list-item>
                  </b-list-group>
                </b-tab>

                <b-tab title="Sire's Side" v-if="poodle.siblings_sireside && poodle.siblings_sireside.length > 0">
                  <b-list-group flush>
                    <poodle-list-item v-for="p in poodle.siblings_sireside" v-bind:key="p.id" :poodle="p"
                      type="sireside">
                    </poodle-list-item>
                  </b-list-group>
                </b-tab>
              </b-tabs>

            </b-tab>
          </b-tabs>    
      </section>


      <small>
        Created {{ poodle.created_at }}
        <span class="float-right">Last Updated {{ poodle.updated_at }}</span>
      </small>
    </div>

</template>

<script>
  import SERVER_CONFIGURATION from './configuration'

  import axios from 'axios'

  import PoodleListItem from './components/PoodleListItem'
  import PoodleBasic from './components/PoodleBasic'

  import PoodleRegistration from './components/PoodleRegistration'
  import PoodleHealth from './components/PoodleHealth'
  import PoodleComments from './components/PoodleComments'

  import ThreeGenPedigree from './components/ThreeGenPedigree'

  export default {
    name: 'App',
    components: {
      PoodleListItem,
      PoodleBasic,
      PoodleRegistration,
      PoodleHealth,
      PoodleComments,
      ThreeGenPedigree
    },
    data: function () {
      return {
        showImageForm: false,
        showBasicForm: false,
        showRegistrationForm: false,
        showHealthForm: false,
        showCommentsForm: false,
        loading: false,
        poodle: {},
        options: {
          sire: [],
          dam: [],
          color: [],
          variety: [],
          origin_country: [],
          owner: [],
          breeder: [],
        },
        hasImage: false,
      }
    },
    mounted() {
      this.options.sex = [{
          code: 'M',
          label: 'Dog',
        },
        {
          code: 'F',
          label: 'Bitch'
        },
        {
          code: 'U',
          label: 'Unknown'
        },
      ]
      this.options.variety = [{
          code: 'S',
          label: 'Standard',
        },
        {
          code: 'M',
          label: 'Miniature/Medium/Moyan'
        },
        {
          code: 'D',
          label: 'Dwarf'
        },
        {
          code: 'T',
          label: 'Toy'
        }
      ]

      //Promise.all([this.getPoodle(), this.getImages()]);
      this.getPoodle()
    },
    computed: {
      adminApproved: function () {
        return this.poodle.is_viewable
      },
    },
    methods: {
      getPoodle: function () {
        this.loading = true
        var url = SERVER_CONFIGURATION.endpoints.poodle() + 'crystal-creeks-conspiracy-of-kings-bcat-star-cgca/'
        return axios.get(url).then((response) => {
          this.poodle = response.data || []
          this.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
      getImages: function () {
        this.loading = true
        var url = SERVER_CONFIGURATION.endpoints.image() +
          '?poodle=crystal-creeks-conspiracy-of-kings-bcat-star-cgca/'
        return axios.get(url).then((response) => {
          this.images = response.data.results || []
          this.loadng = false
        }).catch(error => {
          console.log(error)
        });
      },
      searchColor: function (search) {
        this.loading = true;
        var url = SERVER_CONFIGURATION.endpoints.color() + '?text=' + search
        return axios.get(url).then((response) => {
          this.options.color = response.data.results || [];
          this.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
      searchCountry: function (search) {
        this.loading = true;
        var url = SERVER_CONFIGURATION.endpoints.country() + '?text=' + search
        return axios.get(url).then((response) => {
          this.options.origin_country = response.data.results || [];
          this.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
      searchBreeder: function (search) {
        var url = SERVER_CONFIGURATION.endpoints.person() + '?full_name=' + search
        return axios.get(url).then((response) => {
          this.options.breeder = response.data.results || [];
          this.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
      searchOwner: function (search) {
        this.loading = true;
        var url = SERVER_CONFIGURATION.endpoints.person() + '?full_name=' + search
        return axios.get(url).then((response) => {
          this.options.owner = response.data.results || [];
          this.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
      searchDam: function (search) {
        this.loading = true;
        var url = SERVER_CONFIGURATION.endpoints.filter() + '?sex=F&name_registered=' + search
        return axios.get(url).then((response) => {
          this.options.dam = response.data.results || [];
          this.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
      searchSire: function (search) {
        this.loading = true;
        var url = SERVER_CONFIGURATION.endpoints.filter() + '?sex=M&name_registered=' + search
        return axios.get(url).then((response) => {
          this.options.sire = response.data.results || [];
          this.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
      /**
       * @param search
       * @param q
       * @param options
       * @param url
       */
      search: function (search, q, options, url) {
        var self = this;
        var params = new URLSearchParams();
        params.append(q, search);
        url += '?' + params

        return axios.get(url).then((response) => {
          options = response.data.results || [];
          console.log(options)
          self.loading = false
        }).catch(error => {
          console.log(error)
        });
      },
    }
  }
</script>

<style scoped>
.tab-content.col-10{
  padding: 0
}
</style>