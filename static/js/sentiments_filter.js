
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

        if($.trim(like_action.text())=='Like' ){
            _likes_num = parseInt(likes_number)+1;
            likes_number_id.text(_likes_num + "\tLikes");
            _obj['lang'] = 'en';
        }
        else if($.trim(like_action.text())== "إعجاب"){
            _likes_num = parseInt(likes_number)+1;
            likes_number_id.text(_likes_num + "\tالإعجابات"); 
            _obj['lang'] = 'ar';
        }
        else if ($.trim(like_action.text())=='Liked'){
            _likes_num = parseInt(likes_number)- 1;
            likes_number_id.text(_likes_num + "\tLikes");
            _obj['lang'] = 'en';
        }
        else if ($.trim(like_action.text())=="تم الإعجاب"){
            _likes_num = parseInt(likes_number)- 1;
            likes_number_id.text(_likes_num + "\tالإعجابات");
            _obj['lang'] = 'ar';
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
        localStorage.setItem("post_id_loading", post_id);
        var commet_action = $('#comment'+post_id);
        var acco_comment = $('#acco-comment'+post_id);
        var _obj ={'comment':commet_action.val()};
        _obj['csrftoken'] = getCookie('csrftoken');
        var comments_number_id = $('#comments_number'+post_id);
        var comments_number = comments_number_id.text().split('')[0];
        var _comments_number = parseInt(comments_number);
        var comment_id = localStorage.getItem("comment_id");
        var urlPath;
        var comment_body;
        if(comment_id){
            urlPath = `/update_comment/${comment_id}`
            comment_body = $(`#comment_${post_id}_body_${comment_id}`)
        }
        else{
            urlPath = `/add-comment/${post_id}`;
        }
        $.ajax({
            url:urlPath,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
            },
            success:function(res){
                if(comment_id){
                    comment_body.text(res.comment.body) ;
                    localStorage.removeItem('comment_id');
                }
                else{
                    acco_comment.append(res.comment);
                    _comments_number = _comments_number + 1;
                    comments_number_id.text(_comments_number + "\tcomments");   
                }
                commet_action.val(""); 
                sessionStorage.setItem("reloading1", "true");
                document.location.reload(); 
                

            }
        });    
    });
    $(".editComment").on('click', function(){
        var editBtnId =  $(this).attr('id');
        var splittedId = editBtnId.split('_');
        var post_id = splittedId[1];
        var comment_id = splittedId[3];
        var comment_input = $('#comment'+post_id);
        var comment_body = $(`#comment_${post_id}_body_${comment_id}`)
        comment_input.val(comment_body.text());
        window.location=`#comment${post_id}`;
        comment_input.focus();
        localStorage.setItem("comment_id", comment_id);

    });

    $(".reply-form").on('submit', function(event){
        event.preventDefault();
        var fullId = $(this).attr('id');
        var post_id = fullId.split('_')[1];
        var comment_id = fullId.split('_')[3];
        localStorage.setItem("post_id_loading", post_id);
        localStorage.setItem("comment_id_loading", comment_id);
        var reply_action = $('#comment_'+comment_id);
        var acco_reply = $('#comment_'+comment_id+'_acco_reply');
        var replies_number_id = $('#comment_'+comment_id+'_replies_number');
        var replies_number = replies_number_id.text().split('')[0];
        var _replies_number = parseInt(replies_number);
        var _obj ={'reply':reply_action.val(),'csrftoken':getCookie('csrftoken')};
        var reply_id = localStorage.getItem("reply_id");
        var urlPath;
        
        if(reply_id){
            urlPath = `/update_reply/${reply_id}`;
            reply_body = $(`#replybody_${reply_id}`);
        }
        else{
            urlPath = `/add-reply/${comment_id}`;
        }
        $.ajax({
            url:urlPath,
            data:_obj,
            dataType:'json',
            beforeSend:function(){
            },
            success:function(res){
                if(reply_id){
                    reply_body.text(res.reply) ;
                    localStorage.removeItem('reply_id');
                }
                else{
                    acco_reply.append(res.reply);
                _replies_number = _replies_number + 1;
                replies_number_id.text(_replies_number + "\treplies  reply");   
                }
                
                reply_action.val("");
                sessionStorage.setItem("reloading1", "true");
                sessionStorage.setItem("reloading2", "true");
                document.location.reload();
                
            }
        });      
        
    });

    $(".editReply").on('click', function(){
        var editBtnId =  $(this).attr('id');
        var splittedId = editBtnId.split('_');
        var comment_id = splittedId[1];
        var reply_id = splittedId[3];
        var reply_input = $('#comment_'+comment_id);
        var reply_body = $(`#replybody_${reply_id}`)
        reply_input.val(reply_body.text());
        localStorage.setItem("reply_id", reply_id);
    });

    $(".deleteComment").on('click', function(){
        var deleteBtnId =  $(this).attr('id');
        var splittedId = deleteBtnId.split('_');
        var post_id = splittedId[1];
        localStorage.setItem("post_id_loading", post_id);
        var comment_id = splittedId[3];
        var commentElement = $(`#accordion-comment_${comment_id}`);

        var comments_number_id = $('#comments_number'+post_id);
        var comments_number = comments_number_id.text().split('')[0];
        var _comments_number = parseInt(comments_number);

        $.ajax({
            url:`/delete_comment/${comment_id}`,
            beforeSend:function(){
            },
            success:function(res){
                commentElement.remove();
                _comments_number = _comments_number - 1;
                comments_number_id.text(_comments_number + "\tcomments");
                sessionStorage.setItem("reloading1", "true");
                document.location.reload(); 
                

            }
        });    

    });

});
window.onload = function() {
    var post_id = localStorage.getItem("post_id_loading");
    var comment_id = localStorage.getItem("comment_id_loading");

    if (comment_id && post_id) {
        var reloading1 = sessionStorage.getItem("reloading1");
        var reloading2 = sessionStorage.getItem("reloading2");
        if (reloading1 && reloading2) {
            sessionStorage.removeItem("reloading1");
            sessionStorage.removeItem("reloading2");
            var collapse1 = document.getElementById('collapse-'+post_id);
            var collapsed1 = document.getElementById('collapsed_'+post_id);
            collapsed1.classList.add('collapsed');
            collapse1.classList.add("show");
            collapsed1.getAttribute('aria-expanded').value = 'true';
            
        
            
            var collapse2 = document.getElementById('replies-'+comment_id);
            var collapsed2 = document.getElementById('commentColapsed_'+comment_id); 
            collapsed2.classList.add('collapsed');
            collapse2.classList.add("show");
            collapsed2.getAttribute('aria-expanded').value = 'true';
            localStorage.removeItem('comment_id_loading');
            localStorage.removeItem('post_id_loading');
        }
    }
    else if (post_id) {
        var reloading1 = sessionStorage.getItem("reloading1");
        if (reloading1) {
            sessionStorage.removeItem("reloading1");
            var collapse1 = document.getElementById('collapse-'+post_id);
            var collapsed1 = document.getElementById('collapsed_'+post_id);
            collapsed1.classList.add('collapsed');
            collapse1.classList.add("show");
            collapsed1.getAttribute('aria-expanded').value = 'true';
            localStorage.removeItem('post_id_loading');
        }
    }
    
}
var wrap = $("#wrap");

wrap.on("scroll", function(e) {
    
  if (this.scrollTop > 147) {
    wrap.addClass("fix-search");
  } else {
    wrap.removeClass("fix-search");
  }
  
});






    