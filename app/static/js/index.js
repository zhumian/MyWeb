let index = new Vue({
    el : "#index",
    data : {
        account : null,
        password : null
    },
    methods : {
        login : function () {
            let params = {
                account : this.account,
                password : this.password
            };
            /*this.$http.post(url, params).then(function (value) {

            })*/
            $.ajax({
                url : "/login",
                data : params,
                type : "post",
                success : function (data) {
                    
                }
            })
        }
    },

})