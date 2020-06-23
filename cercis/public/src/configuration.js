const DEVELOPMENT_SERVER_CONFIGURATION = {
    baseUrl() {
        return process.env.BASE_URL;
    },
    endpoints: {
        home() {
            return `http://localhost:8000/`;
        },
        about() {
            `http://localhost:8000/about/`
        },
        api(model, slug) {
            var url = `http://localhost:8000/api/${model}/`
            if (slug) {
                url += slug + '/'
            }
            return url
        },
        api_params(model, params) {
            var url = `http://localhost:8000/api/${model}/?`
            if (params) {
                for (var p in params) {
                    url += `${p.param}=${p.param_value}&`
                }

            }
            return url
        },
        accounts(action) {
            return `http://localhost:8000/accounts/${action}/`;
        },
        admin(app, model, id, action) {
            if (app) {
                return `http://localhost:8000/admin/${app}/${model}/${id}/${action}/`;
            } else {
                return `http://localhost:8000/admin/`;
            }
        },
        core(model, action, slug) {
            if (slug) {
                return `http://localhost:8000/core/${model}/${action}/${slug}/`;
            } else {
                return `http://localhost:8000/core/${model}/${action}/`;
            }
        },
        media() {
            return "http://localhost:8000/media/";
        },
        users(slug) {
            return `http://localhost:8000/users/${slug}/`;
        },
        perms() {
            return {
                'core': {
                    'change_poodle': true
                }
            }
        },
        request() {
            return {
                'user': {
                    'is_authenticated': true
                }
            }
        },
        user() {
            return {
                'is_superuser': true
            }
        }
    },
};

const PRODUCTION_SERVER_CONFIGURATION = {
    baseUrl() {
        return document.querySelector('input[name="server-settings-BASEURL"]')
            .value;
    },
    endpoints: {
        color() {
            return document.querySelector(
                'input[name="server-settings-COLORENDPOINT"]'
            ).value;
        },
        country() {
            return document.querySelector(
                'input[name="server-settings-COUNTRYENDPOINT"]'
            ).value;
        },
        filter() {
            return document.querySelector(
                'input[name="server-settings-FILTERENDPOINT"]'
            ).value;
        },
        poodle() {
            return document.querySelector(
                'input[name="server-settings-POODLEENDPOINT"]'
            ).value;
        },
        person() {
            return document.querySelector(
                'input[name="server-settings-PERSONENDPOINT"]'
            ).value;
        },
        image() {
            return document.querySelector(
                'input[name="server-settings-IMAGEENDPOINT"]'
            ).value;
        }
    },
};

export const SERVER_CONFIGURATION =
    process.env.NODE_ENV === "production" ?
    PRODUCTION_SERVER_CONFIGURATION :
    DEVELOPMENT_SERVER_CONFIGURATION;

export default SERVER_CONFIGURATION;