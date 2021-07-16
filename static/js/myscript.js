$(document).ready(function (){
    //Show gear
    $(".gear").click(function (){

        $(".color_option").toggle();
    });

    var colorbgLi = $(".bg_color ul li"),
        colorsLi = $(".colors ul li");

    colorbgLi
        .eq(0).css("backgroundColor", "#333").end()
        .eq(1).css("backgroundColor", "#333969").end();

    colorsLi
        .eq(0).css("backgroundColor", "#E42524").end()
        .eq(1).css("backgroundColor", "#17ab15").end()
        .eq(2).css("backgroundColor", "#aaaa24").end()
        .eq(3).css("backgroundColor", "#2d1d1d").end()
        .eq(4).css("backgroundColor", "#2db4ca").end()
        .eq(5).css("backgroundColor", "#000000").end()
        .eq(6).css("backgroundColor", "#24e45f").end()
        .eq(7).css("backgroundColor", "#222f0c").end()
        .eq(8).css("backgroundColor", "#1520F6").end()
        .eq(9).css("backgroundColor", "#483624").end();    
    
    colorbgLi.click(function (){
       $("link[href*='bg']").attr("href",$(this).attr("data-bg"));
    }); 
    
    colorsLi.click(function (){
        $("link[href*='theme']").attr("href",$(this).attr("data-value"));
     }); 
     


   
});


$(window).on('load', function (){
    $("body").css("overflow", "auto");
    $(".loading_page .sk-chase").fadeOut(2000,function (){
        $(this).parent().fadeOut(1000,function (){
            $(this).remove();
        });
    });
});