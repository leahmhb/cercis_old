var singleDog = Vue.component('single-dog', {
        delimiters: ['{$', '$}'],
        props: [
            'poodle',
        ],
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
             }
        },
        methods: {           
        },
        template: '#single-dog-template'
    });
