(function($){
	$(document).ready(function(){
    valor = $('#id_acceso_agua').val();
    if (valor == 1) {
      $('.field-acceso_agua .inline').show();
      $('.field-acceso_agua #id_fuente_agua').show();
      $('.field-distancia #id_distancia').show();
    } else {
			$('.field-acceso_agua .inline').hide();
			$('.field-acceso_agua #id_fuente_agua').hide();
			$('.field-distancia #id_distancia').hide();
    }

    $('#id_acceso_agua').change(function(){
      valor = $('#id_acceso_agua').val();
      if (valor == 1) {
        $('.field-acceso_agua .inline').show();
        $('.field-acceso_agua #id_fuente_agua').show();
        $('.field-distancia #id_distancia').show();
      } else {
        $('.field-acceso_agua .inline').hide();
        $('.field-acceso_agua #id_fuente_agua').hide();
        $('.field-distancia #id_distancia').hide();
      }
    });
  });
})(jQuery || django.jQuery);
