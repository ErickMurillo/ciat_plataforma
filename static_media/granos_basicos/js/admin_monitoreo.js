(function($){
	$(document).ready(function(){
    valor = $('#id_datosparcela_set-0-acceso_agua').val();
    if (valor == 1) {
      $('.field-acceso_agua .inline').show();
      $('#id_datosparcela_set-0-fuente_agua').show();
      $('#id_datosparcela_set-0-distancia').show();
    } else {
      $('.field-acceso_agua .inline').hide();
      $('#id_datosparcela_set-0-fuente_agua').hide();
      $('#id_datosparcela_set-0-distancia').hide();
    }

    $('#id_datosparcela_set-0-acceso_agua').change(function(){
      valor = $('#id_datosparcela_set-0-acceso_agua').val();
      if (valor == 1) {
        $('.field-acceso_agua .inline').show();
        $('#id_datosparcela_set-0-fuente_agua').show();
        $('#id_datosparcela_set-0-distancia').show();
      } else {
        $('.field-acceso_agua .inline').hide();
        $('#id_datosparcela_set-0-fuente_agua').hide();
        $('#id_datosparcela_set-0-distancia').hide();
      }
    });
  });
})(jQuery || django.jQuery);
