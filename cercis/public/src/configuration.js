const DEVELOPMENT_SERVER_CONFIGURATION = {
    baseUrl() {
        return process.env.BASE_URL;
    },
    endpoints: {
        color() {
            return `http://localhost:8000/api/color/`
        },
        title() {
            return `http://localhost:8000/api/title/`
        },
        country() {
            return `http://localhost:8000/api/country/`
        },
        poodle() {
            return `http://localhost:8000/api/poodle/`
        },
        person() {
            return `http://localhost:8000/api/person/`
        },
        filter() {
            return `http://localhost:8000/api/filter/`
        },
        image() {
            return `http://localhost:8000/api/image/`
        },
        accounts(action) {
            return `http://localhost:8000/accounts/${action}`;
        },
        admin() {
            return `http://localhost:8000/admin/`;
        },
        media() {
            return "http://localhost:8000/media/";
        },
        users(username) {
            return `http://localhost:8000/users/${username}`;
        },
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
};

const PRODUCTION_SERVER_CONFIGURATION = {
    baseUrl() {
        return document.querySelector('input[name="server-settings-BASEURL"]')
            .value;
    },
    endpoints: {

        poodle() {
            return document.querySelector(
                'input[name="server-settings-POODLE-ENDPOINT"]'
            ).value;
        },
        person() {
            return document.querySelector(
                'input[name="server-settings-PERSON-ENDPOINT"]'
            ).value;
        },
        color() {
            return document.querySelector(
                'input[name="server-settings-COLOR-ENDPOINT"]'
            ).value;
        },
        title() {
            return document.querySelector(
                'input[name="server-settings-TITLE-ENDPOINT"]'
            ).value;
        },
        country() {
            return document.querySelector(
                'input[name="server-settings-COUNTRY-ENDPOINT"]'
            ).value;
        },
        filter() {
            return document.querySelector(
                'input[name="server-settings-FILTER-ENDPOINT"]'
            ).value;
        },
        image() {
            return document.querySelector(
                'input[name="server-settings-IMAGE-ENDPOINT"]'
            ).value;
        },
        accounts(action) {
            return document.querySelector(
                'input[name="server-settings-ACCOUNTS-ENDPOINT"]'
            ).value + action;
        },
        admin() {
            return document.querySelector(
                'input[name="server-settings-ADMIN-ENDPOINT"]'
            ).value;
        },
        media() {
            return document.querySelector(
                'input[name="server-settings-MEDIA-ENDPOINT"]'
            ).value;
        },
        users(username) {
            return document.querySelector(
                'input[name="server-settings-USERS-ENDPOINT"]'
            ).value + username
        },
    },
};

export const SERVER_CONFIGURATION =
    process.env.NODE_ENV === "production" ?
    PRODUCTION_SERVER_CONFIGURATION :
    DEVELOPMENT_SERVER_CONFIGURATION;

export default SERVER_CONFIGURATION;