document.addEventListener("DOMContentLoaded", function () {
    Vue.component('v-select', VueSelect.VueSelect);
    var detail = new Vue({
        el: "#detail",
        delimiters: ['{$', '$}'],
        data: {
            showImageForm: false,
            showBasicForm: false,
            showRegistrationForm: false,
            showHealthForm: false,
            showCommentsForm: false,
            loading: false,
            slide: 0,
            sliding: null,
            poodle: {},
            images: [],
            showErrorAlert: false,
            errors: [],
            image: {
                caption: '',
                comments: '',
                path: '',
            },
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

            Promise.all([this.getPoodle(), this.getImages()]);
        },
        computed: {
            adminApproved: function () {
                return this.poodle.is_viewable
            },
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
            displayVariety: function () {
                v = this.poodle.variety
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
        methods: {
            onSlideStart(slide) {
                this.sliding = true
            },
            onSlideEnd(slide) {
                this.sliding = false
            },
            getPoodle: function () {
                this.loading = true
                var url = CONFIG['poodle_detail_url']
                return axios.get(url).then((response) => {
                    this.poodle = response.data || []
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            getImages: function () {
                this.loading = true
                var url = CONFIG['poodle_image_list_url']
                return axios.get(url).then((response) => {
                    this.images = response.data.results || []
                    this.loadng = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchColor: function (search) {
                this.loading = true;
                var url = CONFIG['color_list_url'] + '?text=' + search
                return axios.get(url).then((response) => {
                    this.options.color = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchCountry: function (search) {
                this.loading = true;
                var url = CONFIG['country_list_url'] + '?text=' + search
                return axios.get(url).then((response) => {
                    this.options.origin_country = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchBreeder: function (search) {
                var url = CONFIG['person_list_url'] + '?full_name=' + search
                return axios.get(url).then((response) => {
                    this.options.breeder = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchOwner: function (search) {
                this.loading = true;
                var url = CONFIG['person_list_url'] + '?full_name=' + search
                return axios.get(url).then((response) => {
                    this.options.owner = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchDam: function (search) {
                this.loading = true;
                var url = CONFIG['poodle_filter_url'] + '?sex=F&name_registered=' + search
                return axios.get(url).then((response) => {
                    this.options.dam = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            searchSire: function (search) {
                this.loading = true;
                var url = CONFIG['poodle_filter_url'] + '?sex=M&name_registered=' + search
                return axios.get(url).then((response) => {
                    this.options.sire = response.data.results || [];
                    this.loading = false
                }).catch(error => {
                    console.log(error)
                });
            },
            /**
             * @param loading
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

            // search: _.debounce((loading, search, q, options, url) => {
            //     // /api/people?q=Ryan
            //     axios.get(url, {
            //         params: {
            //             q: search
            //         }
            //     }).then(function(response){
            //         options = response.data.results;
            //         this.loading = false
            //     })
            // }, 350),  
            submitImage: function () {
                this.loading = true
                var url = CONFIG['image_list_url']
                var formData = new FormData()
                var file = this.$refs["image-path"].files[0]

                if (!this.image.caption || !file) {
                    this.errors.push("Image file and caption are required.")
                    return
                }

                formData.append('path', file)
                formData.append('poodle', this.poodle.id)
                formData.append('caption', this.image.caption)

                if (this.image.caption) {
                    formData.append('comments', this.image.comments)
                }

                var self = this

                let promise = axios.post(url,
                    formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        },
                    })
                return promise.then((response) => {
                    console.log(response)
                    this.images = response.data.results;
                    this.loading = false
                    this.$refs['image-modal'].hide()
                    this.getImages()
                    this.resetImageForm()
                }).catch(error => {
                    console.log(error)
                });
            },
            resetImageForm: function () {
                this.image = {}
                this.errors = []
                var form = document.getElementById("image-form")
                form.reset()
            },
            closeErrorAlert: function () {
                this.errors = []
            },
        }
    });
});