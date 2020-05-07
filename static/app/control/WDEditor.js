sap.ui.define([
    "jquery.sap.global",
    "sap/ui/core/Control",
    "pacbot/control/WDEditorCodeTemplates"

], function (jQuery, Control, WDEditorCodeTemplates) {
    "use strict";
    var oCodeEditor = Control.extend("pacbot.control.WDEditor", {
        metadata: {
            properties: {
                value: {type: "string", group: "Misc", defaultValue: ""},
                type: {type: "string", group: "Appearance", defaultValue: "json"},
                width: {type: "sap.ui.core.CSSSize", group: "Appearance", defaultValue: "100%"},
                height: {type: "sap.ui.core.CSSSize", group: "Appearance", defaultValue: "600px"},
                editable: {type: "boolean", group: "Behavior", defaultValue: true},
                codeTemplateCategory: {type: "string", defaultValue: ""}
            },
            aggregations: {
                text: {type: "sap.ui.core.Control", multiple: false}
            },
            events: {}
        },

        init: function () {
            this.monacoModel = monaco.editor.createModel("{}", this.getType());
        },

        destroy: function () {
            this._oEditor.dispose();
            this.monacoModel.dispose();
            Control.prototype.destroy && Control.prototype.destroy();
        },

        onBeforeRendering: function () {
            if (oCodeEditor._completionProvider)
                oCodeEditor._completionProvider.dispose();
        },

        onAfterRendering: function () {
            if (this.getCodeTemplateCategory() !== "") {
                oCodeEditor._completionProvider = monaco.languages.registerCompletionItemProvider('json', {
                    provideCompletionItems: function (model, position) {
                        return {
                            suggestions: WDEditorCodeTemplates.getCodeTemplates(this.getCodeTemplateCategory())
                        };
                    }.bind(this)
                });
            }

            setTimeout(function () {
                if (this._oEditor) {
                    this._oEditor.dispose();
                    this._oEditor = undefined;
                }
                this.createEditor();
            }.bind(this), 200);
        },

        setType: function (sValue) {
            if (sValue) {
                monaco.editor.setModelLanguage(this.monacoModel, sValue);
            }
        },

        getValue: function () {
            return this.monacoModel.getValue();
        },

        setEditable: function (bValue) {
            this.setProperty("editable", bValue, true);
            if (this._oEditor)
                this._oEditor.updateOptions({readOnly: !bValue});
            return this;
        },

        setValue: function (sValue) {
            if (sValue === undefined)
                sValue = "";
            this.setProperty("value", sValue, true);
            this.monacoModel.setValue(sValue);
            return this;
        },

        createEditor: function () {
            if (!this.getDomRef())
                return;


            this._oEditor = monaco.editor.create(this.getDomRef(), {
                automaticLayout: true,
                autoIndent: true,
                contextmenu: true,
                formatOnType: true,
                lineNumbers: "on",
                roundedSelection: true,
                scrollBeyondLastLine: false,
                readOnly: !this.getEditable(),
                wordWrap: "on",
                minimap: {enabled: false},
                fixedOverflowWidgets: false,
                theme: "vs-light",
                model: this.monacoModel
            });
        },

        renderer: function (oRm, oControl) {
            oRm.write("<div ");
            oRm.writeControlData(oControl);
            oRm.addClass("sapCEd");
            oRm.addStyle("width", oControl.getWidth());
            oRm.addStyle("height", oControl.getHeight());
            oRm.writeStyles();
            oRm.writeClasses();
            oRm.write(">");
            oRm.write("</div>");
        }
    });

    return oCodeEditor;
});