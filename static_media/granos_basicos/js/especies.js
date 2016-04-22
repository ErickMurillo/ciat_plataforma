(function($){
	$(document).ready(function(){
    $('.field-rango_min').hide();
    $('.field-rango_max').hide();
    $('.field-descripcion').hide();

    var valor_tipo = $('#id_umbral').val();
    if (valor_tipo == '1') {
      $('.field-rango_min').show();
      $('.field-rango_max').show();
      $('.field-descripcion').hide();
    }else if (valor_tipo == '2') {
      $('.field-rango_min').hide();
      $('.field-rango_max').hide();
      $('.field-descripcion').show();
    }

    $('#id_umbral').change(function(){
  			var valor_tipo = $('#id_umbral').val();
  			if (valor_tipo == '1') {
          $('.field-rango_min').show();
          $('.field-rango_max').show();
          $('.field-descripcion').hide();
  			}else if (valor_tipo == '2'){
          $('.field-rango_min').hide();
          $('.field-rango_max').hide();
          $('.field-descripcion').show();
  			};
  		});
  });
})(jQuery || django.jQuery);
