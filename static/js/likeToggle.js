$(document).ready(function(){
	//  Like Action Start
		$(".like_action").on('click', function(){
            var obj = {};
            var post_id = $(this).attr('id');
			var like_action = $('.like_action'+post_id);
            
            // if (text == "liked"){
            //     obj["liked"] = "liked";
            // } 
            // else{
            //     obj["liked"] = "like";
            // }
            obj['liked'] = like_action.text();
            console.log(obj);
            $.ajax({
                url:'/like/'+post_id,
                data:obj,
                dataType:'json',
                beforeSend:function(){
                    console.log("loding .............")
                },
                success:function(res){
                    console.log("ssssssssssssssssss");
                    console.log($(this));
                    like_action.text(res.data['liked']);
                    console.log(res.data);
                }
            });
			});
            

            
		});
        
       


    