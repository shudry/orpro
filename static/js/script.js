 $(document).on('submit', '#fb_form', function(e)  {
            e.preventDefault();
            $('#fb_form').preloader({setRelative: false});
            var form = e.target;
            $form = $(form);
            console.log($(".fast-set").attr("id"));
            $form.ajaxSubmit({
                url: form.action,
                method: form.method,
                success: function (data) {
                    try{
                    if( data.indexOf('input type="text"') > -1 ) {
                        $(".form-fb-"+data[28]).html(data);
                        $form.attr("method", "post");
                        $(".fast-set").css("display","none");
                        $("#url_fb_"+data[28]).attr("href", "javascript:");
                        $('#fb_form').preloader('remove');
                    }}
                    catch (TypeError){
                         $form.attr("method", "get");
                        $(".fast-set").css("display","block");
                        $(".form-fb-"+data.id).html(
                            '<h3>' + data.fb_title + '</h3>' +
                            '<p>' + data.fb_text + '</p>'
                        );
                        $('.super_user').html();
                        $("#url_fb_"+data.id).attr("href", data.fb_url);
                    };
                    $('#fb_form').preloader('remove');
                },
                error: function (xhr, textStatus, error) {
                    console.log(data);
                    alert('Что-то пошло не так, перезагрузите страницу и попробуйте снова!');
                    $('#fb_form').preloader('remove');
                }
            });
        });

    function init_data(){
             tinyMCE.init({
                 mode : "textareas",
                 theme : "advanced",
                 width : "300"
             });

        }
        init_data();
    $(document).on('submit', '#lb_form', function(e)  {
            e.preventDefault();
            $('#lb_form').preloader({setRelative: false});
            var form = e.target;
            $form = $(form);
            $form.ajaxSubmit({
                url: form.action,
                method: form.method,
                success: function (data) {
                    console.log(data);
                    try{
                    if( data.indexOf('input type="text" name="lb_title"') > -1 ) {
                        $(".form_lb_"+data[28]).html(data);
                        $form.attr("method", "post");
                        $(".fast-set").css("display","none");
                        $("#url_lb_"+data[28]).attr("href", "javascript:");
                        init_data();
                        $('#lb_form').preloader('remove');
                    }}
                    catch (TypeError){
                         $form.attr("method", "get");
                        $(".fast-set").css("display","block");
                        $(".form_lb_"+data.id).html(
                            '<div class="box_aside">'+'<div class="icon' + data.lb_icon + '">'+'</div>'+ '</div>'+ '<div class="box_cnt__no-flow">'+'<h3>'
                            +'<a href="'+ data.lb_link + '"'+ 'id="url_lb_'+data.id+'">'+data.lb_title+'</a>'+'</h3>'
                                +'<p>'+data.lb_text+'</p>'+
                            '</div>'
                        );
                        $('.super_user').html();
                        $("#url_fb_"+data.id).attr("href", data.lb_link);
                    };
                    $('#lb_form').preloader('remove');
                },
                error: function (xhr, textStatus, error) {
                    console.log(data);
                    alert('Что-то пошло не так, перезагрузите страницу и попробуйте снова!');
                    $('#lb_form').preloader('remove');
                }
            });
        });
    $(document).on('submit', '#ac_form', function(e)  {
            e.preventDefault();
            $('#ac_form').preloader({setRelative: false});
            var form = e.target;
            $form = $(form);
            $form.ajaxSubmit({
                url: form.action,
                method: form.method,
                success: function (data) {
                    console.log(data);
                    try{
                    if( data.indexOf('input type="text" name="ac_title"') > -1 ) {
                        $(".ac_form_"+data[28]).html(data);
                        $form.attr("method", "post");
                        $(".fast-set").css("display","none");
                        init_data();
                        $('#ac_form').preloader('remove');
                    }}
                    catch (TypeError){
                         $form.attr("method", "get");
                        $(".fast-set").css("display","block");
                        $(".ac_form_1").html(
                            '<h2>'+data.ac_title+'</h2>'+
                        '<p>'+data.ac_text+'</p>'
                        );
                        $('.super_user').html();
                    };
                    $('#ac_form').preloader('remove');
                },
                error: function (xhr, textStatus, error) {
                    console.log(data);
                    alert('Что-то пошло не так, перезагрузите страницу и попробуйте снова!');
                    $('#ac_form').preloader('remove');
                }
            });
        });
