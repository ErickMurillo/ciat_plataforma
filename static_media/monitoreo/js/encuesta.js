(function($){

	$(document).ready(function(){

		var valor_tipo1 = $('#id_tipo_encuesta').val();
		
		if (valor_tipo1 === '1' ) {
				$('#organizacionong_set-group').hide();
				alert(valor_tipo1);
		};

		$('#id_tipo_encuesta').change(function(){
			var valor_tipo = $('#id_tipo_encuesta').val();
			if (valor_tipo === '2' ) {
				$('#organizacionong_set-group').show();
			}else{
				$('#organizacionong_set-group').hide();
			};
		});
		
	
	});
})(jQuery || django.jQuery)