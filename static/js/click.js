date = 18;
$(".date").click(function(){
    redate();
    $(this).css("background-color", "red");
    date = this.innerHTML;
    regen();
    console.info(date);
});
get_date = function(){
    return date;
}
redate = function(){
    a = $(".date");
    for(var i=0;i<a.length;i++){
        console.info(a.get(i));
        $(a.get(i)).css("background-color", "#fff");
    }
}
