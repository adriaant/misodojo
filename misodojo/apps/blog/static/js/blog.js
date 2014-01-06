var Blog = {

    loading: false,  // to prevent hitting the ajax function more than necessary
    num_loaded: 0,   // number of posts already shown

    init: function() {
        // record # of posts we already have
        Blog.num_loaded = $(".post").length;

        // hide the non-js pager. By keeping the pager with no JS, google can still index posts.
        $('ul.pager').hide();

        // set the trigger
        $(window).scroll(function(e){
            if (Blog.loading){
                return false;
            }
            if (document.documentElement.clientHeight + $(document).scrollTop() >= document.body.offsetHeight) {
                Blog.loading = true;
                $('#loader').show(); // a way to show the user we're working
                Blog.loadPosts();
            } 
        });
    },

    loadPosts: function() {
        // make request to backend for next batch of posts
        $.get("/blog/?offset=" + Blog.num_loaded, function(data) {
            if (data.indexOf("<div") >= 0) {
                $('#loader').hide();
                $( ".post:last" ).after(data);
                Blog.num_loaded = $(".post").length;
                // wait 1 sec before we allow loading posts again
                setTimeout(function() {
                    Blog.loading = false;
                },1000);
            } else {
                // there are no more posts, remove spinner, show end of paragraph marker
                $("#loader img").remove();
                $("#loader").css("background-image", "url(/static/images/paragraph.png)"); 
            }
        });
    }
};

$(Blog.init);
