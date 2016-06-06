function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
jQuery('#in_purchase_select_group').on('change', function () {
    var selected_group_id = jQuery(this).val();
    if (!selected_group_id) {
        return false;
    }
    jQuery.ajax({
        url: '/group/' + selected_group_id + '/members',
        method: 'GET',
        beforeSend: function () {
            jQuery('#msg').text('لطفا منتظر بمانید...');
        },
        data: {csrfmiddlewaretoken: csrftoken}
    }).done(function(data){
        var html = '';
        jQuery('#msg').text('');
        jQuery.each(data, function (key, person) {
            var p = person;
            person = p.fields;
            html = html + '<tr>' +
                '<td>'+ (key + 1) +'</td>' +
                '<td class="tp-text-align-right"> '+ person.name +'</td>' +
                '<td><input name="portions:'+ p.pk +'" id="portion_id_'+p.pk+'" type="text" placeholder="0"></td>' +
                '</tr>';
        });
        jQuery('#users_group tr:gt(0)').remove();
        jQuery('#users_group tr:eq(0)').after(html);
        jQuery('#users_group').fadeIn(200);
    }).fail(function () {
        jQuery('#msg').text('دریافت اطلاعات با خطا مواجه شده است.');
    })
})

function filterByGroupId (group_id) {
    if ( group_id == undefined ) {
        group_id = 0
    }
    alert("#felbedahe")
}

function sendReciptionMailMessage( ) {
    alert("are you kidding me? :| #portavaqo")
}