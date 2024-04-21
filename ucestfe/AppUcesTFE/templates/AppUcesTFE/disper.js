<!-- IMPO-INCE -->

Highcharts.chart('container', {

    chart: {
        type: 'bubble',
        plotBorderWidth: 1,
        zoomType: 'xy'
    },

    legend: {
        enabled: false
    },

    title: {
        text: 'IMPO-INCE'
    },

    subtitle: {
        text: 'SUBTITLO, puedo usar html'
    },

    accessibility: {
        point: {
            valueDescriptionFormat: '{index}. {point.name}, Importancia: {point.x}, Incertidumbre: {point.y}, Influencia: {point.z}%.'
        }
    },

    xAxis: {
        gridLineWidth: 1,
        title: {
            text: 'IMportancia 0 a 10'
        },
        labels: {
            format: '{value} gr'
        },
        plotLines: [{
            color: 'black',
            dashStyle: 'dot',
            width: 2,
            value: 5,
            label: {
                rotation: 0,
                y: 15,
                style: {
                    fontStyle: 'italic'
                },
                text: 'Texto interno grafico'
            },
            zIndex: 3
        }],
        accessibility: {
            rangeDescription: 'Range: 1 to 10.'
        }
    },

    yAxis: {
        startOnTick: false,
        endOnTick: false,
        title: {
            text: 'Incertidumbre 0 a 10'
        },
        labels: {
            format: '{value} gr'
        },
        maxPadding: 0.2,
        plotLines: [{
            color: 'black',
            dashStyle: 'dot',
            width: 2,
            value: 5,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: 'texto interno 2',
                x: -10
            },
            zIndex: 3
        }],
        accessibility: {
            rangeDescription: 'Range: 0 to 160 grams.'
        }
    },

    tooltip: {
        useHTML: true,
        headerFormat: '<table>',
        pointFormat: '{point.country}',
        footerFormat: '</table>',
        followPointer: true
    },

    plotOptions: {
        series: {
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }
    },

    series: [{
        data: [
            { x: 95, y: 95, z: 13.8, name: 'BE', country: 'Belgium' },
            { x: 86.5, y: 102.9, z: 14.7, name: 'DE', country: 'Germany' },
            { x: 80.8, y: 91.5, z: 15.8, name: 'FI', country: 'Finland' },
            { x: 80.4, y: 102.5, z: 12, name: 'NL', country: 'Netherlands' },
            { x: 80.3, y: 86.1, z: 11.8, name: 'SE', country: 'Sweden' },
            { x: 78.4, y: 70.1, z: 16.6, name: 'ES', country: 'Spain' },
            { x: 74.2, y: 68.5, z: 14.5, name: 'FR', country: 'France' },
            { x: 73.5, y: 83.1, z: 10, name: 'NO', country: 'Norway' },
            { x: 71, y: 93.2, z: 24.7, name: 'UK', country: 'United Kingdom' },
            { x: 69.2, y: 57.6, z: 10.4, name: 'IT', country: 'Italy' },
            { x: 68.6, y: 20, z: 16, name: 'RU', country: 'Russia' },
            { x: 65.5, y: 8.4, z: 35.3, name: 'US', country: 'United States' },
            { x: 65.4, y: 50.8, z: 28.5, name: 'HU', country: 'Hungary' },
            { x: 63.4, y: 51.8, z: 15.4, name: 'PT', country: 'Portugal' },
            { x: 64, y: 82.9, z: 31.3, name: 'NZ', country: 'New Zealand' }
        ],
        colorByPoint: true
    }]

});





