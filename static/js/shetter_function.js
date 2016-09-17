$(function(){
    $.ajax({
	type: 'GET',
        url: 'http://127.0.0.1:5000/test2',
	//data:JSON.stringify(data),
	dataType: 'json',
	success: function(JSON.parse(data)){
	    var dataArray = data;
	    $.each(dataArray, function(i){
   		$(".nameData").append("<p>" + dataArray[i].a + dataArray[i].b + "</p>");
	    });

	},
	error: function() {         // HTTPエラー時
            alert("Server Error. Pleasy try again later.");
        },
    });
});

/*function get_data(id)
$(function(){
    $.ajax({
	type: 'get',
        url: 'http://127.0.0.1:5000/profiles/${id}',
	dataType: 'json',
	data:JSON.stringify(data),
	success: function(data){
	    var dataArray = data;
	    $.each(dataArray, function(i){
   		$(".nameData").append("<p>" + dataArray[i].id + dataArray[i]. + "</p>");
		//$(".nameData").append("<p>id: " + dataArray[i].id + "　Name: " + dataArray[i].name + " Address " + dataArray[i].address + " "　　(CV: " + dataArray[i].cv + ")</p>");
	    });

	}
	error: function() {         // HTTPエラー時
            alert("Server Error. Pleasy try again later.");
        },
    });
})*/


