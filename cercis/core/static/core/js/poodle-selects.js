document.addEventListener("DOMContentLoaded", function () {
    var color_choice = new Choices(
        document.getElementById('color'), {
            itemSelectText: '',


        }).setChoices(function () {
        return fetch(
                CONFIG['color_list_url']
            )
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                return data.results.map(function (color) {
                    return {
                        value: color.id,
                        label: color.text
                    };
                });
            });
    });

    var sex_choice = new Choices(
        document.getElementById('sex'), {
            itemSelectText: '',


        }).setChoices(
        [{
                value: 'M',
                label: 'Dog',
            },
            {
                value: 'F',
                label: 'Bitch'
            },
            {
                value: 'U',
                label: 'Unknown'
            },
        ],
    );


    var variety_choice = new Choices(
        document.getElementById('variety'), {
            itemSelectText: '',
        }).setChoices(
        [{
                value: 'S',
                label: 'Standard',
            },
            {
                value: 'M',
                label: 'Miniature/Medium/Moyan'
            },
            {
                value: 'D',
                label: 'Dwarf'
            },
            {
                value: 'T',
                label: 'Toy'
            }
        ],
    );


});