$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 300) {
            $('#btnScrollToTop').fadeIn();
        }
        else {
            $('#btnScrollToTop').fadeOut();
        }
    });

    $('#btnScrollToTop').click(function() {
        $('html, body').animate({scrollTop: 0}, 'slow');
    })
});