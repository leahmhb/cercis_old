<template>
    <div class="poodle-list-item">
        <b-list-group-item :to="{name: 'poodle-detail', params: {slug:  poodle.slug }}" class="flex-column align-items-start">
            <div class="d-flex w-100 justify-content-between align-items-center">
                <h4 class="mb-1 text-condensed">
                    {{ poodle.name_registered }}
                    <small v-if="poodle.name_call">"{{ poodle.name_call }}"</small>
                </h4>
                <div>
                    <span v-if="poodle.color_text" class="badge badge-light">{{ poodle.color_text }}</span>
                    <i :class="['d-inline', 'float-right', 'fas', iconClass]" :title="poodle.sex"></i>
                </div>
            </div>
            <div class="d-flex flex-row justify-content-between align-items-center">
                <span v-if="displaySire" class="text-thin text-condensed">{{ poodle.sire }}</span>
                <span>{{ displayX }}</span>
                <span v-if="displayDam" class="text-thin text-condensed">{{ poodle.dam }}</span>
            </div>
        </b-list-group-item>
    </div>
</template>

<script>
    export default {
        name: 'PoodleListItem',
        props: [
            'poodle',
            'type'
        ],
        mounted: function () {},
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
            displaySire: function () {
                return this.type != 'sireside' && this.type != 'full' && this.poodle.sire
            },
            displayDam: function () {
                return this.type != 'damside' && this.type != 'full' && this.poodle.dam
            },
            displayX: function () {
                if (this.type == 'full') {
                    return ''
                } else if (!this.displayDam) {
                    return 'x Dam'
                } else if (!this.displaySire) {
                    return 'Sire x'
                } else {
                    return ''
                }
            }
        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>