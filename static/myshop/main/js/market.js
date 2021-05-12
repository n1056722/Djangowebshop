$(function () {
    $("#all_types").click(
        function () {
            console.log("全部類型");
            var $all_types_container = $("#all_types_container");
            $all_types_container.show();
            var $all_type = $(this);
            var $span = $all_type.find("span").find("span");
            $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
            var $sort_rule_container = $("#sort_rule_container");
            $sort_rule_container.slideUp();
            var $sort_rule = $("#sort_rule");
            var $span_sort_ruie = $sort_rule.find("span").find("span")
            $span_sort_ruie.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
        }
    )
    $("#all_types_container").click(function () {
        var $all_type_container = $(this);
        $all_type_container.hide();
        var $all_type = $("#all_types");
        var $span = $all_type.find("span").find("span");
        $span.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
    })

    $("#sort_rule").click(
        function () {
            console.log("排序規則");
            var $sort_rule_container = $("#sort_rule_container");
            $sort_rule_container.slideDown();
            var $sort_rule = $(this);
            var $span = $sort_rule.find("span").find("span")
            $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
            var $all_type_container = $("#all_types_container");
            $all_type_container.hide();
            var $all_type = $("#all_types");
            var $span_all_type = $all_type.find("span").find("span");
            $span_all_type.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
        }
    )
    $("#sort_rule_container").click(function () {
        var $sort_rule_container = $(this);
        $sort_rule_container.slideUp();
        var $sort_rule = $("#sort_rule");
        var $span = $sort_rule.find("span").find("span")
        $span.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    })
    $(".subShopping").click(function () {
        console.log('sub');

    })
    $(".addShopping").click(function () {
        console.log('add');
        var $add = $(this);
        var goodsid = $add.attr('goodsid');
        $.get('/myshop/addtocart/', {'goodsid': goodsid}, function (data) {
            console.log(data);
            if (data['status'] === 302) {
                window.open('/myshop/login', target = "_self");
            } else if (data['status'] === 200) {
                $add.prev().html(data['c_goods_num']);
            }
        })
    })
})