    

    var poodleListItem = Vue.component('poodle-list-item', {
        delimiters: ['{$', '$}'],
        props: [
            'poodle',
            'type'
        ],
        mounted: function () {},
        computed: {
            iconClass: function () {
                s = this.poodle.sex
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
                } 
            }
        },
        template: '#poodle-list-item-template'
    });