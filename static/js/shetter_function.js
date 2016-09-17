var get_start_hour = function(){
    d = $("#start").val().split(":")[0];
    return d;
}
var get_end_hour = function(){
    d = $("#end").val().split(":")[0];
    return d;
}
$(".time").on('change', function(e) {
    regen();
});
regen = function(){
    $(function(){
        get_start_hour(),
        $.ajax({
            type: 'POST',
            url: '/search',
            dataType: 'json',
            data: {
                date: get_date,
                start_hour: get_start_hour(),
                end_hour: get_end_hour(),
            },
            success: function(data){
                //console.info(data);
                $("#p").empty();
                for(p in data){
                    profile = "<tr>" +
                        "<td>" +
						"<a href='./profiles/" + data[p].id + "'>"  + data[p].name + "</a> " +
						"</td>" +
                        "<td>" + data[p].address + "</td>" +
                        "</tr>";
                    $("#p").append(profile);
                }
            },
            error: function(e) {         // HTTPエラー時
                console.error(e);
            },
        });
    });
}
regen();
