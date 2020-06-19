const DEVELOPMENT_SERVER_CONFIGURATION = {
    baseUrl() {
        return process.env.BASE_URL;
    },
    endpoints: {
        color() {
            return "http://localhost:8000/api/color/";
        },
        country() {
            return "http://localhost:8000/api/country/";
        },
        filter() {
            return "http://localhost:8000/api/filter/";
        },
        poodle() {
            return "http://localhost:8000/api/poodle/";
        },
        person() {
            return "http://localhost:8000/api/person/";
        },
        image() {
            return "http://localhost:8000/api/image/";
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