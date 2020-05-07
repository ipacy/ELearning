sap.ui.define([],
    function (Constants) {
        "use strict";
        return {

            getCodeTemplates: function (category) {
                var result = [];
                if (category === "" || !category || category === undefined) {
                    return result;
                }

                var templates = this.getTemplates(category);


                for (var i = 0; i < templates.length; i++) {
                    result.push({
                        label: templates[i].Label,
                        kind: monaco.languages.CompletionItemKind.Function,
                        documentation: templates[i].Description,
                        insertText: this.getJsonToString(templates[i].Code)
                    });
                }

                return result;
            },

            getJsonToString: function (template) {
                return JSON.stringify(template, null, 4);
            },

            getTemplates: function (category) {
                var result = [];

                for (var i = 0; i < this.TemplateCategories.length; i++) {
                    if (this.TemplateCategories[i].Name === category) {
                        result = this.TemplateCategories[i].Templates;
                        break;
                    }
                }

                return result;
            },

            TemplateCategories: [
                {
                    Name: "Placeholder",
                    Templates: [
                        {
                            Label: "placeholder",
                            Description: "Creates new placeholder for the widget.",
                            Code: {
                                Type: "sap.",
                                id: "&PL1&"
                            }
                        }
                    ]
                },
                {
                    Name: "Metadata",
                    Templates: [
                        {
                            Label: "metadata-full",
                            Description: "Creates metadata for the widget.",
                            Code: [
                                {
                                    Id: "PL1",
                                    Label: "",
                                    Category: "id",
                                    Collection: "0",
                                    Hidden: "1",
                                    Type: "string",
                                    Default: "",
                                    ChildWidgets: [],
                                    Values: []
                                }]
                        },
                        {
                            Label: "metadata",
                            Description: "Creates new metadata object.",
                            Code: {
                                Id: "",
                                Label: "",
                                Category: "",
                                Collection: "0",
                                Hidden: "0",
                                Type: "string",
                                Default: "",
                                ChildWidgets: [],
                                Values: []
                            }
                        }
                    ]
                },
                {
                    Name: "Events",
                    Templates: [
                        {
                            Label: "event",
                            Description: "Creates new event for the widget.",
                            Code: {
                                "Id": "PL1",
                                "Name": "press",
                                "Label": "Press",
                                "Handlers": []
                            }
                        },
                        {
                            Label: "events",
                            Description: "Creates new event for the widget.",
                            Code: [{
                                "Id": "PL1",
                                "Name": "press",
                                "Label": "Press",
                                "Handlers": []
                            }]
                        }
                    ]
                },
                {
                    Name: "PlaceholderGroups",
                    Templates: [
                        {
                            Label: "placeholder-group",
                            Description: "Creates new placeholder group for the widget.",
                            Code: []
                        }
                    ]
                },
                {
                    Name: "Overview",
                    Templates: [
                        {
                            Label: "overview",
                            Description: "Creates new overview for the widget.",
                            Code: []
                        }
                    ]
                },
                {
                    Name: "Configuration",
                    Templates: [
                        {
                            Label: "configuration",
                            Description: "Creates new configuration for the widget.",
                            Code: {
                                "Key": "IsContextRequired",
                                "Value": true
                            }
                        }
                    ]
                },
                {
                    Name: "DisplayWidgets",
                    Templates: [
                        {
                            Label: "display-widget",
                            Description: "Creates new display widget for the widget.",
                            Code: []
                        }
                    ]
                },
                {
                    Name: "Code",
                    Templates: [
                        {
                            Label: "code",
                            Description: "Creates new code for the widget.",
                            Code: {}
                        }
                    ]
                },
                {
                    Name: "Data",
                    Templates: [
                        {
                            Label: "data",
                            Description: "Creates new data for the widget.",
                            Code: {}
                        }
                    ]
                }
            ]
        };
    }
);
