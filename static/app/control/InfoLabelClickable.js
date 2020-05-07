sap.ui.define([
    "sap/tnt/InfoLabel"
], function (InfoLabel) {
    "use strict";
    var oControl = InfoLabel.extend("pacbot.control.InfoLabelClickable", {
        metadata: {
            properties: {
            },
            aggregations: {
            },
            associations: {
            },
            events: {
                press: {

                }
            }
        },

        renderer: {}
    });

    oControl.prototype.onclick = function () {
        this.firePress();
    };

    oControl.prototype.onmouseover = function () {
        this.$().css("cursor","pointer");
    };
    return oControl;
});