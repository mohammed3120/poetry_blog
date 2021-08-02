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
       var  _obj={};
       var data_bg = $(this).attr("data-bg");
       $("link[href*='bg']").attr("href",data_bg);
       splited_bg = data_bg.split('/')[3];
       bg = splited_bg.split('.')[0];
       console.log(bg);
       _obj['bg'] = bg;

       $.ajax({
        url:'/change-color/bg',
        data:_obj,
        dataType:'json',
        beforeSend:function(){
            console.log("loding .............")
        },
        success:function(res){
            console.log("sucessed.........");
            
        }
            });
    }); 
    
    colorsLi.click(function (){
        var  _obj={};
        var data_theme = $(this).attr("data-value");
        $("link[href*='theme']").attr("href",data_theme);
        splited_theme = data_theme.split('/')[3];
        theme = splited_theme.split('.')[0];
        console.log(theme);
        _obj['theme'] = theme;
        $.ajax({
            url:'/change-color/theme',
            data:_obj,
            dataType:'json',
            beforeSend:function(){
                console.log("loding .............")
            },
            success:function(res){
                console.log("sucessed.........");
                
            }
                });
    
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