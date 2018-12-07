$(document).ready(function () {
    var images = $('[data-image]');
    var profileImageInput = $('[name=profile_image]');
    var useProfilePicture = $('[name=use_profile_picture]');
    var useProfilePictureErrors = $('#id_use_profile_picture_container .errors');

    images.click(function () {
        var image = $(this);
        images.removeClass('active');
        image.addClass('active');
        profileImageInput.val(image.attr('data-image'));
        useProfilePicture.prop('checked', false);
        useProfilePictureErrors.remove();
    });

    useProfilePicture.change(function () {
        if (useProfilePicture.prop('checked')) {
            images.removeClass('active');
            profileImageInput.val('0');
        } else {
            $('[data-image=1]').click();
        }
    });

    try {
        $('[data-image=' + profileImageInput.val() + ']').click();
    } catch (err) { }
})();
