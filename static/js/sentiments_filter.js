
$(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
	// Sentiment Filter Start
    $(".filter-checkbox").on('click', function(){
        var _filterObj={};
        var _filterVal=$(this).val();
        var _filterKey=$(this).data('filter');
        var _post_typeKey=$(this).data('post_type');
        _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
            return el.value;
        });
        _filterObj['csrftoken'] = getCookie('csrftoken');
        $.ajax({
            url:'/filter-data/'+_post_typeKey,
            data:_filterObj,
            dataType:'json',
            beforeSend:function(){

            },
            success:function(res){
                $('#post_list').html(res.data);
                document.location.reload(); 
                //$("#post_list").load("#post_list");

            }
        });      
    });


    $(".like_action").on('click', function(){
        var _obj = {};
        var like_action_id = $(this).attr('id');
        
        var post_id = like_action_id.split('_')[2];
        var like_action = $('#'+like_action_id);
        _obj['liked'] = like_action.text();
        var likes_number_id = $('#likes_number'+post_id);
        var likes_number = likes_number_id.text().split('')[0];
        var _likes_num = 0;
        if($.trim(like_action.text())=='Like'){
            _likes_num = parseInt(likes_number)+1;
            likes_number_id.text(_likes_num + "\tLikes");
        }
        else if ($.trim(like_action.text())=='Liked'){
            _likes_num = parseInt(likes_number)- 1;
            likes_number_id.text(_likes_num + "\tLikes");
        }
        $.ajax({
            url:'/like/'+post_id,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
            },
            success:function(res){
                l = res.likeData['liked']
                like_action.html(l);
            }
        });
    });

    $(".comment-form").on('submit', function(event){
        event.preventDefault();
        var post_id = $(this).attr('id').split('_')[1];
        localStorage.setItem("post_id", post_id);
        var commet_action = $('#comment'+post_id);
        var acco_comment = $('#acco-comment'+post_id);
        var _obj ={'comment':commet_action.val()};
        _obj['csrftoken'] = getCookie('csrftoken');
        var comments_number_id = $('#comments_number'+post_id);
        var comments_number = comments_number_id.text().split('')[0];
        var _comments_number = parseInt(comments_number);
        $.ajax({
            url:'/add-comment/'+post_id,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
            },
            success:function(res){
                acco_comment.append(res.comment);
                _comments_number = _comments_number + 1;
                comments_number_id.text(_comments_number + "\tcomments");
                commet_action.val(""); 
                sessionStorage.setItem("reloading", "true");
                document.location.reload(); 
                

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
        var replies_number_id = $('#post_'+post_id+'_comment_'+comment_id+'_replies_number');
        var replies_number = replies_number_id.text().split('')[0];
        var _replies_number = parseInt(replies_number);
        

        var _obj ={'reply':reply_action.val(),'csrftoken':getCookie('csrftoken')};
        $.ajax({
            url:'/add-reply/'+comment_id,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
            },
            success:function(res){
                
                acco_reply.append(res.reply);
                _replies_number = _replies_number + 1;
                replies_number_id.text(_replies_number + "\treplies  reply");
                reply_action.val("");
                
            }
        });      
        
    });

});
window.onload = function() {
    var post_id = localStorage.getItem("post_id");
    var reloading = sessionStorage.getItem("reloading");
    if (reloading) {
        sessionStorage.removeItem("reloading");
        var collapse = document.getElementById('collapse-'+post_id);
        var collapsed = document.getElementById('collapsed_'+post_id);
        collapsed.classList.add('collapsed');
        collapse.classList.add("show");
        collapsed.getAttribute('aria-expanded').value = 'true';
        localStorage.clear();
    }
}







    