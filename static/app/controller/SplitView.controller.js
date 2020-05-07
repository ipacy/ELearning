sap.ui.define([
        "pacbot/controller/BaseController",
],

    function (BaseController) {
        "use strict";
        return BaseController.extend("pacbot.controller.SplitView", {

            onInit: function () {
                BaseController.prototype.onInit.apply(this, arguments);
            }

        });
    });
