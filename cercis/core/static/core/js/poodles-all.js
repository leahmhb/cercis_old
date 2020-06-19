var table = new Vue({
    el: "#list",
    delimiters: ['{$', '$}'],
    data() {
        return {
            loading: false,
            items: [],
            pagination: {
                page: 1,
                perPage: 15,
                total: 0,
            },
            sort: {
                sortBy: 'dob',
                sortDesc: false,
            },
            filters: {
                name_registered: '',
                name_call: '',
                color: '',
                variety: '',
                person_owners: '',
                person_breeders: '',
                origin_country: ''
            },
            fields: [{
                    key: 'name_registered',
                    label: 'Registered',
                    sortable: true,
                },
                {
                    key: 'name_call',
                    label: 'Call',
                    sortable: true
                },
                {
                    key: 'dob',
                    label: 'DOB',
                    sortable: true
                },
                {
                    key: 'sex',
                    label: 'Sex',
                    sortable: true
                },
                {
                    key: 'color',
                    label: 'Color',
                    sortable: true
                },
                {
                    key: 'person_owners',
                    label: 'Owner',
                    sortable: true
                },
                {
                    key: 'person_breeders',
                    label: 'Breeder',
                    sortable: true
                },
                {
                    key: 'origin_country',
                    label: 'Origin',
                    sortable: true
                },
            ],
        }
    },
    mounted() {},
    computed: {},
    methods: {
        buildUrl(base_url) {
            var url = base_url + '?';
            const urlparams = new URLSearchParams();
            for (const [key, value] of Object.entries(this.filters)) {
                if (value) {
                    urlparams.append(key, value);
                }
            }
            urlparams.append('page', this.pagination.page);
            urlparams.append('perPage', this.pagination.perPage);

            url += urlparams.toString();

            console.log(url)

            return url;
        },
        checkFilters() {
            for (const [key, value] of Object.entries(this.filters)) {
                if (value) {
                    console.log(key)
                    return true
                }
            }
            return false;
        },
        getItems() {
            this.loading = true
            const url = this.buildUrl(CONFIG['poodle_filter_url'])

            if (url == 'api/poodle/?page=1&perPage=15') {
                this.loading = false
                this.items = []
            }

            let promise = axios.get(this.buildUrl(CONFIG['poodle_filter_url']))
            return promise.then((response) => {
                console.log(response)
                const items = response.data.results;
                this.pagination.total = response.data.count
                this.pagination.next = response.data.next
                this.pagination.previous = response.data.previous
                this.items = items || []
                this.loading = false
            }).catch(error => {

                return [];
            });




        }
    }
});