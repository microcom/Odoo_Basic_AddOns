openerp.birthdate_widget = function(instance) {

    "use strict";

    instance.birthdate_widget.FieldBirthdate = instance.web.form.FieldDate.extend({
        build_widget: function() {
            return new instance.birthdate_widget.BirthdateWidget(this);
        }
    });

    instance.birthdate_widget.BirthdateWidget = instance.web.DateWidget.extend({
        jqueryui_object: 'datepicker',
        type_of_date: "date",
        start: function() {
            this._super();
            this.picker("option", "yearRange", "c-100:+0");
        }
    });

    instance.web.form.widgets.add('birthdate', 'instance.birthdate_widget.FieldBirthdate');
};
