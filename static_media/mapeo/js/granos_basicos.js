(function($){
	$(document).ready(function(){
    $('#productorgranosbasicos_set-group').hide();
    $('#usosuelo_set-group').hide();
    $('#composicionfamiliar_set-group').hide();

    $('#id_productor_set-0-proyecto').change(function(){
  			var value = $('#id_productor_set-0-proyecto option:selected').text();
  			if (value == 'Herramienta granos básicos') {
          $('#productorgranosbasicos_set-group').show();
          $('#usosuelo_set-group').show();
          $('#composicionfamiliar_set-group').show();
  			}else{
          $('#productorgranosbasicos_set-group').hide();
          $('#usosuelo_set-group').hide();
          $('#composicionfamiliar_set-group').hide();
  			};
  		});
  });
})(jQuery || django.jQuery);
