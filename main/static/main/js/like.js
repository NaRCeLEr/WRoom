a = '{{posts}}'
console.log(a)
var like = document.getElementById('ch');
a = function Num(el) {
    var name = el.name;
    return name
}

$(document).on('click', 'input', function(e) {
    e.preventDefault();
    input = $(this).name
    var form = $(this).closest("form");
    $.ajax({
        type: 'POST',
        url: "",
        data: {
            check: $('#ch').val(),
            name: $(this).attr('name'),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }
    });
    
});


// function a(el,  e) {
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url: "",
//         data: {
//             check: $('#ch').val(),
//             name: $('input').val(),
//             a: el.name,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         }
//     });
// }