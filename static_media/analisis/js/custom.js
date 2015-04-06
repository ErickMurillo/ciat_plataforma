

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

		var pathname = window.location.pathname;
		url = pathname.split("/");
		if (url[4]=='add') {
			$('.field-box.field-tipo_estudio').append('<input type="submit" value="Grabar y continuar editando" name="_continue" class="guardar default" id="btn_intro">');
		};
	});




	$(document).on('change','.select-evt',function(){
		//var id = $('.select-evt').attr('id')
		$('.guardar').click()
	});

	// $(document).on('click','#id_tipo_estudio',function(){
	// 	$('.guardar').click()
	// });

	

	$(document).ready( function() 
	{
		var pathname = window.location.pathname;
		url = pathname.split("/");
		if (url[4]=='add') {
	 	//console.log(url[4]);
	 	$('.field-departamento ul').empty();
	 };
	} );

	$(document).on('click','#id_pais',function(){
		var id = $(this).val();
	 	$('.field-departamento ul').empty();
		$.ajax({
			data : {'id' : id},
			url : '/admin/pais/',
			type : 'get',
			success : function(data){
				var html = ""
				 //console.log(data);
				 for (var i = 0; i < data.length; i++) {
				 	html += '<li><label for="id_departamento_'+i+'"><input id="id_departamento_'+i+'" name="departamento" type="checkbox" value="'+data[i].pk+'">'+data[i].fields.nombre+'</label></li>'
				 };
				 $('.field-departamento ul').html(html);
				}
			});
	});


})(jQuery || django.jQuery);

