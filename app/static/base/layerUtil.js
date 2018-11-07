var layerUtil =  {


    LAYER_INDEX : 400,

    defaultSettings : {
        shadeClose: false,  //点击空白处关闭true 不关闭false，默认false
        type: 1,
        area: ['600px', 'auto'], //宽高
        zIndex: this.LAYER_INDEX,            //默认值太大，导致select2下拉不出现
        btn: ['提交', '取消']
    },

    alert : function(msg, title, type, option, event) {
        var defAlertSetting = {icon: type, title: title, time : 1000};
        var useOption = $.extend({}, defAlertSetting, option);
        return layer.alert(msg, useOption, event);
    },



    success : function (msg, option, event) {
        var defSetting = {icon: 1, time: 1000};
        var useOption = $.extend({}, defSetting, option);
        return layer.msg(msg, useOption, event);
    },


    fail : function (msg, title, option, event) {
        if (!title) title = '错误';
        return this.alert(msg, title, 5, option, event);
    },


    warn: function (msg, title, option, event) {
        if (!title) title = '警告';
        return this.alert(msg, title, 0, option, event);
    },

    prompt : function(title, success){
        var option = {title : title, formType : 0};
        layer.prompt(option, success);
    },


    confirm: function (msg, event, option) {
        var defSetting = {title: '提示', icon: 3};
        var useOption = $.extend({}, this.defaultSettings, defSetting, option);
        return layer.confirm(msg, useOption, event);
    },


    open: function (title, content, successFun, yesFun, option) {
        option = $.extend({}, option, {title: title, content: content, success: successFun, yes: yesFun});
        var useOption = $.extend({}, this.defaultSettings, option);
        return layer.open(useOption);
    },

    version: 1.0

};