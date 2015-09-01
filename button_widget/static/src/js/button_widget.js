(function () {
    var instance = openerp,
        _t = instance.web._t;

    instance.web.form.FieldBooleanButton = instance.web.form.AbstractField.extend({
        template: 'FieldBooleanButton',
        start: function() {
            var self = this;
            this.ACTIVE_STRING = _t('Active')
            this.DISABLED_STRING = _t('Disabled')
            this.$booleanButton = $("input", this.$el);
            this.setupFocus(this.$booleanButton);
            this.$booleanButton.click(_.bind(function() {
                this.$booleanButton.toggleClass('active');
                this.$booleanButton.hasClass('active') ? this.$booleanButton.val(this.ACTIVE_STRING) : this.$booleanButton.val(this.DISABLED_STRING);
                this.internal_set_value(this.$booleanButton.hasClass('active'));
            }, this));
            var check_readonly = function() {
                self.$booleanButton.prop('disabled', self.get("effective_readonly"));
                self.click_disabled_boolean();
            };
            this.on("change:effective_readonly", this, check_readonly);
            check_readonly.call(this);
            this._super.apply(this, arguments);
        },
        render_value: function() {
            if (this.get('value')) {
                this.$booleanButton.addClass("active");
                this.$booleanButton.val(this.ACTIVE_STRING)
            } else {
                this.$booleanButton.val(this.DISABLED_STRING)
            }
        },
        focus: function() {
            var input = this.$booleanButton && this.$booleanButton[0];
            return input ? input.focus() : false;
        },
        click_disabled_boolean: function(){
            var $disabled = this.$el.find('input[type=button]:disabled');
            $disabled.each(function (){
                $(this).next('div').remove();
                $(this).closest("span").append($('<div class="boolean"></div>'));
            });
        }
    });

    instance.web.form.widgets.add('changebutton', 'instance.web.form.FieldBooleanButton');
})();
