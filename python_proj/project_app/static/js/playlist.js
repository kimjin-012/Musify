  /* Load the HTTP library */
var request = require('request'); // "Request" library

var client_id = '67da7ffc8c384cbeb8c6d532319189e8'; // Your client id
var client_secret = 'aee6f3e9039246779bd9352e177ba189'; // Your secret

// your application requests authorization
var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    headers: {
        'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
    },
    form: {
        grant_type: 'client_credentials'
    },
    json: true
};

request.post(authOptions, function(error, response, body) {
    if (!error && response.statusCode === 200) {

    // use the access token to access the Spotify Web API
    var token = body.access_token;
    var options = {
    url: 'https://api.spotify.com/v1/users/jmperezperez',
    headers: {
        'Authorization': 'Bearer ' + token
    },
        json: true
    };
    request.get(options, function(error, response, body) {
        console.log(body);
    });
    }
});



$(document).ready(function () {
    $(".button-toggle").click(function () {
        $(".table").toggle();
    });
    $(".button_toggle_like").click(function () {
        $(".table_like").toggle();
    });
});


