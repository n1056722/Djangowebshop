$(function () {
    $("#not_login").click(function () {
        window.open('/myshop/login/', target="_self"); //點擊未註冊事件
    })
    $("#regis").click(function () { //點擊註冊事件
        window.open('/myshop/register/', target="_self");
    })
    $("#not_pay").click(function () {
        window.open('/myshop/orderlistnotpay/', target="_self");
    })

})