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
    window.location = url;
}



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
    console.log(selectedGenre);
    var url = "http://127.0.0.1:5000/getByGenre";
    $.post(url, {
        genre: selectedGenre,
    },function(data, status) {
        console.log(data, status);
        var htmlContent="";
        for(var i=0; i<data[0].genre_movies.length; i++) {
            htmlContent = htmlContent + "<div class='col-6 col-sm-4 col-md-2 movie-card'><a href='/movie/'"+data[0].genre_movies[i]+"><img src='"+data[1].genre_posters[i]+"' alt='' style='width: 100%;height: auto;'><p>"+data[0].genre_movies[i]+"</p></a></div>";
        }
        document.getElementById("genre-row").innerHTML = htmlContent;
    });
}

let selection = document.getElementById("years");


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
            htmlContent = htmlContent + "<div class='col-6 col-sm-4 col-md-2 movie-card'><a href='/movie/'"+data[0].year_movies[i]+"><img src='"+data[1].year_posters[i]+"' alt='' style='width: 100%;height: auto;'><p>"+data[0].year_movies[i]+"</p></a></div>";
        }
        document.getElementById("year-row").innerHTML = htmlContent;
    });
}