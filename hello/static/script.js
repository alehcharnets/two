jQuery("document").ready(function(){
    jQuery("#like").on('click', function () {
        var href = document.getElementById('like').name;
        jQuery.ajax({
            type:"GET",
            url:"/video/addlike/ajax/",
            data: {'addlike': href,},
            dataType: "text",
            catch: false,
            success: function (data) {
                jQuery("#count_likes").html(data);
            }
        });
    });
});

jQuery("document").ready(function(){
    jQuery("#dislike").on('click', function () {
        var href = document.getElementById('dislike').name;
        jQuery.ajax({
            type:"GET",
            url:"/video/adddislike/ajax/",
            data: {'adddislike': href,},
            dataType: "text",
            catch: false,
            success: function (data) {
                jQuery("#count_dislikes").html(data);
            }
        });
    });
});

function openNewWin(url) {
    myWin= open(url);
}