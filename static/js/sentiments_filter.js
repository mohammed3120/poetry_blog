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
                $('#post_list').html(res.data);

            }
        });      
    });


    $(".like_action").on('click', function(){
        var _obj = {};
        var like_action_id = $(this).attr('id');
        
        var post_id = like_action_id.split('_')[2];
        var like_action = $('#'+like_action_id);
        _obj['liked'] = like_action.text();
        console.log(like_action.text());
        var likes_number_id = $('#likes_number'+post_id);
        // console.log("likes_number"+likes_number);
        var likes_number = likes_number_id.text().split('')[0];
        console.log(likes_number)
        // console.log("likes_number_id"+likes_number_id.text());
        var _likes_num = 0;
        if($.trim(like_action.text())=='Like'){
            _likes_num = parseInt(likes_number)+1;
            likes_number_id.text(_likes_num + "\tLikes");
            console.log(likes_number_id.text());
        }
        else if ($.trim(like_action.text())=='Liked'){
            _likes_num = parseInt(likes_number)- 1;
            likes_number_id.text(_likes_num + "\tLikes");
            console.log(likes_number_id.text());
        }
        $.ajax({
            url:'/like/'+post_id,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
                console.log("")
            },
            success:function(res){
                // console.log("ssssssssssssssssss");
                // console.log($(this));
                l = res.likeData['liked']
                like_action.html(l);
                // console.log(res.likeData);
            }
        });
    });

    $(".comment-form").on('submit', function(event){comments_number
        event.preventDefault();
        var post_id = $(this).attr('id').split('_')[1];
        var commet_action = $('#comment'+post_id);
        var acco_comment = $('#acco-comment'+post_id);
        console.log(acco_comment.html());
        console.log(commet_action.val());
        var _obj ={'comment':commet_action.val()};
        _obj['csrfmiddlewaretoken'] = '{{ csrf_token }}';
        var comments_number_id = $('#comments_number'+post_id);
        var comments_number = comments_number_id.text().split('')[0];
        console.log(comments_number)
        var _comments_number = parseInt(comments_number);
        
        $.ajax({
            url:'/add-comment/'+post_id,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
                console.log("loding .............")
            },
            success:function(res){
                console.log("ccccccccccccccccccccc");
                
                acco_comment.append(res.comment);
                _comments_number = _comments_number + 1;
                comments_number_id.text(_comments_number + "\tcomments");
                commet_action.val("");
                
            }
        });
        

        
    });

    $(".reply-form").on('submit', function(event){
        event.preventDefault();
        var fullId = $(this).attr('id');
        var post_id = fullId.split('_')[1];
        var comment_id = fullId.split('_')[3];
        var reply_action = $('#post_'+post_id+'_comment_'+comment_id);
        var acco_reply = $('#post_'+post_id+'_comment_'+comment_id+'_acco_reply');
        console.log(acco_reply);
        console.log(reply_action.val());
        
        var _obj ={'reply':reply_action.val(),'csrfmiddlewaretoken':'{{ csrf_token }}'};
        $.ajax({
            url:'/add-reply/'+comment_id,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
                console.log("loding .............")
            },
            success:function(res){
                console.log("ccccccccccccccccccccc");
                
                acco_reply.append(res.reply);
                reply_action.val("");
                
            }
        });
        

        
    });

});




    