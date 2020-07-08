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


                <b-form-group label="Prefix Titles" label-for="titles_prefix">
                    <v-select multiple label="abbr" v-model="poodle.titles_prefix" :options="title.options"
                        @search="searchTitle($event)">
                        <li slot="list-footer" class="pagination">
                            <b-button @click.prevent="searchTitle(title.search, title.previous)"
                                :disabled="!title.previous">Prev</b-button>
                            <b-button @click.prevent="searchTitle(title.search, title.next)" :disabled="!title.next">
                                Next</b-button>
                        </li>
                    </v-select>
                </b-form-group>

                <b-form-group label="Registered Name" label-for="registered-name">
                    <b-form-input id="registered-name" v-model="poodle.name_registered" trim></b-form-input>
                </b-form-group>

                <b-form-group label="Suffix Titles" label-for="titles_suffix">
                    <v-select multiple label="abbr" v-model="poodle.titles_suffix" :options="title.options"
                        @search="searchTitle($event)">
                        <li slot="list-footer" class="pagination">
                            <b-button @click.prevent="searchTitle(title.search, title.previous)"
                                :disabled="!title.previous">Prev</b-button>
                            <b-button @click.prevent="searchTitle(title.search, title.next)" :disabled="!title.next">
                                Next</b-button>
                        </li>
                    </v-select>
                </b-form-group>

                <b-form-group label="Honorifics" label-for="honorifics">
                    <b-form-input id="honorifics" v-model="poodle.honorifics"></b-form-input>
                </b-form-group>

                <b-form-group label="Sire" label-for="sire">
                    <v-select label="name_registered" :options="sire.options" @search="searchSire($event)"
                        v-model="poodle.sire">
                        <li slot="list-footer" class="pagination">
                            <b-button @click.prevent="searchSire(sire.search, sire.previous)"
                                :disabled="!sire.previous">Prev</b-button>
                            <b-button @click.prevent="searchSire(sire.search, sire.next)" :disabled="!sire.next">Next
                            </b-button>
                        </li>
                    </v-select>
                </b-form-group>

                <b-form-group label="Dam" label-for="dam">
                    <v-select label="name_registered" :options="dam.options" @search="searchDam($event)"
                        v-model="poodle.dam">
                        <li slot="list-footer" class="pagination">
                            <b-button @click.prevent="searchDam(dam.search, dam.previous)" :disabled="!dam.previous">
                                Prev</b-button>
                            <b-button @click.prevent="searchDam(dam.search, dam.next)" :disabled="!dam.next">Next
                            </b-button>
                        </li>
                    </v-select>
                </b-form-group>

                <b-form-group label="Color" label-for="color">
                    <v-select label="text" :options="options.color" @search="searchColor($event)"
                        v-model="poodle.color">
                    </v-select>
                    <b-form-text v-if="poodle.color && poodle.color.text!=poodle.pd_color" class="help-text">
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
                    <v-select multiple label="full_name" v-model="poodle.owners" :options="owner.options"
                        @search="searchOwner($event)">
                        <li slot="list-footer" class="pagination">
                            <b-button @click.prevent="searchOwner(owner.search, owner.previous)"
                                :disabled="!owner.previous">Prev</b-button>
                            <b-button @click.prevent="searchOwner(owner.search, owner.next)" :disabled="!owner.next">
                                Next</b-button>
                        </li>
                    </v-select>
                </b-form-group>

                <b-form-group label="Breeders" label-for="breeders">
                    <v-select multiple label="full_name" v-model="poodle.breeders" :options="breeder.options"
                        @search="searchBreeder($event)">
                        <li slot="list-footer" class="pagination">
                            <b-button @click.prevent="searchBreeder(breeder.search, breeder.previous)"
                                :disabled="!breeder.previous">Prev</b-button>
                            <b-button @click.prevent="searchBreeder(breeder.search, breeder.next)"
                                :disabled="!breeder.next">Next</b-button>
                        </li>
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
                <b-button variant="outline-warning" type="reset">
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
                    color: [],
                    variety: [],
                    origin_country: [],
                },
                title: {
                    options: [],
                    next: null,
                    previous: null,
                    count: null,
                },
                sire: {
                    options: [],
                    next: null,
                    previous: null,
                    count: null,
                },
                dam: {
                    options: [],
                    next: null,
                    previous: null,
                    count: null,
                },
                owner: {
                    options: [],
                    next: null,
                    previous: null,
                    count: null,
                },
                breeder: {
                    options: [],
                    next: null,
                    previous: null,
                    count: null,
                },
                showForm: true,
                perms: perms,
                config: config,

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
            searchColor: function (search) {
                if (search.length < 3) {
                    return
                }
                this.loading = true;
                var url = config.api_search_color(search)
                return axios.get(url).then((response) => {
                    this.options.color = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchTitle: function (search) {
                if (search.length < 1) {
                    return
                }
                this.loading = true;
                var url = config.api_search_title(search)
                return axios.get(url).then((response) => {
                    this.options.title = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchCountry: function (search) {
                if (search.length < 3) {
                    return
                }
                this.loading = true;
                var url = config.api_search_country(search)
                return axios.get(url).then((response) => {
                    this.options.origin_country = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchBreeder: function (search, page_url) {
                if (search.length < 3) {
                    return
                }

                this.loading = true
                var url = ''
                if (page_url) {
                    url = page_url
                } else {
                    url = config.api_search_person(search)
                    this.breeder.search = search
                }

                return axios.get(url).then((response) => {
                    console.log(response)
                    this.breeder.count = response.data.count
                    this.breeder.next = response.data.next
                    this.breeder.previous = response.data.previous
                    this.breeder.options = response.data.results || []
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchOwner: function (search, page_url) {
                if (search.length < 3) {
                    return
                }
                this.loading = true;
                var url = ''
                if (page_url) {
                    url = page_url
                } else {
                    url = config.api_search_person(search)
                    this.owner.search = search
                }
                return axios.get(url).then((response) => {
                    this.owner.count = response.data.count
                    this.owner.next = response.data.next
                    this.owner.previous = response.data.previous
                    this.owner.options = response.data.results || []
                    this.loading = false

                }).catch(error => {
                    console.log(error)
                });
            },
            searchDam: function (search, page_url) {
                if (search.length < 5) {
                    return
                }
                this.loading = true;

                var url = ''
                if (page_url) {
                    url = page_url
                } else {
                    url = url = config.api_search_poodle_parent('F', search)
                    this.dam.search = search
                }

                return axios.get(url).then((response) => {
                    this.dam.count = response.data.count
                    this.dam.next = response.data.next
                    this.dam.previous = response.data.previous
                    this.dam.options = response.data.results || []
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchSire: function (search, page_url) {
                if (search.length < 5) {
                    return
                }
                this.loading = true;
                var url = ''
                if (page_url) {
                    url = page_url
                } else {
                    url = url = config.api_search_poodle_parent('M', search)
                    this.sire.search = search
                }
                return axios.get(url).then((response) => {
                    this.sire.count = response.data.count
                    this.sire.next = response.data.next
                    this.sire.previous = response.data.previous
                    this.sire.options = response.data.results || []
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
        }
    }
</script>