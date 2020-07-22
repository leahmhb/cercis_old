<template>
    <div id="poodle">
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
                    <poodle-basic :poodle="poodle" formRef="basic-form"></poodle-basic>
                </b-tab>
                <b-tab title="Registration">
                    <poodle-registration :poodle="poodle" formRef="registration-form">
                    </poodle-registration>
                </b-tab>
                <b-tab title="Health">
                    <poodle-health :poodle="poodle" formRef="health-form"></poodle-health>
                </b-tab>
                <b-tab title="Pedigree">
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
                                <poodle-list-item v-for="p in poodle.siblings_full" v-bind:key="p.id" :poodle="p"
                                    type="full">
                                </poodle-list-item>
                            </b-list-group>
                        </b-tab>
                        <b-tab title="Dam's Side" v-if="poodle.siblings_damside && poodle.siblings_damside.length > 0">
                            <b-list-group flush>
                                <poodle-list-item v-for="p in poodle.siblings_damside" v-bind:key="p.id" :poodle="p"
                                    type="damside">
                                </poodle-list-item>
                            </b-list-group>
                        </b-tab>
                        <b-tab title="Sire's Side"
                            v-if="poodle.siblings_sireside && poodle.siblings_sireside.length > 0">
                            <b-list-group flush>
                                <poodle-list-item v-for="p in poodle.siblings_sireside" v-bind:key="p.id" :poodle="p"
                                    type="sireside">
                                </poodle-list-item>
                            </b-list-group>
                        </b-tab>
                    </b-tabs>
                </b-tab>
                <b-tab title="Comments">
                    <poodle-comments :poodle="poodle" formRef="comments-form"></poodle-comments>
                </b-tab>
            </b-tabs>
        </section>

        <footer class="footer navbar navbar-expand-lg mt-auto py-3">
            <div class="container-fluid navbar-text">
                <span class="mr-auto">Created {{ poodle.created_at }}</span>
                <span class="ml-auto">Updated {{ poodle.updated_at }}</span>
            </div>
        </footer>

    </div>

</template>

<script>
    import configuration from './../configuration.js'

    import axios from 'axios'

    import PoodleListItem from './../components/PoodleListItem.vue'
    import PoodleBasic from './../components/PoodleBasic.vue'

    import PoodleRegistration from './../components/PoodleRegistration.vue'
    import PoodleHealth from './../components/PoodleHealth.vue'
    import PoodleComments from './../components/PoodleComments.vue'

    import ThreeGenPedigree from './../components/ThreeGenPedigree.vue'

    let config = configuration.endpoints;

    export default {
        name: 'Poodle',
        components: {
            PoodleListItem,
            PoodleBasic,
            PoodleRegistration,
            PoodleHealth,
            PoodleComments,
            ThreeGenPedigree
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            //Promise.all([this.getPoodle(), this.getImages()]);
            this.getPoodle()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'getPoodle'
        },
        data: function () {
            return {
                loading: false,
                poodle: {},
                hasImage: false,
                slug: this.$route.params.slug,
            }
        },
        beforeRouteUpdate(to, from, next) {
            // just use `this`
            this.slug = to.params.slug
            next()
        },
        mounted() {
        },
        computed: {
            adminApproved: function () {
                return this.poodle.is_viewable
            },
        },
        methods: {
            getPoodle: function () {
                this.loading = true
                var url = config.poodle() +  this.slug
                return axios.get(url).then((response) => {
                    this.poodle = response.data || []
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            getImages: function () {
                this.loading = true
                var url = config.image() + '?poodle=' + this.slug
                return axios.get(url).then((response) => {
                    this.images = response.data.results || []
                    this.loadng = false
                }).catch(error => {
                    console.log(error)
                });
            },


        }
    }
</script>

<style scoped>
    .tab-content.col-10 {
        padding: 0
    }
</style>