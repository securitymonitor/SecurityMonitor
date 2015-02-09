$('table .checkbox input').click( function() {            
    if($(this).is(':checked')){            
        $(this).parent().parent().parent().toggleClass('row_selected');                    
        }
    else{    
        $(this).parent().parent().parent().toggleClass('row_selected');        
        }
    });