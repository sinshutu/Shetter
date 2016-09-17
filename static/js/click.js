date = 18;
tmp = $(".date").get(0);
$(".date").click(function(){
    $(this).css("background-color", "red");
    date = this.innerHTML;
    regen();
    console.info(date);
});
get_date = function(){
    return date;
}
