(function($){

	$(document).ready(function(){

		var valor_tipo1 = $('#id_tipo_encuesta').val();
		
		if (valor_tipo1 === '1' ) {
				$('#organizacionong_set-group').hide();
				$('#tenenciaentrevistada_set-group').hide();
				$('#usotierraentrevistada_set-group').hide();
				$('#produccionanimalentrevistada_set-group').hide();
				$('#ingresoentrevistada_set-group').hide();
				$('#propiedadequipoentrevista_set-group').hide();
				$('#propiedadinfraestructuraentrevista_set-group').hide();
				$('#herramientasentrevista_set-group').hide();
				$('#transporteentrevista_set-group').hide();
				$('#ahorroentrevista_set-group').hide();
				$('#creditoentrevista_set-group').hide();
		};

		$('#id_tipo_encuesta').change(function(){
			var valor_tipo = $('#id_tipo_encuesta').val();
			if (valor_tipo === '2' ) {
				$('#organizacionong_set-group').show();
				$('#tenenciaentrevistada_set-group').show();
				$('#usotierraentrevistada_set-group').show();
				$('#produccionanimalentrevistada_set-group').show();
				$('#ingresoentrevistada_set-group').show();
				$('#propiedadequipoentrevista_set-group').show();
				$('#propiedadinfraestructuraentrevista_set-group').show();
				$('#herramientasentrevista_set-group').show();
				$('#transporteentrevista_set-group').show();
				$('#ahorroentrevista_set-group').show();
				$('#creditoentrevista_set-group').show();

			}else{
				$('#organizacionong_set-group').hide();
				$('#tenenciaentrevistada_set-group').hide()
				$('#usotierraentrevistada_set-group').hide();
				$('#produccionanimalentrevistada_set-group').hide();
				$('#ingresoentrevistada_set-group').hide();
				$('#propiedadequipoentrevista_set-group').hide();
				$('#propiedadinfraestructuraentrevista_set-group').hide();
				$('#herramientasentrevista_set-group').hide();
				$('#transporteentrevista_set-group').hide();
				$('#ahorroentrevista_set-group').hide();
				$('#creditoentrevista_set-group').hide();
			};
		});
		
	
	});
})(jQuery || django.jQuery)