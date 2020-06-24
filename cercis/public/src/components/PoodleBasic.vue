<template>
    <div id="basic">
        <article v-if=!showForm>
            <h5 v-if="poodle.honorifics" class="section-header text-center text-thin mb-2">
                {{ poodle.honorifics }}
            </h5>
            <div class="row">
                <div class="col">
                    <table class="table table-sm">
                        <tbody>
                            <tr>
                                <th>Sire</th>
                                <td>
                                    <a v-if="poodle.sire" :href="config.core('poodle', 'detail', poodle.sire.slug)">
                                        {{ poodle.sire.name_registered }}
                                    </a>
                                </td>
                            </tr>
                            <tr>
                                <th>Color</th>
                                <td v-if="poodle.color">{{ poodle.color.text }}</td>
                            </tr>
                            <tr>
                                <th>Origin Country</th>
                                <td v-if="poodle.origin_country">{{ poodle.origin_country.text }}</td>
                            </tr>
                            <tr>
                                <th>Owners</th>
                                <td>
                                    <span v-for="(p, i) in poodle.owners" v-bind:key="p.id">
                                        {{ p.full_name }}<span v-if="i+1 < poodle.owners.length">, </span>
                                    </span>
                                </td>
                            </tr>
                            <tr>
                                <th>DOB</th>
                                <td>{{ poodle.dob }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col">
                    <table class="table table-sm">
                        <tbody>
                            <tr>
                                <th>Dam</th>
                                <td>
                                    <a v-if="poodle.dam" :href="config.core('poodle', 'detail', poodle.dam.slug)">
                                        {{ poodle.dam.name_registered }}
                                    </a>
                                </td>
                            </tr>
                            <tr>
                                <th>Variety</th>
                                <td>{{ displayVariety }}</td>
                            </tr>
                            <tr>
                                <th>Sex</th>
                                <td>
                                    <i :class="['fas', iconClass]" :title="poodle.sex"></i>
                                </td>
                            </tr>
                            <tr>
                                <th>Breeders</th>
                                <td>
                                    <span v-for="(p, i) in poodle.breeders" v-bind:key="p.id">
                                        {{ p.full_name }}<span v-if="i+1 < poodle.owners.length">, </span>
                                    </span>
                                </td>
                            </tr>
                            <tr>
                                <th>DOD</th>
                                <td>{{ poodle.dod }} </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </article>
        <article v-else>
            <form :id="formRef" :ref="formRef" method="post" @submit.prevent="changePoodle(formRef)">

                <b-form-group label="Call Name" label-for="call-name">
                    <b-form-input id="call-name" v-model="poodle.name_call" trim></b-form-input>
                </b-form-group>

                <b-form-group label="Registered Name" label-for="registered-name">
                    <b-form-input id="registered-name" v-model="poodle.name_registered" trim></b-form-input>
                </b-form-group>

                <b-form-group label="Honorifics" label-for="honorifics">
                    <b-form-input id="honorifics" v-model="poodle.honorifics"></b-form-input>
                </b-form-group>

                <b-form-group label="Sire" label-for="sire">
                    <v-select label="name_registered" :options="options.sire" @search="searchSire($event)"
                        v-model="poodle.sire">
                    </v-select>
                </b-form-group>

                <b-form-group label="Dam" label-for="dam">
                    <v-select label="name_registered" :options="options.dam" @search="searchDam($event)"
                        v-model="poodle.dam">
                    </v-select>
                </b-form-group>

                <b-form-group label="Color" label-for="color">
                    <v-select label="text" :options="options.color" @search="searchColor($event)"
                        v-model="poodle.color">
                    </v-select>
                    <b-form-text v-if="poodle.color.text!=poodle.pd_color" class="help-text">
                        Please select a color close to {{ poodle.pd_color }}
                    </b-form-text>
                </b-form-group>

                <b-form-group label="Variety" label-for="variety">
                    <v-select label="label" :options="options.variety" :reduce="variety => variety.code"
                        v-model="poodle.variety">
                    </v-select>
                    <b-form-text v-if="poodle.variety!=poodle.pd_variety" class="help-text">
                        Please select a variety close to {{ poodle.pd_variety }}
                    </b-form-text>
                </b-form-group>

                <b-form-group label="Origin Country" label-for="origin_country">
                    <v-select label="text" :options="options.origin_country" @search="searchCountry($event)"
                        v-model="poodle.origin_country">
                    </v-select>
                </b-form-group>

                <b-form-group label="Sex" label-for="sex">
                    <v-select label="label" :options="options.sex" :reduce="sex => sex.code" v-model="poodle.sex">
                    </v-select>
                </b-form-group>

                <b-form-group label="Owners" label-for="owners">
                    <v-select label="full_name" v-model="poodle.owners" :options="options.owner"
                        @search="searchOwner($event)">
                    </v-select>
                </b-form-group>

                <b-form-group label="Breeders" label-for="breeders">
                    <v-select label="full_name" v-model="poodle.breeders" :options="options.breeder"
                        @search="searchBreeder($event)">
                    </v-select>
                </b-form-group>

                <b-form-group label="Born" label-for="dob">
                    <b-form-input type="text" id="dob" v-model="poodle.dob" trim placeholder="--/--/----">
                    </b-form-input>
                </b-form-group>

                <b-form-text v-if="poodle.dob_dod">Please select dates close to {{ poodle.dob_dod }} </b-form-text>

                <b-form-group label="Died" label-for="dod">
                    <b-form-input type="text" id="dod" v-model="poodle.dod" trim placeholder="--/--/----">
                    </b-form-input>
                </b-form-group>

            </form>
        </article>

        <div v-if="perms.core.change_poodle" class="mt-4 mb-0 d-flex flex-row justify-content-between align-items-end">
            <b-button v-if="showForm" variant="outline-secondary" @click="showForm=!showForm">
                <i v-if="showForm" class="fas fa-toggle-off"></i> Back
            </b-button>
            <b-button v-else variant="outline-info" @click="showForm=!showForm">
                <i class="fas fa-toggle-on"></i> Update
            </b-button>
            <b-btn-group v-if="showForm">
                <b-button variant="outline-secondary" type="reset">
                    <i class="fas fa-eraser"></i> Reset
                </b-button>
                <b-button variant="success" type="subit" @click="changePoodle(formRef)">
                    <i class="fas fa-save"></i> Save
                </b-button>
            </b-btn-group>
        </div>
    </div>
</template>

<script>
    import VueSelect from 'vue-select'
    import configuration from './../configuration.js'
    import axios from 'axios'

    let perms = configuration.perms();
    let config = configuration.endpoints;
    export default {
        name: 'PoodleBasic',
        props: [
            'poodle',
            'formRef'
        ],
        components: {
            'v-select': VueSelect,
        },
        computed: {
            iconClass: function () {
                var s = this.poodle.sex
                if (s == 'F') {
                    return 'fa-venus text-female';
                } else if (s == 'M') {
                    return 'fa-mars text-male';
                } else {
                    return 'fa-genderless text-light';
                }
            },
            displayVariety: function () {
                var v = this.poodle.variety
                if (v == 'S') {
                    return 'Standard';
                } else if (v == 'M') {
                    return 'Miniature/Medium';
                } else if (v == 'D') {
                    return 'Dwarf';
                } else if (v == 'T') {
                    return 'Toy';
                } else {
                    return '';
                }
            },
        },
        data: function () {
            return {
                options: {
                    sire: [],
                    dam: [],
                    color: [],
                    variety: [],
                    origin_country: [],
                    owner: [],
                    breeder: [],
                },
                showForm: false,
                perms: perms,
                config: config
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
        },
        methods: {
            /**
             * @param search
             * @param q
             * @param options
             * @param url
             */
            // search: function (search, q, options, url) {
            //     var self = this;
            //     var params = new URLSearchParams();
            //     params.append(q, search);
            //     url += '?' + params

            //     return axios.get(url).then((response) => {
            //         options = response.data.results || [];
            //         console.log(options)
            //         self.loading = false
            //     }).catch(error => {
            //         console.log(error)
            //     });
            // },
            searchColor: function (search) {                
                this.loading = true;
                var url = config.api_search_color(search)
                return axios.get(url).then((response) => {
                    this.options.color = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchCountry: function (search) {
                this.loading = true;
                var url = config.api_search_country(search)
                return axios.get(url).then((response) => {
                    this.options.origin_country = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchBreeder: function (search) {
                var url = config.api_seach_person(search)
                return axios.get(url).then((response) => {
                    this.options.breeder = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchOwner: function (search) {
                this.loading = true;
               var url = config.api_search_person(search)
                return axios.get(url).then((response) => {
                    this.options.owner = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchDam: function (search) {
                this.loading = true;                
                var url = config.api_search_poodle_parent('F', search)
                return axios.get(url).then((response) => {
                    this.options.dam = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchSire: function (search) {
                this.loading = true;
                var url = config.api_search_poodle_parent('M', search)
                return axios.get(url).then((response) => {
                    this.options.sire = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
        }
    }
</script>