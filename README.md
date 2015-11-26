# To Use:

1. Install with pip -e . within this folder within the edx platform virtual environment.
2. Add "custom_reg_form" to the "ADDL_INSTALLED_APPS" array in `lms.env.json` (you may have to create it if it doesn't exist.)
3. Set "REGISTRATION_EXTENSION_FORM" to "custom_reg_form.forms.ExtraInfoForm" in `lms.env.json`.
4. Run migrations.
5. Start/restart the LMS.
