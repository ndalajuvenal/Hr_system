/* --------------------------------------------- 
# SCRIPTS 
--------------------------------------------- */

// 1) Script to auto close the alert after 3s


/* --------------------------------------------- 
validation
--------------------------------------------- */

$(document).ready(function(){
    
    $(".phone").inputmask("(999) 999 999 999",{"onincomplete": function(){
        swal("Opss !","Numero de telephone incorrect","info");
        return false;
    }});
});

