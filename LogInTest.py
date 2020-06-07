import unittest
from selenium import webdriver


CorrectLogin = "PD0234"
InCorrectPass = "123123"
Name = "Piotr"
LastName = "Testowy"
email = "email@testowy.pl"
Login = "PD0001"
PhoneNumber = "600500200"


class ProloRegistration(unittest.TestCase):

    # Przygotowanie do kazdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\pio_g\Desktop\Testy_webdriver\chromedriver.exe")
        self.driver.get("https://precard.efl.com.pl/")
        self.driver.maximize_window()


    # Sprzatanie po kazdym tescie
    def tearDown(self):
        self.driver.quit()

    def test_login_with_incorrect_pass(self):
        driver = self.driver
        #Kliknij przycisk Nie masz konta
        nie_mam_konta = driver.find_element_by_xpath("//a[@test-id='registrationLink']")
        nie_mam_konta.click()
        #Sprawdzam czy wyświetla się napis Rejestracja
        driver.find_element_by_class_name("box-title").is_displayed()
        #Wpisuję imię
        driver.find_element_by_xpath("//input[@test-id='firstName']").send_keys(Name)
        #Wpisuję nazwisko
        driver.find_element_by_xpath("//input[@test-id='lastName']").send_keys(LastName)
        #Wpisuję e-mail
        driver.find_element_by_xpath("//input[@test-id='email']").send_keys(email)
        #Wpisuję login
        driver.find_element_by_xpath("//input[@test-id='login']").send_keys(Login)
        #Wpisuję numer telefonu
        driver.find_element_by_xpath("//input[@test-id='phoneNumber']").send_keys(PhoneNumber)
        #Wpisuję hasło
        driver.find_element_by_xpath("//input[@test-id='password']").send_keys(InCorrectPass)
        #Powtarzam hasło
        driver.find_element_by_xpath("//input[@formcontrolname='confirmPassword']").send_keys(InCorrectPass)
        #Zaznaczam check-box z regulaminem
        driver.find_element_by_id("checkToRegister").click()
        #Klikam zarejestruj
        driver.find_element_by_xpath("//button[@test-id='registerParticipant']").click()
        #Sprawdzam odpowiedź
        driver.find_element_by_class_name("invalid-feedback")
        #Weryfikuję pierwszą linię odpowiedzi
        var = driver.find_element_by_xpath(
            "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[1]") == (
                  "Hasło musi zawierać conajmniej 14 znaków")
        # Weryfikuję drugą linię odpowiedzi
        var2 = driver.find_element_by_xpath(
            "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]") == (
                   "Podane hasło jest zbyt słabe. Powinno zawierać znaki z trzech spośród czterech następujących grup:")
        # Weryfikuję trzecią linię odpowiedzi
        var3 = driver.find_element_by_xpath(
            "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[1]") == (
                   "Wielkie litery alfabetu (A do Z)")
        # Weryfikuję czwartą linię odpowiedzi
        var4 = driver.find_element_by_xpath(
            "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[2]") == (
                   "Małe litery alfabetu (a do z)")
        # Weryfikuję piatą linię odpowiedzi
        var5 = driver.find_element_by_xpath(
            "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[3]") == (
                   "Cyfry (0 do 9)")
        # Weryfikuję szóstą linię odpowiedzi
        var6 = driver.find_element_by_xpath(
            "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[4]") == (
                   "Znaki specjalne (np. :, !, $, #, %)")


    def test_login_with_out_name(self):
        driver = self.driver
        # Kliknij przycisk Nie masz konta
        nie_mam_konta = driver.find_element_by_xpath("//a[@test-id='registrationLink']")
        nie_mam_konta.click()
        # Sprawdzam czy wyświetla się napis Rejestracja
        driver.find_element_by_class_name("box-title").is_displayed()
        # Wpisuję nazwisko
        driver.find_element_by_xpath("//input[@test-id='lastName']").send_keys(LastName)
        # Wpisuję e-mail
        driver.find_element_by_xpath("//input[@test-id='email']").send_keys(email)
        # Wpisuję login
        driver.find_element_by_xpath("//input[@test-id='login']").send_keys(Login)
        # Wpisuję numer telefonu
        driver.find_element_by_xpath("//input[@test-id='phoneNumber']").send_keys(PhoneNumber)
        # Wpisuję hasło
        driver.find_element_by_xpath("//input[@test-id='password']").send_keys(InCorrectPass)
        # Powtarzam hasło
        driver.find_element_by_xpath("//input[@formcontrolname='confirmPassword']").send_keys(InCorrectPass)
        # Zaznaczam check-box z regulaminem
        driver.find_element_by_id("checkToRegister").click()
        # Klikam zarejestruj
        driver.find_element_by_xpath("//button[@test-id='registerParticipant']").click()
        # Sprawdzam odpowiedź
        driver.find_element_by_class_name("invalid-feedback")
        Imie = driver.find_element_by_xpath(
               "/html/body/app-root/app-registration/section/div/div[1]/div/div/div[2]/form/div[1]/div[1]/div/div/div") == (
            "Pole jest wymagane")


if __name__ == '__main__':
    unittest.main(verbosity=2)