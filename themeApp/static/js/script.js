jQuery('#in_purchase_select_group').on('change', function () {
    var selected_group_id = jQuery(this).val();
    jQuery.ajax({
        url: '/group/' + selected_group_id + '/users',
        method: 'POST',
        beforeSend: function () {
            jQuery('#msg').text('لطفا منتظر بمانید...');
        },
        data: {}
    }).done(function(data){
        var html = '';
        jQuery('#msg').text('');
        jQuery.each(data, function (person, key) {
            html = html + '<tr>' +
                '<td>'+ key + 1 +'</td>' +
                '<td class="tp-text-align-right"> '+ person.name +'</td>' +
                '<td><input name="portion['+person.id+'][]" id="portion_id_'+person.id+'" type="text" placeholder="0"></td>' +
                '</tr>'
        });
        jQuery('#users_group').fadeIn(200, function () {
            jQuery('#users_group tr.data:gt(1)').remove();
            jQuery('#users_group tr.data:eq(1)').after(html);
        });
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