    /* min-win-height attribute: makes the element have at least win height - header - footer */
    var win = $(window);
    var header = $('header');
    var footer = $('footer');
    win.resize(function () {
        $('[min-win-height]').css('min-height', win.height() - header.outerHeight() - footer.outerHeight());
    }).resize();
