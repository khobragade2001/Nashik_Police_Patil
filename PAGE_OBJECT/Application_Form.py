from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class application_pages:
    x = By.XPATH
    click_apply_police_patil = (x, "//a[contains(text(),'पोलीस पाटील पदासाठी अर्ज करण्यासाठी येथे क्लिक करा')]")
    click_upvibhag_name = (x, "//select[@id='SDO']")
    click_talukka_name = (x, "//select[@id='Taluka']")
    click_gaon_name = (x, "//select[@id='Village']")
    click_rahivasi_yes_no = (x, "//select[@id='Village_Resident']")
    click_photo = (x, "//input[@id='photo']")
    click_hole_name = (x, "//input[@id='Candidate_Name']")
    click_add = (x, "//input[@id='Address']")
    click_mobile_no = (x, "//input[@id='Mobile_No']")
    click_email_id = (x, "//input[@id='Email_ID']")
    click_DOB = (x, "//input[@id='DOB']")
    click_month_DD = (x, "//select[@class='ui-datepicker-month']")
    click_date_DD = (x, "//a[@class='ui-state-default ui-state-hover']")
    DD_gender = (x, "//select[@id='Gender']")
    DD_marital_status = (x, "//select[@id='Married_status']")
    click_child = (x, "//input[@id='Child_details']")
    DD_cast = (x, "//select[@id='Cast']")
    click_ten_school_name = (x, "//input[@id='Tenth_School_Name']")
    click_ten_pass_year = (x, "//input[@id='Tenth_Passing_Year']")
    click_ten_marks_obtain = (x, "//input[@id='Tenth_Marks_Gained']")
    click_ten_total_mark = (x, "//input[@id='Tenth_Total']")
    click_ten_percentage = (x, "//input[@id='Tenth_Percentage']")

    click_12_school_name = (x, "//input[@id='Twelfth_School_Name']")
    click_12_pass_year = (x, "//input[@id='Twelfth_Passing_Year']")
    click_12_marks_obtain = (x, "//input[@id='Twelfth_Marks_Gained']")
    click_12_total_mark = (x, "//input[@id='Twefth_Total']")
    click_12_percentage = (x, "//input[@id='Twelfth_Percentage']")

    click_Graduation_school_name = (x, "//input[@id='Graduation_School_Name']")
    click_Graduation_pass_year = (x, "//input[@id='Graduation_Passing_Year']")
    click_Graduation_marks_obtain = (x, "//input[@id='Graduation_Marks_Gained']")
    click_Graduation_total_mark = (x, "//input[@id='Graduation_Total']")
    click_Graduation_percentage = (x, "//input[@id='Graduation_Percentage']")

    DD_have_cast_certificate = (x, "//select[@id='Cast_Certificate']")
    click_cast_certificate_no = (x, "//input[@id='Cast_Certificate_No']")
    click_cast_certificate_date = (x, "//input[@id='Cast_Certificate_Date']")
    DD_Handicap_yes_no = (x, "//select[@id='Doctor_Certificate']")
    DD_Non_creamy_layer = (x, "//select[@id='Non_Creamylayer']")

    click_upload_cast_certificate_file = (x, "//input[@id='Cast_Certificate_file']")
    click_upload_non_creamy_layer_file = (x, "//input[@id='Non_Creamylayer_Certificate']")
    click_upload_medical_fitness_file = (x, "//input[@id='Medical_Certificate']")
    click_upload_ten_certificate_file = (x, "//input[@id='SSC_Doc']")
    click_upload_ews_fle = (x, "//input[@id='ews_doc']")
    click_rahiwasi_file = (x, "//input[@id='Address_doc']")

    click_declaration = (x, "//input[@id='Declaration']")
    click_upload_sign_file = (x, "//input[@id='sign']")
    click_pay_and_submit_button = (x, "//input[@id='btnsubmit']")
    click_final_submit_pop_button = (x, "//button[normalize-space()='Yes']")

    click_cards_details_option = (x, "//body/div/div/div[@role='dialog']/div[@role='document']/div[@class='modal-content']/div[@id='overlay']/div[@id='sdkPopup']/div[@class='popupBody']/div[@class='section']/div[@class='roundedCard']/a[1]")
    click_enter_card_no = (x, "//input[@placeholder='XXXX XXXX XXXX XXXX']")
    click_enter_card_holder_name = (x, "//input[@id='nameOnCard']")
    click_valid_upto = (x, "//input[@id='expdate']")
    click_cvv_code = (x, "//input[@id='cvv']")
    click_proceed_to_payment_button = (x, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def enter_apply_police_patil(self):
        self.driver.find_element(*application_pages.click_apply_police_patil).click()

    def enter_upvibhag_dd(self):
        vibhag = Select(self.driver.find_element(*application_pages.click_upvibhag_name))
        vibhag.select_by_index("1")

    def enter_dd_talukka_name(self):
        talukka = Select(self.driver.find_element(*application_pages.click_talukka_name))
        talukka.select_by_index("1")

    def enter_dd_gaon_name(self):
        gav = Select(self.driver.find_element(*application_pages.click_gaon_name))
        gav.select_by_index("1")

    def enter_dd_rahivasi_yes_no(self):
        rahivasi = Select(self.driver.find_element(*application_pages.click_rahivasi_yes_no))
        rahivasi.select_by_index("1")

    def enter_photo_upload(self, photos):
        self.driver.find_element(*application_pages.click_photo).send_keys(photos)

    def enter_full_name(self, name):
        self.driver.find_element(*application_pages.click_hole_name).send_keys(name)

    def enter_add(self, add):
        self.driver.find_element(*application_pages.click_add).send_keys(add)

    def enter_mobile_no(self, mobile):
        self.driver.find_element(*application_pages.click_mobile_no).send_keys(mobile)

    def enter_email_id(self, mail):
        self.driver.find_element(*application_pages.click_email_id).send_keys(mail)

    def enter_DD_dob(self, dob):
        self.driver.find_element(*application_pages.click_DOB).send_keys(dob)

    def enter_gender(self):
        Gender = Select(self.driver.find_element(*application_pages.DD_gender))
        Gender.select_by_index("1")

    def enter_marital_status(self):
        Gender = Select(self.driver.find_element(*application_pages.DD_marital_status))
        Gender.select_by_index("1")

    def enter_no_chield(self, child):
        self.driver.find_element(*application_pages.click_child).send_keys(child)

    def enter_cast(self):
        Cast = Select(self.driver.find_element(*application_pages.DD_cast))
        Cast.select_by_index("1")

    def enter_ten_school_name(self, school_name):
        self.driver.find_element(*application_pages.click_ten_school_name).send_keys(school_name)

    def enter_ten_passing_year(self, ten_pass_year):
        self.driver.find_element(*application_pages.click_ten_pass_year).send_keys(ten_pass_year)

    def enter_ten_mark_obtain(self, ten_mark_obtain):
        self.driver.find_element(*application_pages.click_ten_marks_obtain).send_keys(ten_mark_obtain)

    def enter_ten_total_mark(self, ten_total_mark):
        self.driver.find_element(*application_pages.click_ten_total_mark).send_keys(ten_total_mark)

    def enter_ten_percentage(self, ten_percentage):
        self.driver.find_element(*application_pages.click_ten_percentage).send_keys(ten_percentage)

    def enter_12_school_name(self, twel_school_name):
        self.driver.find_element(*application_pages.click_12_school_name).send_keys(twel_school_name)

    def enter_12_passing_year(self, twel_pass_year):
        self.driver.find_element(*application_pages.click_12_pass_year).send_keys(twel_pass_year)

    def enter_12_mark_obtain(self, twel_mark_obtain):
        self.driver.find_element(*application_pages.click_12_marks_obtain).send_keys(twel_mark_obtain)

    def enter_12_total_mark(self, twel_total_mark):
        self.driver.find_element(*application_pages.click_12_total_mark).send_keys(twel_total_mark)

    def enter_12_percentage(self, twel_percentage):
        self.driver.find_element(*application_pages.click_12_percentage).send_keys(twel_percentage)

    def enter_graduation_school_name(self, gra_school_name):
        self.driver.find_element(*application_pages.click_Graduation_school_name).send_keys(gra_school_name)

    def enter_graduation_passing_year(self, gra_pass_year):
        self.driver.find_element(*application_pages.click_Graduation_pass_year).send_keys(gra_pass_year)

    def enter_graduation_mark_obtain(self, gra_mark_obtain):
        self.driver.find_element(*application_pages.click_Graduation_marks_obtain).send_keys(gra_mark_obtain)

    def enter_graduation_total_mark(self, gra_total_mark):
        self.driver.find_element(*application_pages.click_Graduation_total_mark).send_keys(gra_total_mark)

    def enter_graduation_percentage(self, gra_percentage):
        self.driver.find_element(*application_pages.click_Graduation_percentage).send_keys(gra_percentage)

    def enter_have_cast_certificate(self):
        Cast_certificate = Select(self.driver.find_element(*application_pages.DD_have_cast_certificate))
        Cast_certificate.select_by_index("1")

    def enter_cast_certificate_number(self, cast_number):
        self.driver.find_element(*application_pages.click_cast_certificate_no).send_keys(cast_number)

    def enter_cast_certificate_date(self, cast_date):
        self.driver.find_element(*application_pages.click_cast_certificate_date).send_keys(cast_date)

    def enter_handicap_yes_no(self):
        Handicap = Select(self.driver.find_element(*application_pages.DD_Handicap_yes_no))
        Handicap.select_by_index("1")

    def enter_non_creamy_layer_yes_no(self):
        Non_creamy = Select(self.driver.find_element(*application_pages.DD_Non_creamy_layer))
        Non_creamy.select_by_index("1")

    def upload_cast_certificate(self, cast_certificate_image):
        self.driver.find_element(*application_pages.click_upload_cast_certificate_file).send_keys(cast_certificate_image)

    def upload_non_creamy_layer(self, non_creamy_layer_image):
        self.driver.find_element(*application_pages.click_upload_non_creamy_layer_file).send_keys(non_creamy_layer_image)

    def upload_medical_fitness(self, medical_fitness):
        self.driver.find_element(*application_pages.click_upload_medical_fitness_file).send_keys(medical_fitness)

    def upload_ten_certificate(self, ten_certificate_image):
        self.driver.find_element(*application_pages.click_upload_ten_certificate_file).send_keys(ten_certificate_image)

    def upload_rahivasi(self, rahivasi_image):
        self.driver.find_element(*application_pages.click_rahiwasi_file).send_keys(rahivasi_image)

    def enter_declaration(self):
        self.driver.find_element(*application_pages.click_declaration).click()

    def enter_sing_file(self, sign_image):
        self.driver.find_element(*application_pages.click_upload_sign_file).send_keys(sign_image)

    def enter_pay_and_submit_button(self):
        self.driver.find_element(*application_pages.click_pay_and_submit_button).click()

    def enter_final_submit_pop(self):
        self.driver.find_element(*application_pages.click_final_submit_pop_button).click()

    def enter_card_detail_brand(self):
        self.driver.find_element(*application_pages.click_cards_details_option).click()

    def enter_card_no(self, card_no):
        self.driver.find_element(*application_pages.click_enter_card_no).send_keys(card_no)

    def enter_card_holder_name(self, card_holder_name):
        self.driver.find_element(*application_pages.click_enter_card_holder_name).send_keys(card_holder_name)

    def enter_valid_upto(self, valid_upto):
        self.driver.find_element(*application_pages.click_valid_upto).send_keys(valid_upto)

    def enter_cvv(self, cvv):
        self.driver.find_element(*application_pages.click_cvv_code).send_keys(cvv)

    def enter_proceed_to_payment_button(self):
        self.driver.find_element(*application_pages.click_proceed_to_payment_button).click()


















