odoo.define('bugs.Column', function (require) {

    "use strict";
    var config = require('web.config');
    var KanbanColumn = require('web_kanban.Column');

    KanbanColumn.include({
        start: function() {

            var self = this;
            this.$header = this.$('.o_kanban_header');

            for (var i = 0; i < this.data_records.length; i++) {
                this.add_record(this.data_records[i], {no_update: true});
            }
            this.$header.tooltip();
            if (config.device.size_class > config.device.SIZES.XS) {
                // deactivate sortable in mobile mode.  It does not work anyway,
                // and it breaks horizontal scrolling in kanban views.  Someday, we
                // should find a way to use the touch events to make sortable work.
                this.$el.sortable({
                    connectWith: '.o_kanban_group',
                    revert: 0,
                    delay: 0,
                    items: '> .o_kanban_record',
                    helper: 'clone',
                    cursor: 'move',
                    over: function () {
                        self.$el.addClass('o_kanban_hover');
                        self.update_column();
                    },
                    out: function () {
                        self.$el.removeClass('o_kanban_hover');
                    },
                    update: function (event, ui) {
                        var record = ui.item.data('record');
                        var index = self.records.indexOf(record);
                        var test2 = $.contains(self.$el[0], record.$el[0]);
                        // comment out forced style
                        //record.$el.removeAttr('style');  // jqueryui sortable add display:block inline
                        if (index >= 0 && test2) {
                            // resequencing records
                            self.trigger_up('kanban_column_resequence');
                        } else if (index >= 0 && !test2) {
                            // removing record from this column
                            self.records.splice(self.records.indexOf(record), 1);
                            self.dataset.remove_ids([record.id]);
                        } else {
                            // adding record to this column
                            self.records.push(record);
                            record.setParent(self);
                            self.trigger_up('kanban_column_add_record', {record: record});
                        }
                        self.update_column();
                    }
                });
            }
            this.update_column();
            this.$el.click(function (event) {
                if (self.$el.hasClass('o_column_folded')) {
                    event.preventDefault();
                    self.folded = false;
                    self.update_column();
                }
            });
        },
    });

});