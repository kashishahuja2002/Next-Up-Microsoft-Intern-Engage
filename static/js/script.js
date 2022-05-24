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



// Sign-up Page
$(document).ready(function() {
    var upBtn = document.getElementById("up-btn");
    if (!(upBtn == null)) {
        var handleClick = function (event) {
            var upForm = document.getElementById("up-form")
            var email = upForm.elements['user_email'].value;
            var mobile = upForm.elements['user_mobile'].value;
            var password = upForm.elements['user_password'].value;
    
            var url = "http://127.0.0.1:5000/signup";
            $.post(url, {
                email: email,
                mobile: mobile,
                password: password,
            },function(data, status) {
                console.log(data, status);
                if(data == "choices") {
                    var url = "http://127.0.0.1:5000/choices";
                    window.location.href = url;
                }
                else {
                    var errorMsg = data;
                    document.getElementById("error").innerHTML = errorMsg;
                }
            });
    
            event.preventDefault();
        };
        upBtn.onclick = handleClick;
    }
});



// Sign-in Page
$(document).ready(function() {
    var inBtn = document.getElementById("in-btn");
    if (!(inBtn == null)) {
        var handleClick = function (event) {
            var inForm = document.getElementById("in-form")
            var email = inForm.elements['user_email'].value;
            var password = inForm.elements['user_password'].value;

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
    
            event.preventDefault();
        };
        inBtn.onclick = handleClick;
    }
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

var choiceBtn = document.getElementById("choice-btn");
if (!(choiceBtn == null)) {
    var handleClick = function (event) {
        genres = $('input[name="genre-checkbox"]:checked').length;
        cast = $('input[name="cast-checkbox"]:checked').length;
    
        if(genres == 3 && cast == 5) {
            document.getElementById("choice-form").submit();
        }
        else {
            alert("Please select 3 genres and 5 casts.");
            event.preventDefault();
        }
    };
    choiceBtn.onclick = handleClick;
}