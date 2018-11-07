let index = new Vue({
    el : "#index",
    data : {
        account : null,
        password : null
    },
    methods : {
        login : function () {
            let url = "/login";
            let params = {
                account : this.account,
                password : this.password
            };
            this.$http.post(url, params, {emulateJSON : true}).then(function (value) {
                let response = value.data
                if(response.success){
                    window.location.href = "/home";
                }else{
                    layerUtil.fail(response.msg)
                }
            });

        },
        register : function () {
            
        }
    },

})
