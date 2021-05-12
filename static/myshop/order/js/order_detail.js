$(function () {
    $("#paypal").click(function () {
        console.log("付款");
        var orderid = $(this).attr("orderid");
        $.getJSON("/myshop/payed/", {"orderid": orderid}, function (data) {
            console.log(data)
            if (data['status']===200){
                window.open("/myshop/mine/", target="_self");
            }
        })
    })
})
