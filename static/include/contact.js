$(function() {


    $('#contact-form').validator();


    // when the form is submitted
    $('#contact-form').on('submit', function(e) {

        // if the validator does not prevent form submit
        if (!e.isDefaultPrevented()) {
            var url = "contact.php";

            // POST values in the background the the script URL
            $.ajax({
                type: "POST",
                url: "contact.php",
                data: $(this).serialize(),
                success: function(data) {
                    // data = JSON object that contact.php returns

                    // we recieve the type of the message: success x danger and apply it to the 
                    var messageAlert = 'alert-' + data.type;
                    var messageText = data.message;

                    // let's compose Bootstrap alert box HTML
                    var alertBox = '<div class="alert ' + messageAlert + '  alert-dismissible fade show">  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' + messageText + '</div>';

                    // If we have messageAlert and messageText
                        // inject the alert to .messages div in our form
                        $('#contact-form').find('.messages').html(alertBox);
                        // empty the form
                        $('#contact-form')[0].reset();
                }
            });
            return false;
        }
    })
});

$(document).ready(function() {
    var formSubmitted = false; // متغیر برای ذخیره وضعیت ارسال فرم
    
    $('#contact-form').submit(function(e) {
        e.preventDefault();
        
        var name = $('input[name=name]').val();
        var email = $('input[name=email]').val();
        var subject = $('input[name=subject]').val();
        var message = $('textarea[name=message]').val();
        
        if (!formSubmitted && name && email && subject && message) {
            formSubmitted = true; // تنظیم متغیر به true برای جلوگیری از ارسال دوباره فرم
            
            $.ajax({
                type: 'POST',
                url: 'contact.php',
                data: { name: name, email: email, message: message, subject: subject },
                dataType: 'json',
                success: function(data) {
                    var messageAlert = 'alert-' + data.type;
                    var messageText = data.message;
                    var alertBox = '<div class="alert ' + messageAlert + ' alert-dismissible fade show">' +
                                    '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                                    messageText + '</div>';
                    $('#contact-form').find('.messages').html(alertBox);
                    $('#contact-form')[0].reset();
                },
                error: function(xhr, status, error) {
                    console.error(xhr.responseText);
                    $('#contact-form').find('.messages').html('<div class="alert alert-danger">خطا در ارسال اطلاعات.</div>');
                }
            });
        }
    });
});