Highcharts.chart('container2', {

    chart: {
        type: 'bubble',
        plotBorderWidth: 1,
        zoomType: 'xy'
    },

    legend: {
        enabled: false
    },

    title: {
        text: 'INF-INC - MICMAC'
    },

    subtitle: {
        text: 'SUBTITLO, puedo usar html'
    },

    accessibility: {
        point: {
            valueDescriptionFormat: '{index}. {point.name}, Importancia: {point.x}, Incertidumbre: {point.y}, Influencia: {point.z}%.'
        }
    },

    xAxis: {
        gridLineWidth: 1,
        title: {
            text: 'IMportancia 0 a 10'
        },
        labels: {
            format: '{value} gr'
        },
        plotLines: [{
            color: 'black',
            dashStyle: 'dot',
            width: 2,
            value: 5,
            label: {
                rotation: 0,
                y: 15,
                style: {
                    fontStyle: 'italic'
                },
                text: 'Texto interno grafico'
            },
            zIndex: 3
        }],
        accessibility: {
            rangeDescription: 'Range: 1 to 10.'
        }
    },

    yAxis: {
        startOnTick: false,
        endOnTick: false,
        title: {
            text: 'Incertidumbre 0 a 10'
        },
        labels: {
            format: '{value} gr'
        },
        maxPadding: 0.2,
        plotLines: [{
            color: 'black',
            dashStyle: 'dot',
            width: 2,
            value: 5,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: 'texto interno 2',
                x: -10
            },
            zIndex: 3
        }],
        accessibility: {
            rangeDescription: 'Range: 0 to 160 grams.'
        }
    },

    tooltip: {
        useHTML: true,
        headerFormat: '<table>',
        pointFormat: '{point.country}',
        footerFormat: '</table>',
        followPointer: true
    },

    plotOptions: {
        series: {
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }
    },

    series: [{
        data: [
            { x: 95, y: 95, z: 13.8, name: 'BE', country: 'Belgium' },
            { x: 86.5, y: 102.9, z: 14.7, name: 'DE', country: 'Germany' },
            { x: 80.8, y: 91.5, z: 15.8, name: 'FI', country: 'Finland' },
            { x: 80.4, y: 102.5, z: 12, name: 'NL', country: 'Netherlands' },
            { x: 80.3, y: 86.1, z: 11.8, name: 'SE', country: 'Sweden' },
            { x: 78.4, y: 70.1, z: 16.6, name: 'ES', country: 'Spain' },
            { x: 74.2, y: 68.5, z: 14.5, name: 'FR', country: 'France' },
            { x: 73.5, y: 83.1, z: 10, name: 'NO', country: 'Norway' },
            { x: 71, y: 93.2, z: 24.7, name: 'UK', country: 'United Kingdom' },
            { x: 69.2, y: 57.6, z: 10.4, name: 'IT', country: 'Italy' },
            { x: 68.6, y: 20, z: 16, name: 'RU', country: 'Russia' },
            { x: 65.5, y: 8.4, z: 35.3, name: 'US', country: 'United States' },
            { x: 65.4, y: 50.8, z: 28.5, name: 'HU', country: 'Hungary' },
            { x: 63.4, y: 51.8, z: 15.4, name: 'PT', country: 'Portugal' },
            { x: 64, y: 82.9, z: 31.3, name: 'NZ', country: 'New Zealand' }
        ],
        colorByPoint: true
    }]

});






Highcharts.Templating.helpers.substr = (s, from, length) =>
    s.substr(from, length);


Highcharts.chart('container3', {

    chart: {
        type: 'heatmap',
        marginTop: 40,
        marginBottom: 80,
        plotBorderWidth: 1
    },


    title: {
        text: 'Sales per employee per weekday',
        style: {
            fontSize: '1em'
        }
    },

    xAxis: {
        categories: ['Alexander', 'Marie', 'Maximilian', 'Sophia', 'Lukas',
            'Maria', 'Leon', 'Anna', 'Tim', 'Laura']
    },

    yAxis: {
        categories: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        title: null,
        reversed: true
    },

    accessibility: {
        point: {
            descriptionFormat: '{(add index 1)}. ' +
                '{series.xAxis.categories.(x)} sales ' +
                '{series.yAxis.categories.(y)}, {value}.'
        }
    },

    colorAxis: {
        min: 0,
        minColor: '#FFFFFF',
        maxColor: Highcharts.getOptions().colors[0]
    },

    legend: {
        align: 'right',
        layout: 'vertical',
        margin: 0,
        verticalAlign: 'top',
        y: 25,
        symbolHeight: 280
    },

    tooltip: {
        format: '<b>{series.xAxis.categories.(point.x)}</b> sold<br>' +
            '<b>{point.value}</b> items on <br>' +
            '<b>{series.yAxis.categories.(point.y)}</b>'
    },

    series: [{
        name: 'Sales per employee',
        borderWidth: 1,
        data: [[0, 0, 0], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67],
            [1, 0, 92], [1, 1, 58], [1, 2, 78], [1, 3, 117], [1, 4, 48],
            [2, 0, 35], [2, 1, 15], [2, 2, 123], [2, 3, 64], [2, 4, 52],
            [3, 0, 72], [3, 1, 132], [3, 2, 114], [3, 3, 19], [3, 4, 16],
            [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 117], [4, 4, 115],
            [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 120],
            [6, 0, 13], [6, 1, 44], [6, 2, 88], [6, 3, 98], [6, 4, 96],
            [7, 0, 31], [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30],
            [8, 0, 85], [8, 1, 97], [8, 2, 123], [8, 3, 64], [8, 4, 84],
            [9, 0, 47], [9, 1, 114], [9, 2, 31], [9, 3, 48], [9, 4, 91]],
        dataLabels: {
            enabled: true,
            color: '#000000'
        }
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                yAxis: {
                    labels: {
                        format: '{substr value 0 1}'
                    }
                }
            }
        }]
    }

});






