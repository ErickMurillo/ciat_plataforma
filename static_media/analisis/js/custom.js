

(function($){
   $(document).ready(function(){
   	var prio = $(".dynamic-pregunta_5a_set select")
   	var priox = $('#pregunta_5a_set-group .add-row a')
      prio.click(function (e) {
        if (prio.val() == '1') {
        	alert('ya ta')
        };
    });
   });
})(jQuery || django.jQuery);


