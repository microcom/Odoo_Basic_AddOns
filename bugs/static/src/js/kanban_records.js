odoo.define('bugs.Record', function (require) {
    "use strict";

    var KanbanRecord = require('web_kanban.Record');

    KanbanRecord.include({
        renderElement: function () {
            var self = this;
            this.record_id = self.id;
            this._super();
            this.setup_color_picker();
            this.$el.addClass('o_kanban_record');
            // use t-att-data-color as background color
            if (this.__parentedParent.__parentedParent.model == 'bugs.bug') {
                var color = this.$el.data().color;
                this.$el.css('background-color', color);

                this.$el.data('record', this);
                if (this.$el.hasClass('oe_kanban_global_click') || this.$el.hasClass('oe_kanban_global_click_edit')) {
                    this.$el.on('click', this.proxy('on_global_click'));
                }
            }
        },
    });
});
