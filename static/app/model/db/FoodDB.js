sap.ui.define([
    "pacbot/model/BaseDb"
], function (BaseDb) {
    "use strict";

    var FoodDB = BaseDb.extend("pacbot.model.db.FoodDB", {});

    FoodDB.allFood = function () {
        return BaseDb.callServer("GET", "/Foods");
    };

    FoodDB.getSelectedFood = function (ch) {
        return BaseDb.callServer("GET", "/s/" + ch);
    };

    FoodDB.SelectedAns = function (level, ans) {
        return BaseDb.callServer("GET", "/SelectedAns/" + level + "/" + ans);
    };

    FoodDB.createUser = function (oUser) {
        return BaseDb.callServer("POST", "/db/Users", oUser);
    };

    FoodDB.updateUser = function (sId, oUser) {
        return BaseDb.callServer("PUT", "/db/Users/" + sId, oUser);
    };

    FoodDB.deleteUser = function (sId) {
        return BaseDb.callServer("DELETE", "/db/Users/" + sId);
    };
    return FoodDB;
});