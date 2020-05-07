sap.ui.define([
        "pacbot/controller/BaseController",
        "pacbot/model/DbManager",
        "pacbot/utils/MessageHelper",
        "sap/m/MessageBox",
        "pacbot/utils/Constants",
        "sap/ui/model/json/JSONModel",
        "pacbot/model/db/FoodDB",
        "pacbot/utils/Formatter"
    ],

    function (BaseController, DbManager, MessageHelper, MessageBox, Constants, JSONModel, FoodDB, Formatter) {
        "use strict";
        return BaseController.extend("pacbot.controller.Editor", {
            formatter: Formatter,

            onInit: function () {
                BaseController.prototype.onInit.apply(this, arguments);

                this.getRouter().getRoute('home').attachPatternMatched(this._onRouteMatched, this);

                this.setModel(new JSONModel({
                    'Questions': [],
                    Food: []
                }), "mainModel");

            },

            _onRouteMatched: function (oEvent) {
                //var oParams = oEvent.getParameter('arguments');
                let oMainModel = this.getModel("mainModel");
                FoodDB.SelectedAns(99, 'Yes').then(function (oData) {
                    oMainModel.setProperty('/Questions/0', oData.Data);
                    this.setViewBusy(false);
                }.bind(this), function (oError) {
                    this.setViewBusy(false);
                }.bind(this));
            },

            getAllFoods: function () {
                var oMainModel = this.getModel("mainModel");
                this.setViewBusy(true);
                FoodDB.allFood().then(function (oData) {
                    oMainModel.setProperty("/Food", oData);
                    this.setViewBusy(false);
                }.bind(this), function (oError) {
                    // MessageHelper.showSystemError(oError);
                    this.setViewBusy(false);
                }.bind(this));
            },

            getSelectedFood: function () {
                var oMainModel = this.getModel("mainModel");
                this.setViewBusy(true);
                var opt =
                    FoodDB.getSelectedFood(opt).then(function (oData) {
                        oMainModel.setProperty("/Food", oData);

                        this.setViewBusy(false);
                    }.bind(this), function (oError) {
                        // MessageHelper.showSystemError(oError);
                        this.setViewBusy(false);
                    }.bind(this));
            },
            productListFactory: function (sId, oContext) {
                var oUIControl;
                oUIControl = this.byId("productSimple").clone(sId);
                var da = $(oUIControl.getDomRef());
                // var da = oUIControl.$();
                // da.ready(function(){
                //     da.animate({height: "300px"});
                // });

                /*	da.promise().done(function( arg1 ) {
                        if(arg1.length > 0)
                        arg1.context.animate({height: "300px"});
                        });*/
                //$a.classList.add('animated', 'bounceOutLeft')
                // $a.animate.css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
                // $a.animate.css({opacity: 1.0, visibility: "visible"}).animate({opacity: 0.0});
                //$a.animate({visible:'true'},"slow");
                // $a.animate({visible:'false'},"slow");
                // $a.animate({visible:'true'},"slow");
                //$a.animate({bottom: '250px'}, 2000, 'swing');
                return oUIControl;
            },
            updateFinished: function (d, f) {
                /* var oC = d.getSource().getItems()[0];
                 if (oC) {
                     oC.setVisible(false);
                     setTimeout(function () {
                         oC.setVisible(true);
                     }, 2000);
                 }*/
            },
            onSelectAnswer: function (oEvent) {
                let oContext = oEvent.getSource().getBindingContext('mainModel');
                //oContext.getObject().selected = true;     //.setSelected(true);
               // oContext.setProperty(oContext.getPath() + "/selected", true);
                let oLevel = oContext.getModel().getProperty('/Questions/' + oContext.getPath().split('/')[2] + '/level');
                //oContext.getModel().setProperty('/Questions/' + oContext.getPath().split('/')[2] + '/selected', true);
                let oSelected = oContext.getObject().name;
                let oMainModel = this.getModel("mainModel");
                let that = this;
                if (oSelected === 'No') {
                    oLevel = (oLevel === 0) ? '101' : '102'
                }
                //oMainModel.refresh();


                FoodDB.SelectedAns(parseInt(oLevel), oSelected).then(function (oData) {
                    if (oData.action === 'do') {
                        var ok = true;
                        var pQuestions = oMainModel.getData().Questions;
                        for (var i = 0; i < pQuestions.length; i++) {
                            if (pQuestions[i].level == oData.Data.level) {
                                pQuestions[i] = oData.Data;
                                ok = false;
                            }
                        }
                        if (ok)
                            oMainModel.getData().Questions.unshift(oData.Data);
                    } else if (oData.action === 'no') {
                        oMainModel.getData().Questions = [oData.Data];

                    }
                    // var $a = $(that.getView().byId('chatList').getDomRef());
                    // $a.animate({bottom: '250px'}, 2000, 'swing');
                    oMainModel.refresh();
                    this.setViewBusy(false);
                }.bind(this), function (oError) {
                    this.setViewBusy(false);
                }.bind(this));
            }
        });
    });
