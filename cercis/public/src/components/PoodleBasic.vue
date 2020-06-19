<template>
    <div id="basic">
        <article v-if=!showBasicForm>
            <h4 class="section-header text-center text-condensed mb-1">
                <a v-if="poodle.sire" :href="poodle.sire.url">
                    {$ poodle.sire.name_registered $}
                </a>
                x
                <a v-if="poodle.dam" :href="poodle.dam.url">
                    {$ poodle.dam.name_registered $}
                </a>
            </h4>
            <h5 class="section-header text-center text-thin mb-2">
                Origin Country {$ poodle.origin_country.text $}
            </h5>
            <div class="row">
                <div class="col">
                    <table class="table table-sm">
                        <tbody>
                            <tr>
                                <th>Color</th>
                                <td>{$ poodle.color.text $}</td>
                            </tr>
                            <tr>
                                <th>Honorifics</th>
                                <td>{$ poodle.honorifics $}</td>
                            </tr>
                            <tr>
                                <th>Owners</th>
                                <td>
                                    <span v-for="(p, i) in poodle.owners" v-bind:key="p.id">
                                        {$ p.full_name $}<span v-if="i+1 < poodle.owners.length">, </span>
                                    </span>
                                </td>
                            </tr>
                            <tr>
                                <th>DOB</th>
                                <td>{$ poodle.dob $}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col">
                    <table class="table table-sm">
                        <tbody>
                            <tr>
                                <th>Variety</th>
                                <td>{$ displayVariety $}</td>
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
                                        {$ p.full_name $}<span v-if="i+1 < poodle.owners.length">, </span>
                                    </span>
                                </td>
                            </tr>
                            <tr>
                                <th>DOD</th>
                                <td>{$ poodle.dod $} </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </article>
        <article v-if="showBasicForm">
            <form id="basic-form" ref="basic-form" method="post" @submit.prevent="changePoodle('basic-form')">
                <b-form-row>
                    <b-col cols="2">
                        <b-form-group label="Call Name" label-for="call-name">
                            <b-form-input id="call-name" v-model="poodle.name_call" trim></b-form-input>
                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group label="Registered Name" label-for="registered-name">
                            <b-form-input id="registered-name" v-model="poodle.name_registered" trim></b-form-input>
                        </b-form-group>
                    </b-col>
                </b-form-row>


                <b-form-row>
                    <b-col>

                        <b-form-group label="Color" label-for="color">
                            <v-select label="text" :options="options.color" @search="searchColor($event)"
                                v-model="poodle.color">
                            </v-select>
                            <b-form-text v-if="poodle.color.text!=poodle.pd_color" class="help-text">
                                Please select a color close to {$ poodle.pd_color $}
                            </b-form-text>
                        </b-form-group>
                    </b-col>
                    <b-col>

                        <b-form-group label="Variety" label-for="variety">
                            <v-select label="label" :options="options.variety" :reduce="variety => variety.code"
                                v-model="poodle.variety">
                            </v-select>
                            <b-form-text v-if="poodle.variety!=poodle.pd_variety" class="help-text">
                                Please select a variety close to {$ poodle.pd_variety $}
                            </b-form-text>
                        </b-form-group>
                    </b-col>

                    <b-col>
                        <b-form-group label="Origin Country" label-for="origin_country">

                            <v-select label="text" :options="options.origin_country" @search="searchCountry($event)"
                                v-model="poodle.origin_country">
                            </v-select>
                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group label="Sex" label-for="sex">
                            <v-select label="label" :options="options.sex" :reduce="sex => sex.code"
                                v-model="poodle.sex">
                            </v-select>
                        </b-form-group>
                    </b-col>
                </b-form-row>

                <b-form-row>
                    <b-col>
                        <b-form-group label="Honorifics" label-for="honorifics">
                            <b-form-input id="honorifics" v-model="poodle.honorifics" size="sm"></b-form-input>
                        </b-form-group>
                    </b-col>
                </b-form-row>


                <b-form-row>
                    <b-col>
                        <b-form-group label="Sire" label-for="sire">
                            <v-select label="name_registered" :options="options.sire" @search="searchSire($event)"
                                v-model="poodle.sire">
                            </v-select>
                        </b-form-group>
                    </b-col>
                </b-form-row>


                <b-form-row>
                    <b-col>
                        <b-form-group label="Dam" label-for="dam">
                            <v-select label="name_registered" :options="options.dam" @search="searchDam($event)"
                                v-model="poodle.dam">
                            </v-select>
                        </b-form-group>
                    </b-col>
                </b-form-row>

                <b-form-row>
                    <b-col>
                        <b-form-group label="Owners" label-for="owners">
                            <v-select label="full_name" v-model="poodle.owners" :options="options.owner"
                                @search="searchOwner($event)">
                            </v-select>
                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group label="Breeders" label-for="breeders">
                            <v-select label="full_name" v-model="poodle.breeders" :options="options.breeder"
                                @search="searchBreeder($event)">
                            </v-select>
                        </b-form-group>
                    </b-col>
                </b-form-row>

                <b-form-row>
                    <b-col>
                        <b-form-group label="Born" label-for="dob">
                            <b-form-input type="text" id="dob" v-model="poodle.dob" trim placeholder="--/--/----">
                            </b-form-input>
                        </b-form-group>
                    </b-col>
                    <b-form-text v-if="poodle.dob_dod">Please select dates close to {$ poodle.dob_dod $} </b-form-text>
                    <b-col>
                        <b-form-group label="Died" label-for="dod">
                            <b-form-input type="text" id="dod" v-model="poodle.dod" trim placeholder="--/--/----">
                            </b-form-input>
                        </b-form-group>
                    </b-col>

                </b-form-row>
            </form>

        </article>

        <div class="mt-4 mb-0 d-flex flex-row justify-content-between align-items-end">
            <b-button variant="outline-info" size="sm" @click="showBasicForm=!showBasicForm">
                <i v-if="showBasicForm" class="fas fa-toggle-off"></i>
                <i v-if="!showBasicForm" class="fas fa-toggle-on"></i> Update
            </b-button>
            <b-btn-group v-if="showBasicForm">
                <b-button variant="outline-secondary" size="sm" type="reset">
                    <i class="fas fa-eraser"></i> Reset
                </b-button>
                <b-button variant="success" size="sm" type="subit" @click="changePoodle('basic-form')">
                    <i class="fas fa-save"></i> Save
                </b-button>
            </b-btn-group>
        </div>
    </div>
</template>

<script>
  import VueSelect from 'vue-select'
    export default {
        name: 'PoodleBasic',
        delimiters: ['{$', '$}'],
        props: [
            'poodle',
            'showBasicForm'
        ],
        components: {
            'v-select': VueSelect
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
        }
    }
</script>