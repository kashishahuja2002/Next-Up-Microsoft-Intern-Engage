// Header

// Select2
$(document).ready(function() {
    $('.select2').select2();
});

// Search select
function movieSelect()
{
    let selection = document.getElementById('movieSelect');
    let selectedMovie = selection.options[selection.selectedIndex].text;

    var url = "http://127.0.0.1:5000/movie/"+selectedMovie;
    window.location.href = url;
}



// Sign-in Page

const form  = document.getElementById("signin-form");
form.addEventListener('submit', (event) => {
    event.preventDefault();
    var email = form.elements['user_email'].value;
    var password = form.elements['user_password'].value;

    var url = "http://127.0.0.1:5000/signin";
    $.post(url, {
        email: email,
        password: password,
    },function(data, status) {
        console.log(data, status);
        if(data == "recommendations") {
            var url = "http://127.0.0.1:5000/recommendations";
            window.location.href = url;
        }
        else {
            var errorMsg = data;
            document.getElementById("error-msg").innerHTML = errorMsg;
        }
    });
});



// Sign-up Page

const newForm  = document.getElementById("signup-form");
newForm.addEventListener('submit', (event) => {
    event.preventDefault();
    var email = newForm.elements['user_email'].value;
    var mobile = newForm.elements['user_mobile'].value;
    var password = newForm.elements['user_password'].value;

    var url = "http://127.0.0.1:5000/signup";
    $.post(url, {
        email: email,
        mobile: mobile,
        password: password,
    },function(data, status) {
        console.log(data, status);
        if(data != "choices") {
            var errorMsg = data;
            document.getElementById("error").innerHTML = errorMsg;
        }
        else if(data == "choices"){
            var url = "http://127.0.0.1:5000/choices";
            window.location.href = url;
        }
    });
});



// Recommendations Page

//Movie Slider carousel
$('.carousel').carousel({
    interval: 5000,
    keyboard: true
})

// select by genre
function genreSelected()
{
    let selection = document.getElementById("genres");
    let selectedGenre = selection.options[selection.selectedIndex].text;
    var url = "http://127.0.0.1:5000/getByGenre";
    $.post(url, {
        genre: selectedGenre,
    },function(data, status) {
        console.log(data, status);
        var htmlContent="";
        for(var i=0; i<data[0].genre_movies.length; i++) {
            htmlContent = htmlContent + "<div class='col-6 col-sm-4 col-md-2 movie-card'><a href='/movie/"+data[0].genre_movies[i]+"'><img src='"+data[1].genre_posters[i]+"' alt='' style='width: 100%;height: auto;'><p>"+data[0].genre_movies[i]+"</p></a></div>";
        }
        document.getElementById("genre-row").innerHTML = htmlContent;
    });
}

function yearSelected() {
    let selection = document.getElementById("years");
    let selectedYear = selection.options[selection.selectedIndex].text;
    var url = "http://127.0.0.1:5000/getByYear";
    $.post(url, {
        year: selectedYear,
    },function(data, status) {
        console.log(data, status);
        var htmlContent="";
        for(var i=0; i<data[0].year_movies.length; i++) {
            htmlContent = htmlContent + "<div class='col-6 col-sm-4 col-md-2 movie-card'><a href='/movie/"+data[0].year_movies[i]+"'><img src='"+data[1].year_posters[i]+"' alt='' style='width: 100%;height: auto;'><p>"+data[0].year_movies[i]+"</p></a></div>";
        }
        document.getElementById("year-row").innerHTML = htmlContent;
    });
}


// Movie Page

var genreLimit = 3;
$('input.genre-checkbox').on('change', function(evt) {
    if($('input[name="genre-checkbox"]:checked').length > genreLimit) {
        this.checked = false;
    }
});

var castLimit = 5;
$('input.cast-checkbox').on('change', function(evt) {
    if($('input[name="cast-checkbox"]:checked').length > castLimit) {
        this.checked = false;
    }
});

// function choiceSubmit() {
//     genres = ('input[name="genre-checkbox"]:checked').length;
//     cast = ('input[name="cast-checkbox"]:checked').length;

//     console.log(genres, cast);
//     // if(genres != 3 || cast != 5) {
//     //     alert("Please select 3 genres and 5 casts.");
//     // }
//     // else {
//     //     document.getElementById("choice-form").submit();
//     // }
// }

// $('input[name="genres"]:checked').each(function() {
//     console.log(this.value);
// });