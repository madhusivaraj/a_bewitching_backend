
//var form = $('#ajax-flicker');
//var formMessages = $('#flicker-messages');

// $(function() {
//     // Get the form.
//     var form = $('#ajax-flicker');

//     // Get the messages div.
//     var formMessages = $('#flicker-messages');

//     // Set up an event listener for the contact form.
// 	$.ajax({
//             type: 'POST',
//             url: $(form).attr('action'),
//             data: formData
//     })
// });

function flicker(){
    $.ajax({
        type: 'POST',
        url: '/flicker'
    });
}