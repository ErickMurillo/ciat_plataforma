(function($){
	$(document).ready(function(){
    //semillas
    if ($('#id_areas_0').is(':checked')) {
      $('#semillas_set-group').show();
      $('#procedenciasemilla_set-group').show();
      $('#pruebagerminacion_set-group').show();
    }else{
      $('#semillas_set-group').hide();
      $('#procedenciasemilla_set-group').hide();
      $('#pruebagerminacion_set-group').hide();
    };

    $('#id_areas_0').change(function(){
        if ($('#id_areas_0').is(':checked')) {
          $('#semillas_set-group').show();
          $('#procedenciasemilla_set-group').show();
          $('#pruebagerminacion_set-group').show();
        }else{
          $('#semillas_set-group').hide();
          $('#procedenciasemilla_set-group').hide();
          $('#pruebagerminacion_set-group').hide();
        }
		});

    //suelo
    if ($('#id_areas_1').is(':checked')) {
      $('#suelo_set-group').show();
    }else{
      $('#suelo_set-group').hide();
    };

    $('#id_areas_1').change(function(){
        if ($('#id_areas_1').is(':checked')) {
          $('#suelo_set-group').show();
        }else{
          $('#suelo_set-group').hide();
        }
    });

    //macrofauna
    if ($('#id_areas_2').is(':checked')) {
      $('#macrofauna_set-group').show();
    }else{
      $('#macrofauna_set-group').hide();
    };

    $('#id_areas_2').change(function(){
        if ($('#id_areas_2').is(':checked')) {
          $('#macrofauna_set-group').show();
        }else{
          $('#macrofauna_set-group').hide();
        }
		});

    //malezas
    if ($('#id_areas_3').is(':checked')) {
      $('#monitoreomalezas_set-group').show();
      $('#tablamalezas_set-group').show();
    }else{
      $('#monitoreomalezas_set-group').hide();
      $('#tablamalezas_set-group').hide();
    };

    $('#id_areas_3').change(function(){
        if ($('#id_areas_3').is(':checked')) {
          $('#monitoreomalezas_set-group').show();
          $('#tablamalezas_set-group').show();
        }else{
          $('#monitoreomalezas_set-group').hide();
          $('#tablamalezas_set-group').hide();
        }
		});

    //vigor
    if ($('#id_areas_4').is(':checked')) {
      $('#vigorfrijol_set-group').show();
      $('#vigormaiz_set-group').show();
    }else{
      $('#vigorfrijol_set-group').hide();
      $('#vigormaiz_set-group').hide();
    };

    $('#id_areas_4').change(function(){
        if ($('#id_areas_4').is(':checked')) {
          $('#vigorfrijol_set-group').show();
          $('#vigormaiz_set-group').show();
        }else{
          $('#vigorfrijol_set-group').hide();
          $('#vigormaiz_set-group').hide();
        }
    });

    //plagas y enfermedades
    if ($('#id_areas_5').is(':checked')) {
      $('#plagasfrijol_set-group').show();
      $('#plagasmaiz_set-group').show();
      $('#enfermedadesfrijol_set-group').show();
      $('#enfermedadesmaiz_set-group').show();
    }else{
      $('#plagasfrijol_set-group').hide();
      $('#plagasmaiz_set-group').hide();
      $('#enfermedadesfrijol_set-group').hide();
      $('#enfermedadesmaiz_set-group').hide();
    };

    $('#id_areas_5').change(function(){
        if ($('#id_areas_5').is(':checked')) {
          $('#plagasfrijol_set-group').show();
          $('#plagasmaiz_set-group').show();
          $('#enfermedadesfrijol_set-group').show();
          $('#enfermedadesmaiz_set-group').show();
        }else{
          $('#plagasfrijol_set-group').hide();
          $('#plagasmaiz_set-group').hide();
          $('#enfermedadesfrijol_set-group').hide();
          $('#enfermedadesmaiz_set-group').hide();
        }
    });

    //poblacion
    if ($('#id_areas_6').is(':checked')) {
      $('#poblacion_set-group').show();
      $('#tablapoblacion_set-group').show();
    }else{
      $('#poblacion_set-group').hide();
      $('#tablapoblacion_set-group').hide();
    };

    $('#id_areas_6').change(function(){
        if ($('#id_areas_6').is(':checked')) {
          $('#poblacion_set-group').show();
          $('#tablapoblacion_set-group').show();
        }else{
          $('#poblacion_set-group').hide();
          $('#tablapoblacion_set-group').hide();
        }
    });

    //estimado cosecha
    if ($('#id_areas_7').is(':checked')) {
      $('#estimadocosechafrijol_set-group').show();
      $('#granosplanta_set-group').show();
      $('#estimadocosechamaiz_set-group').show();
      $('#estimadocosechamaiz2_set-group').show();
    }else{
      $('#estimadocosechafrijol_set-group').hide();
      $('#granosplanta_set-group').hide();
      $('#estimadocosechamaiz_set-group').hide();
      $('#estimadocosechamaiz2_set-group').hide();
    };

    $('#id_areas_7').change(function(){
        if ($('#id_areas_7').is(':checked')) {
          $('#estimadocosechafrijol_set-group').show();
          $('#granosplanta_set-group').show();
          $('#estimadocosechamaiz_set-group').show();
          $('#estimadocosechamaiz2_set-group').show();
        }else{
          $('#estimadocosechafrijol_set-group').hide();
          $('#granosplanta_set-group').hide();
          $('#estimadocosechamaiz_set-group').hide();
          $('#estimadocosechamaiz2_set-group').hide();
        }
    });

    //almacenamiento
    if ($('#id_areas_8').is(':checked')) {
      $('#sobrecosecha_set-group').show();
      $('#curadosemilla_set-group').show();
    }else{
      $('#sobrecosecha_set-group').hide();
      $('#curadosemilla_set-group').hide();
    };

    $('#id_areas_8').change(function(){
        if ($('#id_areas_8').is(':checked')) {
          $('#sobrecosecha_set-group').show();
          $('#curadosemilla_set-group').show();
        }else{
          $('#sobrecosecha_set-group').hide();
          $('#curadosemilla_set-group').hide();
        }
    });

  });
})(jQuery || django.jQuery);