function include(scriptUrl) {
    document.write('<script src="/static/' + scriptUrl + '"></script>');
}

function isIE() {
    var myNav = navigator.userAgent.toLowerCase();
    return (myNav.indexOf('msie') != -1) ? parseInt(myNav.split('msie')[1]) : false;
};

/* cookie.JS
 ========================================================*/
include('js/jquery.cookie.js');

/* Easing library
 ========================================================*/
include('js/jquery.easing.1.3.js');

/* PointerEvents  
 ========================================================*/
;
(function ($) {
    if(isIE() && isIE() < 11){ 
        include('js/pointer-events.js');
        $('html').addClass('lt-ie11'); 
        $(document).ready(function(){
            PointerEventsPolyfill.initialize({});
        });
    }
})(jQuery); 

/* Stick up menus
 ========================================================*/
;
(function ($) {
    var o = $('html');
    if (o.hasClass('desktop')) {
        include('js/tmstickup.js');

        $(document).ready(function () {
            $('#stuck_container').TMStickUp({})
        });
    }
})(jQuery);

/* ToTop
 ========================================================*/
;
(function ($) {
    var o = $('html');
    if (o.hasClass('desktop')) {
        include('js/jquery.ui.totop.js');

        $(document).ready(function () {
            $().UItoTop({
                easingType: 'easeOutQuart',
                containerClass: 'toTop fa fa-angle-up'
            });
        });
    }
})(jQuery);

/* EqualHeights
 ========================================================*/
;
(function ($) {
    var o = $('[data-equal-group]');
    if (o.length > 0) {
        include('js/jquery.equalheights.js');
    }
})(jQuery);

/* Copyright Year
 ========================================================*/
;
(function ($) {
    var currentYear = (new Date).getFullYear();
    $(document).ready(function () {
        $("#copyright-year").text((new Date).getFullYear());
    });
})(jQuery);


/* Superfish menus
 ========================================================*/
;
(function ($) {
    include('js/superfish.js');    
})(jQuery);

/* Navbar
 ========================================================*/
;
(function ($) {
    include('js/jquery.rd-navbar.js');
})(jQuery);


/* Google Map
 ========================================================*/
;
(function ($) {
    var o = document.getElementById("google-map");
    if (o) {
        include('//maps.google.com/maps/api/js?sensor=false');
        include('js/jquery.rd-google-map.js');

        $(document).ready(function () {
            var o = $('#google-map');
            if (o.length > 0) {
                o.googleMap({
                    styles: [{"featureType":"water","elementType":"all","stylers":[{"hue":"#76aee3"},{"saturation":38},{"lightness":-11},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"hue":"#8dc749"},{"saturation":-47},{"lightness":-17},{"visibility":"on"}]},{"featureType":"poi.park","elementType":"all","stylers":[{"hue":"#c6e3a4"},{"saturation":17},{"lightness":-2},{"visibility":"on"}]},{"featureType":"road.arterial","elementType":"all","stylers":[{"hue":"#cccccc"},{"saturation":-100},{"lightness":13},{"visibility":"on"}]},{"featureType":"administrative.land_parcel","elementType":"all","stylers":[{"hue":"#5f5855"},{"saturation":6},{"lightness":-31},{"visibility":"on"}]},{"featureType":"road.local","elementType":"all","stylers":[{"hue":"#ffffff"},{"saturation":-100},{"lightness":100},{"visibility":"simplified"}]},{"featureType":"water","elementType":"all","stylers":[]}]
                });
            }
        });
    }
})
(jQuery);