const data = [
    {
        id: '0.0',
        parent: '',
        name: 'The World'
    },
    {
        id: '1.3',
        parent: '0.0',
        name: 'Asia'
    },
    {
        id: '1.1',
        parent: '0.0',
        name: 'Africa'
    },
    {
        id: '1.2',
        parent: '0.0',
        name: 'America'
    },
    {
        id: '1.4',
        parent: '0.0',
        name: 'Europe'
    },
    {
        id: '1.5',
        parent: '0.0',
        name: 'Oceanic'
    },

    /* Africa */
    {
        id: '2.1',
        parent: '1.1',
        name: 'Eastern Africa'
    },

    {
        id: '2.5',
        parent: '1.1',
        name: 'Western Africa'
    },

    {
        id: '2.3',
        parent: '1.1',
        name: 'North Africa'
    },

    {
        id: '2.2',
        parent: '1.1',
        name: 'Central Africa'
    },

    {
        id: '2.4',
        parent: '1.1',
        name: 'South America'
    },

    /* America */
    {
        id: '2.9',
        parent: '1.2',
        name: 'South America'
    },

    {
        id: '2.8',
        parent: '1.2',
        name: 'Northern America'
    },

    {
        id: '2.7',
        parent: '1.2',
        name: 'Central America'
    },

    {
        id: '2.6',
        parent: '1.2',
        name: 'Caribbean'
    },

    /* Asia */
    {
        id: '2.13',
        parent: '1.3',
        name: 'Southern Asia'
    },

    {
        id: '2.11',
        parent: '1.3',
        name: 'Eastern Asia'
    },

    {
        id: '2.12',
        parent: '1.3',
        name: 'South-Eastern Asia'
    },

    {
        id: '2.14',
        parent: '1.3',
        name: 'Western Asia'
    },

    {
        id: '2.10',
        parent: '1.3',
        name: 'Central Asia'
    },

    /* Europe */
    {
        id: '2.15',
        parent: '1.4',
        name: 'Eastern Europe'
    },

    {
        id: '2.16',
        parent: '1.4',
        name: 'Northern Europe'
    },

    {
        id: '2.17',
        parent: '1.4',
        name: 'Southern Europe'
    },

    {
        id: '2.18',
        parent: '1.4',
        name: 'Western Europe'
    },
    /* Oceania */
    {
        id: '2.19',
        parent: '1.5',
        name: 'Australia and New Zealand'
    },

    {
        id: '2.20',
        parent: '1.5',
        name: 'Melanesia'
    },

    {
        id: '2.21',
        parent: '1.5',
        name: 'Micronesia'
    },

    {
        id: '2.22',
        parent: '1.5',
        name: 'Polynesia'
    }
];

Highcharts.chart('container4', {
    title: {
        text: 'Treegraph with box layout'
    },
    series: [
        {
            type: 'treegraph',
            data,
            tooltip: {
                pointFormat: '{point.name}'
            },
            marker: {
                symbol: 'rect',
                width: '25%'
            },
            borderRadius: 10,
            dataLabels: {
                pointFormat: '{point.name}',
                style: {
                    whiteSpace: 'nowrap'
                }
            },
            levels: [
                {
                    level: 1,
                    levelIsConstant: false
                },
                {
                    level: 2,
                    colorByPoint: true
                },
                {
                    level: 3,
                    colorVariation: {
                        key: 'brightness',
                        to: -0.5
                    }
                },
                {
                    level: 4,
                    colorVariation: {
                        key: 'brightness',
                        to: 0.5
                    }
                }
            ]
        }
    ]
});











