odoo.define('custom_treeview_colors.ListView', function (require) {
"use strict";

var listView = require('web.ListView');

var core = require('web.core');
var data = require('web.data');
var DataExport = require('web.DataExport');
var formats = require('web.formats');
var common = require('web.list_common');
var Model = require('web.DataModel');
var pyeval = require('web.pyeval');
var session = require('web.session');
var Sidebar = require('web.Sidebar');
var utils = require('web.utils');
var View = require('web.View');

var Class = core.Class;
var _t = core._t;
var _lt = core._lt;
var QWeb = core.qweb;
var list_widget_registry = core.list_widget_registry;

var row_decoration = [
    'decoration-bf',
    'decoration-it',
    'decoration-danger',
    'decoration-info',
    'decoration-muted',
    'decoration-primary',
    'decoration-success',
    'decoration-warning',
    'green-font',
    'yellow-font',
    'yellow-background',
    'red-background',
    'blue-background'//,
    /*
        add your new style here
    */
];

listView.include({

    compute_decoration_classnames: function (record) {
        var classnames= '';
        var context = _.extend({}, record.attributes, {
            uid: session.uid,
            current_date: moment().format('YYYY-MM-DD')
            // TODO: time, datetime, relativedelta
        });

        _.each(this.decoration, function(expr, decoration) {
            if (py.PY_isTrue(py.evaluate(expr, context))) {
                if(decoration.match(/^decoration-/)) {
                    // default behaviour
                    classnames += ' ' + decoration.replace('decoration', 'text');
                } else {
                    // otherwise we simply add our new class name
                    classnames += ' ' + decoration;
                }
            }
        });
        return classnames;
    },

    load_list: function(data) {
        var self = this;
        this.fields_view = data;
        this.name = "" + this.fields_view.arch.attrs.string;
        this._limit = parseInt(this.fields_view.arch.attrs.limit, 10) || this._limit;

        // Retrieve the decoration defined on the model's list view
        this.decoration = _.pick(this.fields_view.arch.attrs, function(value, key) {
            return row_decoration.indexOf(key) >= 0;
        });
        this.decoration = _.mapObject(this.decoration, function(value) {
            return py.parse(py.tokenize(value));
        });

        this.setup_columns(this.fields_view.fields, this.grouped);

        this.$el.html(QWeb.render(this._template, this));
        this.$el.addClass(this.fields_view.arch.attrs['class']);

        // Head hook
        // Selecting records
        this.$el.find('.oe_list_record_selector').click(function(){
            self.$el.find('.oe_list_record_selector input').prop('checked',
                self.$el.find('.oe_list_record_selector').prop('checked')  || false);
            var selection = self.groups.get_selection();
            $(self.groups).trigger(
                'selected', [selection.ids, selection.records]);
        });

        //Sort
        var default_order = this.fields_view.arch.attrs.default_order,
            unsorted = !this.dataset._sort.length;
        if (unsorted && default_order && !this.grouped) {
            this.dataset.set_sort(default_order.split(','));
        }

        if(this.dataset._sort.length){
            if(this.dataset._sort[0].indexOf('-') == -1){
                this.$el.find('th[data-id=' + this.dataset._sort[0] + ']').addClass("sortdown");
            }else {
                this.$el.find('th[data-id=' + this.dataset._sort[0].split('-')[1] + ']').addClass("sortup");
            }
        }
        this.trigger('list_view_loaded', data, this.grouped);
    }
});

});
