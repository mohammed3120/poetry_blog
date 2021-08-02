$(document).ready(function(){
	// Sentiment Filter Start
		$(".filter-checkbox").on('click', function(){
            var _filterObj={};
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			var _post_typeKey=$(this).data('post_type');
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
            

            $.ajax({
                url:'/filter-data/'+_post_typeKey,
                data:_filterObj,
                dataType:'json',
                beforeSend:function(){
                    console.log("loding .............")
                },
                success:function(res){
                    $("#post_list").html(res.data);
                }
            });
		});
        
       
	});


    