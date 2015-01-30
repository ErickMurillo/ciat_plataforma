

// (function($){
//    $(document).ready(function(){
//    	var prio = $(".dynamic-pregunta_5a_set select")
//       prio.click(function (e) {
//         if (prio.val() == '1') {
//         	alert('ya ta')
//         };
//     });
//    });
// })(jQuery || django.jQuery);


(function($){

	$(document).ready(function(){

	 var gu = $(".submit-row input[name$='_continue']");
	 gu.addClass('guardar');

	});


   $(document).on('click','#id_pregunta_5a_set-0-prioritizado',function(){
	var prio = $('#id_pregunta_5a_set-0-prioritizado')
	if (prio.val() == '1') {
		$('.guardar').click()

	};
});

//    $(document).on('click','#id_pregunta_5a_set-1-prioritizado',function(){
// 	var prio1 = $("#id_pregunta_5a_set-1-prioritizado")
// 	if (prio1.val() == '1') {
// 		$('.guardar').click()
// 	};
// });


})(jQuery || django.jQuery);