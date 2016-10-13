from selenium.webdriver.common.by import By

"""Login page elements locators"""
login_locators = {
    "email_field": (By.ID, 'user_email'),
    "password_field": (By.ID, 'user_password'),
    "login_button": (By.TAG_NAME, 'button'),
    "title": (By.TAG_NAME, 'h3')
}

"""Header elements locators"""
header_locators = {
    "base_branding": (By.CLASS_NAME, 'base-branding'),
    "dashboard_icon": (By.ID, 'nav-dashboard'),
    "leads_icon": (By.ID, 'nav-leads'),
    "contacts_icon": (By.ID, 'nav-contacts'),
    "sales_pipeline_icon": (By.ID, 'nav-sales'),
    "calendar_icon": (By.ID, 'nav-calendar'),
    "tasks_icon": (By.ID, 'nav-tasks'),
    "communication_center_icon": (By.ID, 'nav-communication-center'),
    "reports_icon": (By.ID, 'nav-reports'),
    "notification_icon": (By.ID, 'notifications-widget'),
    "phone_icon": (By.ID, 'quick-add'),
    "search_field": (By.CLASS_NAME, 'navbar-search'),
    "user_info_icon": (By.ID, 'user-dd'),
    "profile_settings": (By.XPATH, '//a[strong="Settings"]')
}

"""Dashboard page locators"""
dashboard_locators = {
    "title": (By.TAG_NAME, 'h1')
}

"""Leads page locators"""
leads_locators = {
    # lead page
    "title": (By.TAG_NAME, 'h1'),
    "add_lead_button": (By.ID, 'leads-new'),
    "smart_list_button": (By.CLASS_NAME, 'smart-list-view'),
    "smart_list_lead": (By.XPATH, '//div[@id="smart-lists"]//a[text()="{}"]'),
    # create lead locators
    "save_button": (By.CSS_SELECTOR, '.save.btn'),
    "cancel_button": (By.CLASS_NAME, 'cancel btn'),
    "first_name_field": (By.ID, 'lead-first-name'),
    "last_name_field": (By.ID, 'lead-last-name'),
    "company_name_field": (By.ID, 'lead-company-name'),
    "owner_field": (By.ID, 'owner_id_chzn'),
    "title_field": (By.ID, 'lead_title'),
    "lead_status_field": (By.CLASS_NAME, 'status-select'),
    # lead details
    "lead_details_title": (By.CLASS_NAME, 'detail-title'),
    "lead_details_status": (By.CLASS_NAME, 'lead-status'),
}

"""Settings page locators"""
settings_locators = {
    "menu": {
        "manage_accounts": (By.XPATH, '//div[@id="sidebar"]//li[@class="account"]'),
        "manage_users": (By.XPATH, '//div[@id="sidebar"]//li[@class="users"]'),
        "profile": (By.XPATH, '//div[@id="sidebar"]//li[@class="profile"]'),
        "leads": (By.XPATH, '//div[@id="sidebar"]//li[@class="leads"]')
    },
    "profile": {
        "title": (By.TAG_NAME, 'h2'),
        "full_name": (By.ID, 'profileName'),
        "email_address": (By.ID, 'profileEmail')
    },
    "leads": {
        "title": (By.TAG_NAME, 'h2'),
        "lead_sources": (By.LINK_TEXT, 'Lead Sources'),
        "custom_fields": (By.LINK_TEXT, 'Custom Fields'),
        "lead_statuses": {
            "tab": (By.LINK_TEXT, 'Lead Statuses'),
            "status": (By.XPATH, './/h4[text()="{}"]'),
            "edit_status_button": (By.XPATH, '//h4[text()="{}"]/../..//button'),
            "status_name_field": (By.XPATH, '//*[@id="lead-status"]//input[@value="{}"]'),
            "save_button": (By.XPATH, '//*[@id="lead-status"]//button[text()="Save"]')
        },
        "unqualified_reasons": (By.LINK_TEXT, 'Unqualified Reasons'),
        "tags": (By.LINK_TEXT, 'Tags'),
        "smart_links": (By.LINK_TEXT, 'Smart Links'),
        "visits": (By.LINK_TEXT, 'Visits')
    }

}
