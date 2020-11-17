
// calling the url to get response . if given input is numbers it will call the url
// send response to user.

  jQuery(document).ready(function($){
             $('#input_number').change(function(){
             var input_number = $("#input_number").val();
             if ($.isNumeric(input_number)){
                    $.ajax({
                 url: "http://"+window.location.host+"/stably/get-prime-number/"+input_number,
                 context: document.body
                }).done(function(responseText) {
                    $('#prime_number').html("")
                  $('#prime_number').append(responseText.response);
                });
             }
             else {
                 $('#prime_number').html("")
                 $('#prime_number').append("please enter natural numbers  .  <b>"+input_number+"</b>   not a number");
             }

        });

       });

// page loader
$body = $("body");
$(document).on({
    ajaxStart: function() { $body.addClass("loading"); },
     ajaxStop: function() { $body.removeClass("loading"); }
});