// Header

// Select2
$(document).ready(function() {
    $('.select2').select2();
});

// Recommendations Page

// Movie Slider carousel
$('.carousel').carousel({
    interval: 5000,
    keyboard: true
})

// Movie Page
function movieSelect()
{
    let selection = document.querySelector('select');
    let selectedMovie = selection.options[selection.selectedIndex].text;

    var url = "http://127.0.0.1:5000/movie/"+selectedMovie;
    window.location = url;
}