/* WOW
 ========================================================*/
;
(function ($) {
    var o = $('html');

    if ((navigator.userAgent.toLowerCase().indexOf('msie') == -1 ) || (isIE() && isIE() > 9)) {
        if (o.hasClass('desktop')) {
            include('js/wow.js');

            $(document).ready(function () {
                new WOW().init();
            });
        }
    }
})(jQuery);

/* Contact Form
 ========================================================*/
;
(function ($) {
    var o = $('#contact-form');
    if (o.length > 0) {
        include('js/modal.js');
        include('js/TMForm.js'); 

        if($('#contact-form .recaptcha').length > 0){
        	include('//www.google.com/recaptcha/api/js/recaptcha_ajax.js');
        }
    }
})(jQuery);

/* Orientation tablet fix
 ========================================================*/
$(function () {
    // IPad/IPhone
    var viewportmeta = document.querySelector && document.querySelector('meta[name="viewport"]'),
        ua = navigator.userAgent,

        gestureStart = function () {
            viewportmeta.content = "width=device-width, minimum-scale=0.25, maximum-scale=1.6, initial-scale=1.0";
        },

        scaleFix = function () {
            if (viewportmeta && /iPhone|iPad/.test(ua) && !/Opera Mini/.test(ua)) {
                viewportmeta.content = "width=device-width, minimum-scale=1.0, maximum-scale=1.0";
                document.addEventListener("gesturestart", gestureStart, false);
            }
        };

    scaleFix();
    // Menu Android
    if (window.orientation != undefined) {
        var regM = /ipod|ipad|iphone/gi,
            result = ua.match(regM);
        if (!result) {
            $('.sf-menus li').each(function () {
                if ($(">ul", this)[0]) {
                    $(">a", this).toggle(
                        function () {
                            return false;
                        },
                        function () {
                            window.location.href = $(this).attr("href");
                        }
                    );
                }
            })
        }
    }
});
var ua = navigator.userAgent.toLocaleLowerCase(),
    regV = /ipod|ipad|iphone/gi,
    result = ua.match(regV),
    userScale = "";
if (!result) {
    userScale = ",user-scalable=0"
}
document.write('<meta name="viewport" content="width=device-width,initial-scale=1.0' + userScale + '">');

/* Camera
========================================================*/
;(function ($) {
var o = $('#camera');
    if (o.length > 0) {
        if (!(isIE() && (isIE() > 9))) {
            include('js/jquery.mobile.customized.min.js');
        }

        include('js/camera.js');

        $(document).ready(function () {
            o.camera({
                autoAdvance: true,
                height: '30.859375%',
                minHeight: '350px',
                pagination: false,
                thumbnails: false,
                playPause: false,
                hover: false,
                loader: 'none',
                navigation: true,
                navigationHover: false,
                mobileNavHover: false,
                fx: 'simpleFade'
            })
        });
    }
})(jQuery);

/* Owl Carousel
========================================================*/
;(function ($) {
    var o = $('.owl-carousel');
    if (o.length > 0) {
        include('js/owl.carousel.min.js');
        $(document).ready(function () {
            o.owlCarousel({
                margin: 30,
                smartSpeed: 450,
                loop: true,
                dots: true,
                dotsEach: 1,
                nav: false,
                navClass: ['owl-prev fa fa-angle-left', 'owl-next fa fa-angle-right'],
                responsive: {
                    0: { items: 1 },
                    768: { items: 1},
                    980: { items: 1}
                }
            });
        });
    }
})(jQuery);

/* Mailform
=============================================*/
;(function ($) {
    include('js/mailform/jquery.form.min.js');
    include('js/mailform/jquery.rd-mailform.min.c.js');
})(jQuery);