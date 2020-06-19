<template>
    <div id="3-gen-pedigree">
        <b-container>
            <b-row class="d-flex align-items-center gen-1">
                <b-col cols="3">
                    {$ poodle.name_registered $}
                </b-col><!-- THIS poodle -->
                <b-col>
                    <b-row class="d-flex align-items-center gen-2">
                        <b-col cols="4">
                            <single-dog v-if="poodle.sire" :poodle="poodle.sire"></single-dog>
                        </b-col>
                        <b-col>
                            <b-row class="d-flex align-items-center gen-3">
                                <b-col cols="6">
                                    <single-dog v-if="poodle.sire.sire" :poodle="poodle.sire.sire"></single-dog>
                                </b-col>
                                <b-col>
                                    <b-row class="d-flex align-items-center">
                                        <b-col>
                                            <single-dog v-if="poodle.sire.sire.sire" :poodle="poodle.sire.sire.sire">
                                            </single-dog>
                                            <hr>
                                            <single-dog v-if="poodle.sire.sire.dam" :poodle="poodle.sire.sire.dam">
                                            </single-dog>
                                        </b-col>
                                </b-col>
                            </b-row>
                            <hr>
                            <b-row class="d-flex align-items-center gen-3">
                                <b-col cols="6">
                                    <single-dog v-if="poodle.sire.dam" :poodle="poodle.sire.dam"></single-dog>
                                </b-col>
                                <b-col>
                                    <b-row class="d-flex align-items-center gen-4">
                                        <b-col>
                                            <single-dog v-if="poodle.sire.dam.sire" :poodle="poodle.sire.dam.sire">
                                            </single-dog>
                                            <hr>
                                            <single-dog v-if="poodle.sire.dam.dam" :poodle="poodle.sire.dam.dam">
                                            </single-dog>
                                        </b-col>
                                    </b-row>
                                </b-col>
                            </b-row>
                        </b-col>
                    </b-row>
                    <hr>
                    <b-row class="d-flex align-items-center gen-2">
                        <b-col cols="4">
                            <single-dog v-if="poodle.dam" :poodle="poodle.dam"></single-dog>
                        </b-col>
                        <b-col>
                            <b-row class="d-flex align-items-center gen-3">
                                <b-col cols="6">
                                    <single-dog v-if="poodle.dam.sire" :poodle="poodle.dam.sire"></single-dog>
                                </b-col>
                                <b-col>
                                    <b-row class="d-flex align-items-center gen-4">
                                        <b-col>
                                            <single-dog v-if="poodle.dam.sire.sire" :poodle="poodle.dam.sire.sire">
                                            </single-dog>
                                            <hr>
                                            <single-dog v-if="poodle.dam.sire.dam" :poodle="poodle.dam.sire.dam">
                                            </single-dog>
                                        </b-col>
                                    </b-row>
                                </b-col>
                            </b-row>
                            <hr>
                            <b-row class="d-flex align-items-center gen-3">
                                <b-col cols="6">
                                    <single-dog v-if="poodle.dam.dam" :poodle="poodle.dam.dam"></single-dog>
                                </b-col>
                                <b-col>
                                    <b-row class="d-flex align-items-center gen-4">
                                        <b-col>
                                            <single-dog v-if="poodle.dam.dam.sire" :poodle="poodle.dam.dam.sire">
                                            </single-dog>
                                            <hr>
                                            <single-dog v-if="poodle.dam.dam.dam" :poodle="poodle.dam.dam.dam">
                                            </single-dog>
                                        </b-col>
                                    </b-row>
                                </b-col>
                            </b-row>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
        </b-container>

    </div>
</template>

<script>
    import SingleDog from './SingleDog'
    export default {
        name: 'ThreeGenPedigree',
        delimiters: ['{$', '$}'],
        props: [
            'poodle',
        ],
        components: {
            SingleDog,
        }
    }
</script>