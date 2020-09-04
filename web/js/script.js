function getRadioVal(form, name) {
    var val;
    // get list of radio buttons with specified name
    var radios = form.elements[name];
    
    // loop through list of radio buttons
    for (var i=0, len=radios.length; i<len; i++) {
        if ( radios[i].checked ) { // radio checked?
            val = radios[i].value; // if so, hold its value in val
            break; // and break out of for loop
        }
    }
    return val; // return value of checked radio or undefined if none checked
}



$(function(){                    
	$(".button_confirm").click(function(){
        eel.get_info($(".input_name").val(), getRadioVal( document.getElementById('input_gender'), 'gender' ), $(".input_age").val());
        window.location = "../html/main.html";
	});
});


