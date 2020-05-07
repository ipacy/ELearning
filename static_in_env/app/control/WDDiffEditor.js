sap.ui.define([
    "sap/ui/core/Control",
    "vs/loader",
    "vs/editor/editor.main.nls",
    "vs/editor/editor.main"
], function (Control, Loader, Editornls, Editormain) {
    "use strict";
    var oCodeEditor = Control.extend("pacbot.control.WDDiffEditor", {
        metadata: {
            properties: {
                value: { type: "string", defaultValue: ""},
                type: {type: "string", defaultValue: "json"},
                width: {type: "sap.ui.core.CSSSize", defaultValue: "100%"},
                height: {type: "sap.ui.core.CSSSize", defaultValue: "100%"},
                editable: {type: "boolean", defaultValue: false},
                editorType: {type: "string", defaultValue: "ICodeEditor"},
                modelData: {type: "object", defaultValue: {}},
                modelX: {type: "string", defaultValue: ""},
                modelY: {type: "string", defaultValue: ""}
            },

            aggregations: {
                text: {type: "sap.ui.core.Control", multiple: false}
            },

            events: {
                liveChange: {},
                change: {}
            },
        },

        init: function () {
            this.originalModel = monaco.editor.createModel("{}", "text/json");
            this.modifiedModel = monaco.editor.createModel("{}", "text/json");
        },

        destroy: function () {
            this._oEditor.dispose();
            this.modifiedModel.dispose();
            this.originalModel.dispose();
            Control.prototype.destroy && Control.prototype.destroy();
        },

        onAfterRendering: function () {
            setTimeout(function () {
                if (this._oEditor) {
                    this._oEditor.dispose();
                    this._oEditor = undefined;
                }
                this.createEditor();
            }.bind(this));
        },

        createEditor: function () {
            this._oEditor = monaco.editor.createDiffEditor(this.getDomRef(), {
                originalIsEditable: true,
                enableSplitViewResizing: false,
                automaticLayout: true,
                autoIndent: true,
                contextmenu: false,
                formatOnType: true,
                lineNumbers: "on",
                roundedSelection: true,
                scrollBeyondLastLine: false,
                readOnly: !this.getEditable(),
                wordWrap: "on",
                minimap: {enabled: false},
                fixedOverflowWidgets: false,
                theme: "vs-light",
            });

            this._oEditor.setModel({
                original: this.originalModel,
                modified: this.modifiedModel,
            });
        },

        setEditable: function (bValue) {
            this.setProperty("editable", bValue, true);
            if (this._oEditor)
                this._oEditor.getModifiedEditor().updateOptions({readOnly: !bValue});
            return this;
        },

        setModelData: function (oValue) {
            if (oValue && oValue.original && oValue.modified) {
                this.originalModel.setValue(oValue.original);
                this.modifiedModel.setValue(oValue.modified);
            }

        },

        setHeight: function (bValue) {
            this.setProperty("height", bValue);
        },

        setWidth: function (bValue) {
            this.setProperty("width", bValue);
        },

        setType: function (sValue) {
            if (sValue) {
                monaco.editor.setModelLanguage(this.originalModel, sValue);
                monaco.editor.setModelLanguage(this.modifiedModel, sValue);
            }
        },

        renderer: {
            render: function (oRm, oControl) {
                oRm.write("<div ");
                oRm.writeControlData(oControl);
                oRm.addStyle("width", oControl.getWidth());
                oRm.addStyle("height", oControl.getHeight());
                oRm.writeStyles();
                oRm.write(">");
                oRm.write("</div>");
            }
        }
    });

    return oCodeEditor;
});
