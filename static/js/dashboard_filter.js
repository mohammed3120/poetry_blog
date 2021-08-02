$(document).ready(function(){
    filterCheckbox = $(".filter-checkbox"); 
    post_search = $(".post_search");
    var post_typeKey=post_search.data('post_type');
    var filterObj={};

    $(".filter-checkbox,.post_search").on("click input", function(){
        filterObj['title'] = post_search.val();
        var _filterKey = filterCheckbox.data('filter');
        filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
            return el.value;
        });
        
        console.log(filterObj);
        $.ajax({
            url:'/dashboard/dashboard_filter_data/'+post_typeKey,
            data:filterObj,
            dataType:'json',
            beforeSend:function(){
                console.log("loding .............")
            },
            success:function(res){
                $("#dashboard_post_list").html(res.data);
            }
        });
    });

    
    
        
            

            
});
        
       


    