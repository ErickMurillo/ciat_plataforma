

(function($){
   $(document).ready(function(){
   	var prio = $(".dynamic-pregunta_5a_set select")
      prio.click(function (e) {
        if (prio.val() == '1') {
        	alert('ya ta')
        };
    });
   });
})(jQuery || django.jQuery);
