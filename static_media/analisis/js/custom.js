
(function($){

	$(document).ready(function(){

		var gu = $(".submit-row input[name$='_continue']");
		gu.addClass('guardar');

		var save = $(".submit-row input[name$='_save']");
		save.addClass('save');

		var add = $(".submit-row input[name$='_addanother']");
		add.addClass('add');

		var pathname = window.location.pathname;
		url = pathname.split("/");
			if (url[4]=='add' && url[2] == 'analysis') {
			$('.field-box.field-tipo_estudio').append('<input type="submit" value="Save and continue editing" name="_continue" class="guardar default" id="btn_intro">');
		}else if(url[4]=='add' && url[2] == 'analisis'){
			$('.field-box.field-tipo_estudio').append('<input type="submit" value="Guardar y continuar editando" name="_continue" class="guardar default" id="btn_intro">');
		};
		
		if (url[2] == 'analysis') {
			$('.save').prop('value', 'Save');
			$('.guardar').prop('value', 'Save and continue editing');
			$('.add').prop('value', 'Seva and add another');

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

