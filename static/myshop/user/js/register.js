$(function () {
    var $username = $("#username_input");
    $username.change(function () {
        var username = $username.val().trim();
        if (username.length) {
            $.getJSON('/myshop/checkuser/', {'username': username}, function (data) {
                console.log(data);
                var $username_info = $("#username_info")
                if (data['status'] === 200) {
                    $username_info.html("帳戶名稱可用").css('color', 'green');
                } else if (data['status'] === 901) {
                    $username_info.html("該帳戶已存在").css('color', 'red');
                }
            })
            //利用帳號發送給伺服器進行預先檢驗

        }
    });
    //密碼驗證
    check_password();

});

$(function () {
    var $email = $("#email_input");
    $email.change(function () {
        var email = $email.val().trim();
        if (email.length) {
            $.post('/myshop/checkemail/', {'email': email}, function (data) {
                console.log(data);
                var $email_info = $("#email_info")
                if (data['status'] === 200) {
                    $email_info.html("電子郵件可用").css('color', 'green');
                } else if (data['status'] === 902) {
                    $email_info.html("該郵件已存在").css('color', 'red');
                }
            })
            //利用帳號發送給伺服器進行預先檢驗

        }
    })

})


//使用者帳號校驗
function check() {
    var $username = $("#username_input");
    var username = $username.val().trim();
    if (!username) {
        return false
    }
    var info_color = $("#username_info").css('color');
    console.log(info_color);
    if (info_color == 'rgb(255, 0, 0)') {
        return false
    }
    var $password_input = $("#password_input");
    var password = $password_input.val().trim();

    $password_input.val(md5(password));

    return true
}

//密碼驗證
function check_password() {
    var $password = $('#password_input');
    var $confirm = $('#password_confirm_input');

    $confirm.blur(function () {
        var password = $password.val();
        var confirm = $confirm.val();
        if (password != confirm) {
            $('#password_confirm_info').text('密碼不一致').css({color: 'red'});

        } else {
            $('#password_confirm_info').text('密碼相同可使用').css({color: 'green'});
        }
        if (!password | !confirm) {
            $('#password_confirm_info').text('不能為空').css({color: 'red'});
        }

    })

}