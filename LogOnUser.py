from selenium import webdriver

CorrectLogin = "PD0234"
CorrectPass = "123123"
Name = "Piotr"
LastName="Testowy"
email="email@testowy.pl"
Login="PD0001"
PhoneNumber="600500200"

driver = webdriver.Chrome(executable_path=r"C:\Users\pio_g\Desktop\Testy_webdriver\chromedriver.exe")
driver.get("https://precard.efl.com.pl/")

driver.find_element_by_xpath("//a[@test-id='registrationLink']").click()
driver.find_element_by_class_name("box-title").is_displayed()
driver.find_element_by_xpath("//input[@test-id='firstName']").send_keys(Name)
driver.find_element_by_xpath("//input[@test-id='lastName']").send_keys(LastName)
driver.find_element_by_xpath("//input[@test-id='email']").send_keys(email)
driver.find_element_by_xpath("//input[@test-id='login']").send_keys(Login)
driver.find_element_by_xpath("//input[@test-id='phoneNumber']").send_keys(PhoneNumber)
driver.find_element_by_xpath("//input[@test-id='password']").send_keys(CorrectPass)
driver.find_element_by_xpath("//input[@formcontrolname='confirmPassword']").send_keys(CorrectPass)
driver.find_element_by_id("checkToRegister").click()
driver.find_element_by_xpath("//button[@test-id='registerParticipant']").click()
driver.find_element_by_class_name("invalid-feedback")

var = driver.find_element_by_xpath(
    "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[1]") == ("Hasło musi zawierać conajmniej 14 znaków")
var2 = driver.find_element_by_xpath(
    "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]") == ("Podane hasło jest zbyt słabe. Powinno zawierać znaki z trzech spośród czterech następujących grup:")
var3 = driver.find_element_by_xpath(
    "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[1]") == ("Wielkie litery alfabetu (A do Z)")
var4 = driver.find_element_by_xpath(
    "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[2]") == ("Małe litery alfabetu (a do z)")
var5 = driver.find_element_by_xpath(
    "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[3]") == ("Cyfry (0 do 9)")
var6 = driver.find_element_by_xpath(
    "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[4]") == ("Znaki specjalne (np. :, !, $, #, %)")